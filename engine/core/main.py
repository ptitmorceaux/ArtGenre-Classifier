# ruff: noqa
import os
import sys
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from engine.core.config import CONFIG
from engine.core.build import compile_c_library, load_c_library
from engine.core.dataset import load_and_prepare_csv, load_images_from_filepaths
from engine.core.preprocessing import standardize_data
from engine.core.training import train_models
from engine.core.persistence import save_trained_models, save_config_json
from engine.core.evaluation import evaluate_models, plot_confusion_matrix


def select_seed():
    if CONFIG["lib"]["seed"] is None:
        if CONFIG["lib"]["seeds_choice"] is None:
            raise ValueError("CONFIG['lib']['seeds_choice'] doit être défini si CONFIG['lib']['seed'] est None.")
        CONFIG["lib"]["seed"] = random.choice(CONFIG["lib"]["seeds_choice"])
    if not isinstance(CONFIG["lib"]["seed"], int):
        raise ValueError("CONFIG['lib']['seed'] doit être un entier ou None.")


def main():

    # INFO
    print(f"\n# INFO :")
    print(f"[*] Start TensorBoard with: tensorboard --logdir={CONFIG['output']['folder']} --port=6007")

    # 1. Gestion de l'aléa
    select_seed()
    print(f"\n# Etape 1 : Seed sélectionnée : {CONFIG['lib']['seed']}")

    # 2. Compilation et chargement de l'interopérabilité
    print("\n# Etape 2 : Compilation et chargement de l'interopérabilité...")
    compile_c_library()
    load_c_library()

    # 3. Préparation des données
    print("\n# Etape 3 : Préparation des données...")
    df_X_filepaths, df_Y = load_and_prepare_csv()
    df_X = load_images_from_filepaths(df_X_filepaths)
    df_X, scaler = standardize_data(df_X)

    # 4. Entraînement
    print("\n# Etape 4 : Entraînement des modèles et enregistrement des logs pour tensorboard...")
    models_per_category = train_models(df_X, df_Y)

    # 5. Sauvegarde de la configuration en json
    print("\n# Etape 5 : Sauvegarde de la configuration...")
    save_config_json(CONFIG["output"]["logs"], CONFIG)

    # 6. Sauvegarde des modèles entraînés + du scaler utilisé (un fichier par catégorie).
    #    Les modèles restent en mémoire ensuite pour l'évaluation ci-dessous.
    print("\n# Etape 6 : Sauvegarde des modèles entraînés...")
    save_trained_models(models_per_category, scaler, CONFIG["output"]["models"], CONFIG["model"]["type"])

    # 7. Évaluation et Visualisation
    print("\n# Etape 7 : Évaluation et Visualisation...")
    df_predictions_expected, df_predictions_test = evaluate_models(models_per_category, df_X, df_Y)
    plot_confusion_matrix(df_predictions_expected, df_predictions_test, df_X)


if __name__ == "__main__":
    main()