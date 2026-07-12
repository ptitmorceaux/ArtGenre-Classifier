import os
import numpy as np
import pandas as pd
from PIL import Image

import engine.core.config as cf


def load_and_prepare_csv() -> dict:
    """
    Charge les CSV par catégorie (train/test) et construit la structure imbriquée :
    {
        "train": {"csv": {category: DataFrame}, "img": {}},
        "test":  {"csv": {category: DataFrame}, "img": {}},
    }
    Le découpage One-vs-All (1/-1) n'est plus pré-calculé ici : il se fait à la volée
    dans build_one_vs_all_train_arrays(), une fois les images chargées.
    """
    data = {
        "train": {"csv": dict(), "img": dict()},
        "test": {"csv": dict(), "img": dict()},
    }

    cf.CONFIG["dataset"]["count_total_dataset"] = {
        "loaded": dict(),
        "used_during_train": dict(),
    }

    for step, categories in cf.CONFIG["dataset"]["categories"].items():

        if step not in ["train", "test"]:
            raise ValueError(f"load_and_prepare_csv(): step invalide '{step}'. Doit être 'train' ou 'test'.")

        if step not in cf.CONFIG["dataset"]["count_total_dataset"]["loaded"]:
            cf.CONFIG["dataset"]["count_total_dataset"]["loaded"][step] = {"total": 0, "categories": dict()}

        for category, paths in categories.items():
            df = pd.read_csv(paths["csv_path"])
    
            if df.empty:
                raise ValueError(f"Le fichier CSV pour la catégorie '{category}' est vide ou introuvable.")

            limit_config = cf.CONFIG["dataset"]["limit_per_category"]
            limit = limit_config.get(category, -1) if isinstance(limit_config, dict) else limit_config

            if step == "train" and limit > 0:
                n_df = len(df)
                if limit > n_df:
                    raise ValueError(
                        f"load_and_prepare_csv(): 'limit_per_category' ({limit}) dépasse le nombre "
                        f"d'images disponibles pour la catégorie '{category}' ({n_df}). "
                        f"Baisse 'limit_per_category' à {n_df} ou moins."
                    )
                df = df.sample(
                    n=limit,
                    random_state=cf.CONFIG["lib"]["seed"]
                ).reset_index(drop=True)

            n_df = len(df)
            cf.CONFIG["dataset"]["count_total_dataset"]["loaded"][step]["categories"][category] = n_df
            cf.CONFIG["dataset"]["count_total_dataset"]["loaded"][step]["total"] += n_df

            if "Nom_Fichier" not in df.columns:
                raise ValueError("La colonne 'Nom_Fichier' n'existe pas dans le DataFrame.")

            # Transformation du nom en chemin complet
            df["filepath"] = df["Nom_Fichier"].apply(lambda x: os.path.join(paths["data_folder_path"], x))

            data[step]["csv"][category] = df

    cf.CONFIG["dataset"]["count_total_dataset"]["loaded"]["total"] = sum(
        cf.CONFIG["dataset"]["count_total_dataset"]["loaded"][step]["total"] for step in cf.CONFIG["dataset"]["count_total_dataset"]["loaded"]
    )

    return data


def load_images_from_filepaths(data: dict, step: str) -> dict[str, np.ndarray]:
    """
    Charge (Pillow) les images de toutes les catégories du `step` donné ('train' ou
    'test') et RENVOIE un dict {category: np.ndarray} (une image aplatie par ligne).

    Ne mute pas `data` : c'est à l'appelant d'assigner le résultat, ex.
    `data[step]["img"] = load_images_from_filepaths(data, step)`.

    Ne charge qu'un seul step à la fois : permet de libérer la RAM du train avant
    de charger le test (cf. main.py).
    """
    images_per_category = dict()

    for category, df in data[step]["csv"].items():
        filepaths = df["filepath"].tolist()
        total = len(filepaths)
        images = list()

        for i, filepath in enumerate(filepaths):
            if i % 50 == 0 or i == total - 1:
                print(f"\rChargement {step}/{category}... {i+1}/{total} ({100*(i+1)/total:.2f}%)", end="", flush=True)

            img = Image.open(filepath).convert("RGB")
            img_array = np.array(img).flatten().astype(np.float32)

            if "W_length" not in cf.CONFIG["dataset"]:
                cf.CONFIG["dataset"]["W_length"] = len(img_array)
            elif len(img_array) != cf.CONFIG["dataset"]["W_length"]:
                raise ValueError(
                    f"Image at {filepath} has a different size ({len(img_array)}) "
                    f"than expected ({cf.CONFIG['dataset']['W_length']})."
                )

            images.append(img_array)
        print()

        images_per_category[category] = np.array(images)

    return images_per_category


def _split_negative_quota(total_negatives_needed: int, n_other_categories: int) -> list[int]:
    """
    Répartit le nombre total de négatifs nécessaires le plus équitablement possible
    entre les autres catégories (ex: 10 négatifs / 3 catégories -> [4, 3, 3]).
    """
    base = total_negatives_needed // n_other_categories
    remainder = total_negatives_needed % n_other_categories
    return [base + 1 if i < remainder else base for i in range(n_other_categories)]


def build_one_vs_all_train_arrays(data: dict, category: str) -> tuple[np.ndarray, list[int]]:
    """
    Construit (X, Y) One-vs-All pour le TRAIN d'un modèle donné :
    positifs = data["train"]["img"][category], négatifs = toutes les autres catégories.
    X est renvoyé APLATI (1D, row-major) pour alimenter directement model.train().

    Si cf.CONFIG["dataset"]["train_positive_ratio"] != -1, le dataset est rééquilibré
    SANS JAMAIS dupliquer d'images (uniquement du sous-échantillonnage) :

    - Si le ratio demandé est atteignable en gardant TOUS les positifs (ratio >= ratio
      naturel = positifs / (positifs + négatifs disponibles)) : les négatifs sont
      sous-échantillonnés, répartis le plus équitablement possible entre les autres
      catégories.
    - Si le ratio demandé est INFÉRIEUR au ratio naturel (il faudrait plus de négatifs
      que ce qui existe) : impossible d'ajouter des négatifs sans dupliquer, donc on
      utilise TOUS les négatifs disponibles et on réduit les POSITIFS à la place, pour
      atteindre exactement le ratio demandé.

    Dans tous les cas (ratio -1, >= naturel, ou < naturel), une ligne [INFO] est
    affichée avec le nombre de positifs/négatifs utilisés et le ratio obtenu.

    S'applique APRÈS limit_per_category (qui a déjà fixé N_pos au moment du chargement
    des images).

    Enregistre aussi, pour ce modèle, le nombre d'images réellement utilisées par
    catégorie dans
    cf.CONFIG["dataset"]["count_total_dataset"]["used_during_train"]["model_<category>"]["categories"]
    (ex: {"impressionism": 500, "realism": 250, "romanticism": 250}).
    """
    # On prend celles qui ont le plus de données (other_categories) pour éviter de dépasser le nombre d'images disponibles
    sorted_other_categories = sorted(
        data["train"]["img"].keys(),
        key=lambda c: cf.CONFIG["dataset"]["count_total_dataset"]["loaded"]["train"]["categories"][c],
        reverse=True
    )

    positives_available = data["train"]["img"][category]
    n_positives_available = len(positives_available)
    other_categories = [c for c in sorted_other_categories if c != category]

    if not other_categories:
        raise ValueError("build_one_vs_all_train_arrays(): il faut au moins 2 catégories pour du One-vs-All.")

    rng = np.random.default_rng(cf.CONFIG["lib"]["seed"])
    ratio = cf.CONFIG["dataset"]["train_positive_ratio"]
    if ratio != -1 and (ratio <= 0 or ratio >= 1):
        raise ValueError("build_one_vs_all_train_arrays(): ratio invalide. Doit être compris entre 0 et 1 exclus (ou -1 pour tous).")

    total_negatives_available = sum(len(data["train"]["img"][c]) for c in other_categories)

    if ratio == -1:
        # Pas de rework : tout est gardé tel quel.
        positives = positives_available
        negatives_parts = [data["train"]["img"][c] for c in other_categories]
        counts_used = {"total": n_positives_available, "categories": {category: n_positives_available}}
        for cat in other_categories:
            available = data["train"]["img"][cat]
            counts_used["categories"][cat] = len(available)
            counts_used["total"] += len(available)

    else:
        natural_ratio = n_positives_available / (n_positives_available + total_negatives_available)

        if ratio >= natural_ratio:
            # Cas standard : on garde TOUS les positifs, on sous-échantillonne les négatifs.
            positives = positives_available
            total_negatives_needed = round(n_positives_available * (1 - ratio) / ratio)
            quotas = _split_negative_quota(total_negatives_needed, len(other_categories))

            negatives_parts = []
            counts_used = {"total": n_positives_available, "categories": {category: n_positives_available}}
            for cat, quota in zip(other_categories, quotas):
                available = data["train"]["img"][cat]
                n_available = len(available)
                if quota > n_available:
                    # Filet de sécurité : ne devrait pas arriver puisque ratio >= natural_ratio
                    # garantit que le total est atteignable, mais une répartition très inégale
                    # entre catégories pourrait ponctuellement dépasser une catégorie précise.
                    raise ValueError(
                        f"build_one_vs_all_train_arrays(): ratio {ratio} pour '{category}' demande "
                        f"{quota} négatifs depuis '{cat}' mais seulement {n_available} disponibles."
                    )
                idx = rng.choice(n_available, size=quota, replace=False)
                negatives_parts.append(available[idx])
                counts_used["categories"][cat] = quota
                counts_used["total"] += quota

        else:
            # Ratio demandé en dessous du ratio naturel : impossible d'ajouter des négatifs
            # sans dupliquer. On garde TOUS les négatifs disponibles (déjà le maximum) et on
            # réduit les POSITIFS pour atteindre exactement le ratio demandé.
            n_positives_target = round(total_negatives_available * ratio / (1 - ratio))

            idx = rng.choice(n_positives_available, size=n_positives_target, replace=False)
            positives = positives_available[idx]
            negatives_parts = [data["train"]["img"][c] for c in other_categories]

            counts_used = {"total": n_positives_target, "categories": {category: n_positives_target}}
            for cat in other_categories:
                available = data["train"]["img"][cat]
                counts_used["categories"][cat] = len(available)
                counts_used["total"] += len(available)

    n_pos_final = counts_used["categories"][category]
    n_neg_final = counts_used["total"] - n_pos_final
    achieved_ratio = n_pos_final / counts_used["total"]
    suffix = ", natural" if ratio == -1 else ""
    print(f"[INFO] '{category}': {n_pos_final} pos / {n_neg_final} neg (ratio={achieved_ratio:.3f}{suffix})")

    cf.CONFIG["dataset"]["count_total_dataset"]["used_during_train"][f"model_{category}"] = counts_used

    negatives = np.concatenate(negatives_parts, axis=0)

    X = np.concatenate([positives, negatives], axis=0)
    Y = [1] * len(positives) + [-1] * len(negatives)

    perm = rng.permutation(len(Y))
    X = X[perm]
    Y = [Y[i] for i in perm]

    return X.flatten(), Y


def build_multiclass_test_arrays(data: dict) -> tuple[np.ndarray, list[str]]:
    """
    Construit le tableau de test 2D combiné (toutes catégories, une image par
    ligne) et la liste des catégories attendues (même ordre), pour l'évaluation
    multiclasse.
    """
    X_parts, expected = [], []
    for category, imgs in data["test"]["img"].items():
        X_parts.append(imgs)
        expected.extend([category] * len(imgs))

    return np.concatenate(X_parts, axis=0), expected