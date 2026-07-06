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
from engine.core.persistence import save_trained_models
from engine.core.evaluation import evaluate_models, plot_confusion_matrix


def main():
    # Gestion de l'aléa
    if CONFIG["lib"]["seed"] is None:
        if CONFIG["lib"]["seeds_choice"] is None:
            raise ValueError("CONFIG['lib']['seeds_choice'] doit être défini si CONFIG['lib']['seed'] est None.")
        CONFIG["lib"]["seed"] = random.choice(CONFIG["lib"]["seeds_choice"])
    if not isinstance(CONFIG["lib"]["seed"], int):
        raise ValueError("CONFIG['lib']['seed'] doit être un entier ou None.")
    print(f"Seed sélectionnée : {CONFIG['lib']['seed']}")

    # 1. Compilation et chargement de l'interopérabilité
    print("\nEtape 1 : Compilation et chargement de l'interopérabilité...")
    compile_c_library()
    load_c_library()

    # 2. Préparation des données
    print("\nEtape 2 : Préparation des données...")
    df_X_filepaths, df_Y = load_and_prepare_csv()
    df_X = load_images_from_filepaths(df_X_filepaths)
    df_X, scaler = standardize_data(df_X)

    # 3. Entraînement
    print("\nEtape 3 : Entraînement des modèles...")
    models_per_category = train_models(df_X, df_Y)

    # 4. Sauvegarde des modèles entraînés + du scaler utilisé (un fichier par catégorie).
    #    Les modèles restent en mémoire ensuite pour l'évaluation ci-dessous.
    print("\nEtape 4 : Sauvegarde des modèles entraînés...")
    save_trained_models(models_per_category, scaler, CONFIG["output"]["models_folder"])

    # 5. Évaluation et Visualisation
    print("\nEtape 5 : Évaluation et Visualisation...")
    df_predictions_expected, df_predictions_test = evaluate_models(models_per_category, df_X, df_Y)
    plot_confusion_matrix(df_predictions_expected, df_predictions_test, df_X)


if __name__ == "__main__":
    main()