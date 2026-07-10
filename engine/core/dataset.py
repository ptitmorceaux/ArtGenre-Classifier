import os
import numpy as np
import pandas as pd
from PIL import Image

import engine.core.config as cf


def load_and_prepare_csv() -> tuple[dict, dict]:
    """Charge les fichiers CSV des catégories et effectue le découpage Train/Test."""

    df_csv_categories = dict()
    df_csv_all_shuffled = dict()

    cf.CONFIG["dataset"]["count_total_dataset"] = {
        "test": { "total": 0 },
        "train": { "total": 0 }
    }

    for step, categories in cf.CONFIG["dataset"]["categories"].items():
        for category, paths in categories.items():
            df = pd.read_csv(paths["csv_path"])

            if df.empty:
                raise ValueError(f"Le fichier CSV pour la catégorie '{category}' est vide ou introuvable.")

            if step == "train":
                if cf.CONFIG["dataset"]["limit_per_category"] > 0:
                    df = df.head(cf.CONFIG["dataset"]["limit_per_category"])

            cf.CONFIG["dataset"]["count_total_dataset"][step][category] = len(df)
            cf.CONFIG["dataset"]["count_total_dataset"][step]["total"] += cf.CONFIG["dataset"]["count_total_dataset"][step][category]

            if "Nom_Fichier" not in df.columns:
                raise ValueError("La colonne 'Nom_Fichier' n'existe pas dans le DataFrame.")

            # Transformation du nom en chemin complet
            df["filepath"] = df["Nom_Fichier"].apply(lambda x: os.path.join(paths["data_folder_path"], x))

            # Ajouter une colonne category (Y) avec Encodage One-vs-All (1 ou -1)
            for c in cf.CONFIG["dataset"]["categories"]["train"].keys():
                if c in df.columns:
                    raise ValueError(f"La colonne '{c}' existe déjà dans le DataFrame. Veuillez renommer ou supprimer cette colonne.")
                df[c] = 1 if c == category else -1

            # On stocke les DataFrames train et test pour chaque catégorie
            if step not in df_csv_categories:
                df_csv_categories[step] = dict()
            df_csv_categories[step][category] = df
    
        # On concatène les DataFrames train et test pour toutes les catégories
        df_csv_all_shuffled[step] = pd.concat([df for df in df_csv_categories[step].values()], ignore_index=True)

    # Mélange final du jeu de données uniquement pour le TRAIN
    df_csv_all_shuffled["train"] = df_csv_all_shuffled["train"].sample(frac=1, random_state=cf.CONFIG["lib"]["seed"]).reset_index(drop=True)

    # Extraction des labels (Y) et nettoyage des DataFrames
    df_X_filepaths = {
        "train": df_csv_all_shuffled["train"]["filepath"].tolist(),
        "test": df_csv_all_shuffled["test"]["filepath"].tolist()
    }

    df_Y = {"train": {}, "test": {}}
    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        df_Y["train"][category] = list(df_csv_all_shuffled["train"][category])
        df_Y["test"][category] = list(df_csv_all_shuffled["test"][category])
        df_csv_all_shuffled["train"].drop(columns=[category], inplace=True)
        df_csv_all_shuffled["test"].drop(columns=[category], inplace=True)

    return df_X_filepaths, df_Y


def load_images_from_filepaths(df_X_filepaths: dict) -> dict:
    """Charge et aplatit les images réelles en utilisant Pillow."""
    df_X = dict()

    for step in df_X_filepaths:

        df_X[step] = list()
        filepaths = df_X_filepaths[step]
        total = len(filepaths)

        for i, filepath in enumerate(filepaths):
            if i % 50 == 0 or i == total - 1:
                print(f"\rChargement {step}... {i+1}/{total} ({100*(i+1)/total:.2f}%)", end="", flush=True)

            img = Image.open(filepath).convert("RGB")
            img_array = (np.array(img).flatten()).astype(np.float32)

            if "W_length" not in cf.CONFIG["dataset"]:
                cf.CONFIG["dataset"]["W_length"] = len(img_array)
            elif len(img_array) != cf.CONFIG["dataset"]["W_length"]:
                raise ValueError(f"Image at {filepath} has a different size ({len(img_array)}) than expected ({cf.CONFIG['dataset']['W_length']}).")

            df_X[step].append(img_array)
        print()

    # Le train est concaténé en un seul vecteur 1D (row-major) pour nourrir directement
    # LinearModel.train(). Le test reste une liste d'images séparées, car on prédit
    # image par image dans evaluate_models().
    df_X["train"] = np.concatenate(df_X["train"])
    return df_X