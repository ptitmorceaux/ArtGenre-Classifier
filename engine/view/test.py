# ruff: noqa
"""
test.py

Charge un modèle One-vs-All déjà entraîné (le meilleur par défaut, selon la
Top-1 Accuracy multiclasse, ou un run donné via --model_path), charge une image
(par défaut ./engine/view/test.png), vérifie qu'il s'agit bien d'une image
valide, la redimensionne en 64x64 et l'aplatit en ndarray 1D. L'image est
ensuite normalisée avec le scaler sauvegardé avec le modèle, puis chaque
modèle de catégorie (One-vs-All) prédit un score de confiance. Les scores sont
affichés dans le terminal, la catégorie la plus probable (score le plus élevé)
étant mise en évidence.

Le mode de prédiction (`is_classification`) dépend du type de modèle du run
(`config.json` -> model.type) :
- "mlp"    -> is_classification=True  : le MLP a une vraie couche d'activation
              (tanh) en sortie, le score est donc borné dans ]-1, 1[.
- "linear" -> is_classification=False : un modèle linéaire n'a pas de fonction
              d'activation, `predict_linear_classification`/`predict_linear_regression`
              renvoient tous les deux la même somme brute w·x+b (non bornée) ;
              is_classification=False évite juste l'aller-retour inutile par
              `predict_linear_classification`.

Se base sur/réutilise les fonctions existantes du moteur :
- engine.core.build.load_c_library()          -> charge la lib C (déjà compilée)
- engine.interop.storage.Storage["load"]      -> charge un modèle + son scaler (.bin)
- engine.view.top_models.collect_runs()       -> pour trouver le meilleur run

Usage:
    python -m engine.view.test
    python -m engine.view.test -i chemin/vers/image.png
    python -m engine.view.test -p engine/core/output/linear/2026-07-12/01-36-00_123456

NOTE : un "run" correspond au dossier de logs d'un entraînement, de la forme
       engine/core/output/<model_type>/<YYYY-mm-dd>/<HH-MM-SS_ms>/
       (voir config.py -> get_date_time_now() / init_config()). Il doit contenir
       un fichier 'config.json' et un sous-dossier 'models/' avec un .bin par
       catégorie (voir persistence.py -> save_trained_models()).
"""

import argparse
import glob
import json
import os
import sys

import numpy as np
from PIL import Image, UnidentifiedImageError

# On ajoute la racine du projet au sys.path, comme le fait main.py, pour que
# les imports `engine.xxx` fonctionnent quel que soit le dossier d'exécution.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)

import engine.core.config as cf
from engine.core.build import load_c_library
from engine.interop.storage import Storage
from engine.view.top_models import collect_runs, UNKNOWN


DEFAULT_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "test.png")
OUTPUT_GLOB_PATTERN = os.path.join(PROJECT_ROOT, "engine", "core", "output", "*", "*", "*", "*.json")
IMG_SIZE = (64, 64)  # doit correspondre au format attendu par les modèles (cf. config.py)


#====== Arguments CLI ======#

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Teste un modèle One-vs-All entraîné sur une image donnée."
    )
    parser.add_argument(
        "-i", "--image",
        dest="image_path",
        type=str,
        default=DEFAULT_IMAGE_PATH,
        help=f"Chemin vers l'image à tester (défaut: '{DEFAULT_IMAGE_PATH}').",
    )
    parser.add_argument(
        "-p", "--model_path",
        dest="model_path",
        type=str,
        default=None,
        help="Chemin vers le dossier du run à charger "
             "(ex: 'engine/core/output/linear/2026-07-12/01-36-00_123456'). "
             "Si non fourni, charge automatiquement le run avec la meilleure Top-1 Accuracy.",
    )
    return parser.parse_args()


#====== Résolution de chemins ======#

def _resolve_path(path: str) -> str:
    """Résout un chemin relatif par rapport à la racine du projet si besoin (le
    CWD au moment de l'exécution peut différer du dossier racine du projet)."""
    if os.path.isabs(path) and os.path.exists(path):
        return path
    if os.path.exists(path):
        return os.path.abspath(path)
    candidate = os.path.join(PROJECT_ROOT, path)
    if os.path.exists(candidate):
        return candidate
    return path  # tel quel : l'erreur explicite sera levée par l'appelant


def find_best_run_path() -> str:
    """Trouve le dossier du run avec la meilleure Top-1 Accuracy (multiclasse),
    en se basant sur les config.json déjà sauvegardés (cf. top_models.py)."""
    runs = collect_runs(OUTPUT_GLOB_PATTERN)
    if not runs:
        raise FileNotFoundError(
            f"find_best_run_path(): Aucun run valide trouvé avec le pattern '{OUTPUT_GLOB_PATTERN}'."
        )

    best_run = max(runs, key=lambda r: r["top1_accuracy"])
    if best_run["path"] == UNKNOWN:
        raise ValueError("find_best_run_path(): Impossible de déterminer le chemin du meilleur run.")

    print(
        f"[*] Meilleur run trouvé : '{best_run['path']}' "
        f"(Top-1 Accuracy: {best_run['top1_accuracy'] * 100:.2f}%, model={best_run['model_type']})"
    )
    return _resolve_path(best_run["path"])


#====== Chargement du run (config + modèles + scaler) ======#

def load_run_config(run_path: str) -> dict:
    """Charge le config.json sauvegardé à la fin de l'entraînement (déjà 'finalisé',
    pas besoin de repasser par init_config())."""
    config_path = os.path.join(run_path, "config.json")
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"load_run_config(): fichier de configuration introuvable : '{config_path}'.")

    with open(config_path, "r") as f:
        return json.load(f)


def load_models_for_run(run_path: str, run_config: dict) -> tuple[dict, object]:
    """
    Charge tous les modèles One-vs-All (un fichier .bin par catégorie, cf.
    persistence.save_trained_models()) du dossier 'models/' du run, ainsi que le
    scaler partagé (le même scaler est sauvegardé avec chaque modèle -> on ne le
    lit qu'une fois).
    """
    models_folder = os.path.join(run_path, "models")
    bin_files = sorted(glob.glob(os.path.join(models_folder, "*.bin")))

    if not bin_files:
        raise FileNotFoundError(f"load_models_for_run(): Aucun fichier .bin trouvé dans '{models_folder}'.")

    models_per_category = dict()
    scaler = None

    for filepath in bin_files:
        # Nom de fichier : "{model_type}__{category}__{date}.bin" (cf. persistence.py)
        filename = os.path.basename(filepath)
        parts = filename.split("__")
        if len(parts) < 2:
            print(f"[!] Nom de fichier inattendu, ignoré : '{filename}'")
            continue
        category = parts[1]

        model, model_scaler = Storage["load"](filepath)
        models_per_category[category] = model

        if scaler is None:
            scaler = model_scaler

        print(f"[*] Modèle chargé pour '{category}' : '{filename}'")

    if scaler is None:
        raise ValueError("load_models_for_run(): Aucun scaler n'a pu être chargé depuis les fichiers .bin.")

    expected_categories = list(run_config.get("dataset", {}).get("categories", {}).get("train", {}).keys())
    missing = [c for c in expected_categories if c not in models_per_category]
    if missing:
        print(f"[!] ATTENTION : catégories attendues mais manquantes parmi les modèles chargés : {missing}")

    return models_per_category, scaler


#====== Image : chargement / validation / prétraitement ======#

def load_and_preprocess_image(image_path: str) -> np.ndarray:
    """
    Charge une image, vérifie qu'il s'agit bien d'une image valide (non
    corrompue), la convertit en RGB, la redimensionne en 64x64, puis l'aplatit
    en ndarray 1D de float32 (même format que dataset.load_images_from_filepaths).
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"load_and_preprocess_image(): image introuvable : '{image_path}'.")

    try:
        with Image.open(image_path) as img_check:
            img_check.verify()  # vérifie l'intégrité du fichier (sans le décoder complètement)
    except (UnidentifiedImageError, OSError) as e:
        raise ValueError(f"load_and_preprocess_image(): fichier image invalide '{image_path}' : {e}")

    # img.verify() invalide l'objet pour toute utilisation ultérieure -> on rouvre l'image.
    img = Image.open(image_path).convert("RGB")

    if img.size != IMG_SIZE:
        print(f"[*] Redimensionnement de l'image {img.size} -> {IMG_SIZE}")
        resample = getattr(Image, "Resampling", Image).LANCZOS
        img = img.resize(IMG_SIZE, resample)

    img_array = np.array(img).flatten().astype(np.float32)
    return img_array


#====== Prédiction ======#

def predict_all_categories(models_per_category: dict, X: list, is_classification: bool) -> dict[str, float]:
    """
    Renvoie, pour chaque catégorie, le score de confiance de son modèle One-vs-All.

    `is_classification` doit être déterminé par l'appelant à partir du type de
    modèle du run (cf. main()) :
    - MLP    -> True  : applique tanh en sortie -> score borné dans ]-1, 1[.
    - Linear -> False : pas d'activation -> score brut w·x+b, non borné
                        (identique au score utilisé pour l'argmax multiclasse
                        dans evaluation.evaluate_models()).
    """
    scores = dict()
    for category, model in models_per_category.items():
        output = model.predict(X, is_classification=is_classification)
        scores[category] = float(output[0] if isinstance(output, list) else output)
    return scores


#====== Affichage ======#

def _enable_ansi_on_windows() -> None:
    """Active l'interprétation des séquences ANSI dans cmd.exe (no-op ailleurs)."""
    if sys.platform.startswith("win"):
        os.system("")


def print_predictions(scores: dict[str, float], is_classification: bool) -> None:
    """Affiche le score de chaque catégorie (triés du plus élevé au plus bas),
    en mettant en évidence la catégorie la plus probable (score le plus élevé)."""
    _enable_ansi_on_windows()
    BOLD, GREEN, RESET = "\033[1m", "\033[92m", "\033[0m"

    best_category = max(scores, key=lambda c: scores[c])
    width = max(len(c) for c in scores) + 2

    label = "score tanh, borné ]-1, 1[" if is_classification else "score brut w·x+b, non borné"
    print(f"\n========>>> PREDICTION ({label}) <<<========\n")
    for category, value in sorted(scores.items(), key=lambda kv: kv[1], reverse=True):
        if category == best_category:
            print(f"{BOLD}{GREEN}  ==> {category.ljust(width)}: {value:+.6f}   <== PLUS PROBABLE{RESET}")
        else:
            print(f"      {category.ljust(width)}: {value:+.6f}")
    print()


#====== Main ======#

def main() -> None:
    args = parse_args()

    run_path = _resolve_path(args.model_path) if args.model_path else find_best_run_path()
    if not os.path.isdir(run_path):
        raise FileNotFoundError(f"main(): dossier de run introuvable : '{run_path}'.")
    print(f"[*] Chargement du run : '{run_path}'")

    run_config = load_run_config(run_path)

    # La config sauvegardée est déjà complète/finalisée (post-entraînement) :
    # pas besoin de repasser par init_config()/finalize_mlp_config().
    cf.CONFIG = run_config

    # Charge la lib C (déjà compilée lors de l'entraînement) : nécessaire pour
    # Storage["load"] et pour model.predict().
    load_c_library()

    models_per_category, scaler = load_models_for_run(run_path, run_config)
    print(f"[*] {len(models_per_category)} modèle(s) chargé(s) : {list(models_per_category.keys())}")

    # Seul le MLP a une vraie fonction d'activation en sortie (tanh) : on ne
    # demande is_classification=True que dans ce cas (cf. docstring du module).
    model_type = run_config["model"]["type"]
    is_classification = (model_type == "mlp")
    print(f"[*] Type de modèle : '{model_type}' -> is_classification={is_classification}")

    print(f"[*] Chargement de l'image : '{args.image_path}'")
    img_array = load_and_preprocess_image(args.image_path)

    X_normalized = scaler.transform(img_array)

    scores = predict_all_categories(models_per_category, X_normalized, is_classification)
    print_predictions(scores, is_classification)


if __name__ == "__main__":
    main()