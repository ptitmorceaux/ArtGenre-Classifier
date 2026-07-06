# noqa
import sys
import os
import subprocess
import random
import numpy as np
import pandas as pd
from PIL import Image
from math import tanh
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# --- CONFIGURATION GLOBALE ---

CONFIG = {
    "lib": {
        "lib_name": "libc",
        "lib_folder": os.path.join("libc"),
        "build_folder": os.path.join("libc", "build"),
        "specs_folder": os.path.join("libc", "specs"),
        "dependencies_folder": r"C:\msys64\mingw64\bin",
        "seeds_choice": [42, 1337, 2024, 1234, 5678],
        "seed": None,
    },
    "dataset": {
        "csv_path": os.path.join("..", "dataset"),
        "data_folder_path": os.path.join("..", "dataset", "64x64"),
        "limit_per_category": 1000,
        "train_test_split_ratio": 0.7,
    },
    "model": {
        "alpha": 0.01,
        "epochs": 1000,
    },
    "global": {
        "unknown_category": "unknown",
    }
}

# Définition des catégories globales
CATEGORIES = {
    "impressionism": {
        "data_folder_path": os.path.join(CONFIG["dataset"]["data_folder_path"], "impressionism"),
        "csv_path": os.path.join(CONFIG["dataset"]["csv_path"], "impressionism_clean.csv")
    },
    "realism": {
        "data_folder_path": os.path.join(CONFIG["dataset"]["data_folder_path"], "realism"),
        "csv_path": os.path.join(CONFIG["dataset"]["csv_path"], "realism_clean.csv")
    },
    "romanticism": {
        "data_folder_path": os.path.join(CONFIG["dataset"]["data_folder_path"], "romanticism"),
        "csv_path": os.path.join(CONFIG["dataset"]["csv_path"], "romanticism_clean.csv")
    }
}

def compile_c_library():
    """Compile la bibliothèque C à l'aide de make."""
    print("Compilation de la bibliothèque C...")

    try:
        result = subprocess.run(
            f"make -C {CONFIG['lib']['lib_folder']} clean && make -C {CONFIG['lib']['lib_folder']}",
            shell=True,
            capture_output=True,
            text=True
        )
        # print(result.stdout)

        if result.stderr:
            print(result.stderr)
        
        if result.returncode != 0:
            print(f"Build failed with exit code {result.returncode}")
            sys.exit(1)
        else:
            print("Build succeeded.")

    except Exception as e:
        raise ValueError(f"Build failed: {e}")


def load_c_library():
    """Charge le Singleton Loader pour l'interopérabilité avec la bibliothèque C."""
    from engine.interop.loader import Loader
    try:
        Loader.loadLibrary(
            lib_name=CONFIG["lib"]["lib_name"],
            lib_folder=CONFIG["lib"]["lib_folder"],
            build_folder=CONFIG["lib"]["build_folder"],
            specs_folder=CONFIG["lib"]["specs_folder"],
            dependencies_bin_folder=CONFIG["lib"]["dependencies_folder"],
            seed=CONFIG["lib"]["seed"]
        )

        print("Bibliothèque C chargée avec succès !")
    except Exception as e:
        if "already loaded" in str(e):
            print("✓ Bibliothèque C déjà chargée.")
        else:
            raise Exception(f"Erreur lors du chargement de la bibliothèque C : {e}")


def load_and_prepare_csv():
    """Charge les fichiers CSV des catégories et effectue le découpage Train/Test."""
    
    df_csv_categories = dict()
    df_csv_all_shuffled = {
        "train": pd.DataFrame(),
        "test": pd.DataFrame()
    }
    
    CONFIG["dataset"]["count_total_dataset"] = dict()
    CONFIG["dataset"]["count_total_dataset"]["total"] = 0

    for category, paths in CATEGORIES.items():
        df = pd.read_csv(paths["csv_path"])

        if df.empty:
            raise ValueError(f"Le fichier CSV pour la catégorie '{category}' est vide ou introuvable.")
        
        if CONFIG["dataset"]["limit_per_category"] > 0:
            df = df.head(CONFIG["dataset"]["limit_per_category"])
        
        CONFIG["dataset"]["count_total_dataset"][category] = len(df)
        CONFIG["dataset"]["count_total_dataset"]["total"] += CONFIG["dataset"]["count_total_dataset"][category]

        if "Nom_Fichier" not in df.columns:
            raise ValueError("La colonne 'Nom_Fichier' n'existe pas dans le DataFrame.")
        
        # Transformation du nom en chemin complet
        df["filepath"] = df["Nom_Fichier"].apply(lambda x: os.path.join(paths["data_folder_path"], x))

        # Ajouter une colonne category (Y) avec Encodage One-vs-All (1 ou -1)
        for c in CATEGORIES:
            if c in df.columns:
                raise ValueError(f"La colonne '{c}' existe déjà dans le DataFrame. Veuillez renommer ou supprimer cette colonne.")
            df[c] = 1 if c == category else -1
        
        # Split train / test
        df_train = df.sample(frac=CONFIG["dataset"]["train_test_split_ratio"], random_state=CONFIG["lib"]["seed"])
        df_test = df.drop(df_train.index)
        
        # On stocke les DataFrames train et test pour chaque catégorie
        df_csv_categories[category] = {"train": df_train, "test": df_test}

        # On concatène les DataFrames train et pour toutes les catégories
        if df_csv_all_shuffled["train"].empty:
            df_csv_all_shuffled["train"] = df_train
            df_csv_all_shuffled["test"] = df_test
        else:
            df_csv_all_shuffled["train"] = pd.concat([df_csv_all_shuffled["train"], df_train], ignore_index=True)
            df_csv_all_shuffled["test"] = pd.concat([df_csv_all_shuffled["test"], df_test], ignore_index=True)

    # Mélange final des jeux de données complets
    df_csv_all_shuffled["train"] = df_csv_all_shuffled["train"].sample(frac=1, random_state=CONFIG["lib"]["seed"]).reset_index(drop=True)
    df_csv_all_shuffled["test"] = df_csv_all_shuffled["test"].sample(frac=1, random_state=CONFIG["lib"]["seed"]).reset_index(drop=True)

    # Extraction des labels (Y) et nettoyage des DataFrames
    df_X_filepaths = {
        "train": df_csv_all_shuffled["train"]["filepath"].tolist(),
        "test": df_csv_all_shuffled["test"]["filepath"].tolist()
    }

    df_Y = {"train": {}, "test": {}}
    for category in CATEGORIES:
        df_Y["train"][category] = list(df_csv_all_shuffled["train"][category])
        df_Y["test"][category] = list(df_csv_all_shuffled["test"][category])
        df_csv_all_shuffled["train"].drop(columns=[category], inplace=True)
        df_csv_all_shuffled["test"].drop(columns=[category], inplace=True)

    return df_X_filepaths, df_Y


def load_images_from_filepaths(df_X_filepaths):
    """Charge et aplatit les images réelles en utilisant Pillow."""
    df_X = dict()
    
    for step in df_X_filepaths:
        
        df_X[step] = list()
        filepaths = df_X_filepaths[step]
        total = len(filepaths)

        for i, filepath in enumerate(filepaths):
            if i % 50 == 0 or i == total - 1:
                print(f"\rChargement {step}... {i+1}/{total} ({100*(i+1)/total:.1f}%)", end="", flush=True)

            img = Image.open(filepath).convert("RGB")
            img_array = (np.array(img).flatten()).astype(np.float32)

            if "W_length" not in CONFIG["dataset"]:
                CONFIG["dataset"]["W_length"] = len(img_array)
            elif len(img_array) != CONFIG["dataset"]["W_length"]:
                raise ValueError(f"Image at {filepath} has a different size ({len(img_array)}) than expected ({CONFIG['dataset']['W_length']}).")

            df_X[step].append(img_array)
        print()

    df_X["train"] = np.concatenate(df_X["train"])
    return df_X


def standardize_data(df_X) -> tuple[dict, float, float]:
    """Applique une standardisation standard (X - moyenne) / ecart_type."""
    X_train_mean = np.mean(df_X["train"])
    X_train_std = np.std(df_X["train"])

    # Protection contre la division par zéro si un pixel est constant
    if np.any(X_train_std == 0):
        print("Warning: Some features have zero standard deviation. They will not be standardized.")
        X_train_std = 1

    df_X["train"] = ((df_X["train"] - X_train_mean) / X_train_std).astype(np.float32).tolist()

    for i, X_test in enumerate(df_X["test"]):
        df_X["test"][i] = ((np.array(X_test) - X_train_mean) / X_train_std).astype(np.float32).tolist()
        
    return df_X, X_train_mean, X_train_std


def train_models(df_X, df_Y):
    """Entraîne un modèle linéaire par catégorie (One-vs-All)."""
    from engine.interop.linearModel import LinearModel
    models_per_category = dict()

    for category in CATEGORIES:
        print(f"Training model for category: {category}")
        models_per_category[category] = LinearModel.init_random(input_dim=CONFIG["dataset"]["W_length"])
        models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            is_classification=True,
            alpha=CONFIG["model"]["alpha"],
            epochs=CONFIG["model"]["epochs"]
        )
        print(f"Model for category '{category}' trained successfully.\n")
        
    return models_per_category


def evaluate_models(models_per_category, df_X, df_Y):
    """Évalue les modèles et génère les prédictions finales par rapport aux attentes."""
    predictions = dict()

    for category in CATEGORIES:
        print(f"Evaluating model for category: {category}")
        
        predictions[category] = dict()
        predictions[category]["values"] = [
            models_per_category[category].predict(x, is_classification=False) for x in df_X["test"]
        ]
        predictions[category]["prediction"] = [tanh(value) >= 0 for value in predictions[category]["values"]]

    # Détermination de la catégorie prédite (Argmax de la valeur de sortie ou "unknown")
    df_predictions_test = list()
    first_cat = list(CATEGORIES.keys())[0]
    
    for i in range(len(predictions[first_cat]["prediction"])):
        category_predicted = max(CATEGORIES.keys(), key=lambda c: predictions[c]["values"][i])

        if predictions[category_predicted]["prediction"][i]:
            df_predictions_test.append(category_predicted)
        else:
            df_predictions_test.append(CONFIG["global"]["unknown_category"])

    # Détermination de la catégorie attendue
    df_predictions_expected = []
    for i in range(len(df_Y["test"][first_cat])):
        category_expected = next((c for c in CATEGORIES if df_Y["test"][c][i] == 1), None)
        df_predictions_expected.append(category_expected)

    return df_predictions_expected, df_predictions_test


def plot_confusion_matrix(df_predictions_expected, df_predictions_test, df_X):
    """Génère et affiche la matrice de confusion."""
    ConfusionMatrixDisplay.from_predictions(
        df_predictions_expected,
        df_predictions_test,
        labels=list(CATEGORIES.keys()) + [CONFIG["global"]["unknown_category"]],
        cmap="Blues",
        xticks_rotation=45
    )

    length_X_test = len(df_X["test"])
    length_X_train = CONFIG["dataset"]["count_total_dataset"]["total"] - length_X_test

    plt.title("Matrix de Confusion")
    plt.suptitle(
        f"Seed: {CONFIG['lib']['seed']} | "
        f"Model: Classification Linéaire | "
        f"Alpha: {CONFIG['model']['alpha']} | "
        f"Epochs: {CONFIG['model']['epochs']}\n\n"
        f"Dataset: {length_X_train} train, {length_X_test} test "
        f"(total = {CONFIG['dataset']['count_total_dataset']['total']}, "
        f"{CONFIG['dataset']['train_test_split_ratio'] * 100}% ratio)",
        fontsize=10,
        y=1.02
    )

    plt.tight_layout()
    plt.show()


def main():
    # Gestion de l'aléa
    if CONFIG["lib"]["seeds_choice"] is not None:
        CONFIG["lib"]["seed"] = random.choice(CONFIG["lib"]["seeds_choice"])
    print(f"Seed sélectionné : {CONFIG['lib']['seed']}")

    # 1. Compilation et chargement de l'interopérabilité
    compile_c_library()
    load_c_library()

    # 2. Préparation des données
    df_X_filepaths, df_Y = load_and_prepare_csv()
    df_X = load_images_from_filepaths(df_X_filepaths)
    df_X, X_train_mean, X_train_std = standardize_data(df_X)

    # 3. Entraînement
    models_per_category = train_models(df_X, df_Y)

    # 4. Évaluation et Visualisation
    df_predictions_expected, df_predictions_test = evaluate_models(models_per_category, df_X, df_Y)
    plot_confusion_matrix(df_predictions_expected, df_predictions_test, df_X)


if __name__ == "__main__":
    main()
