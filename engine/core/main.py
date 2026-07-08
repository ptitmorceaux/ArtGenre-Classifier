# ruff: noqa
import os
import sys
import random
import json
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from engine.core.config import CONFIG
from engine.core.build import compile_c_library, load_c_library
from engine.core.dataset import load_and_prepare_csv, load_images_from_filepaths
from engine.core.preprocessing import standardize_data
from engine.core.training import train_models
from engine.core.persistence import save_trained_models
from engine.core.evaluation import evaluate_models, plot_confusion_matrix

def select_seed():
    if CONFIG["lib"]["seed"] is None:
        if CONFIG["lib"]["seeds_choice"] is None:
            raise ValueError("CONFIG['lib']['seeds_choice'] doit être défini si CONFIG['lib']['seed'] est None.")
        CONFIG["lib"]["seed"] = random.choice(CONFIG["lib"]["seeds_choice"])
    if not isinstance(CONFIG["lib"]["seed"], int):
        raise ValueError("CONFIG['lib']['seed'] doit être un entier ou None.")


def main():
    # 0. Gestion de l'aléa et de la Session
    select_seed()
    session_id = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M")
    
    print(f"Seed sélectionnée : {CONFIG['lib']['seed']}")
    print(f"ID de Session d'entraînement : {session_id}")

    # 1. Compilation et chargement de l'interopérabilité
    print("\n# Etape 1 : Compilation et chargement de l'interopérabilité...")
    compile_c_library()
    load_c_library()

    # 2. Préparation des données
    print("\n# Etape 2 : Préparation des données...")
    df_X_filepaths, df_Y = load_and_prepare_csv()
    df_X = load_images_from_filepaths(df_X_filepaths)
    df_X, scaler = standardize_data(df_X)

    # 3. Entraînement (Retourne maintenant aussi le nom du fichier de la courbe de loss)
    print("\n# Etape 3 : Entraînement des modèles...")
    models_per_category, loss_filename = train_models(df_X, df_Y, session_id)

    # 4. Sauvegarde des modèles
    print("\n# Etape 4 : Sauvegarde des modèles (fichiers .bin)...")
    save_trained_models(models_per_category, scaler, CONFIG["output"]["models"], session_id)

    # 5. Évaluation et Visualisation (Retourne l'accuracy et le nom de la matrice)
    print("\n# Etape 5 : Évaluation et Visualisation...")
    df_predictions_expected, df_predictions_test, global_accuracy = evaluate_models(models_per_category, df_X, df_Y)
    cm_filename = plot_confusion_matrix(df_predictions_expected, df_predictions_test, df_X, session_id)

    # 6. Sauvegarde des métadonnées (Pour le MLOps / Django)
    print("\n# Etape 6 : Génération du fichier de session (metadata.json)...")
    metadata = {
        "session_id": session_id,
        "model_type": CONFIG["model"]["type"],
        "hyperparameters": { 
            "epochs": CONFIG["model"]["epochs"],
            "alpha": CONFIG["model"]["alpha"]
        },
        "metrics": {
            "accuracy": round(global_accuracy, 4)
        },
        "artifacts": {
            "confusion_matrix": cm_filename,
            "loss_curve": loss_filename,
            "accuracy_curve": acc_filename
        }
    }
    
    # Création du dossier metrics s'il n'existe pas
    metrics_dir = os.path.join(CONFIG["output"]["outdir"], "metrics", session_id)
    meta_path = os.path.join(metrics_dir, "metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)
        
    print(f"[*] Session sauvegardée avec succès !\n -> {meta_path}")

if __name__ == "__main__":
    main()