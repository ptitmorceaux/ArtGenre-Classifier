import os

CONFIG = {
    "lib": {
        "compile": True,
        "lib_name": "libc",
        "lib_folder": os.path.join("libc"),
        "build_folder": os.path.join("libc", "build"),
        "specs_folder": os.path.join("libc", "specs"),
        "dependencies_folder": r"C:\msys64\mingw64\bin",
        "seeds_choice": [42, 1337, 2024, 1234, 5678],
        "seed": None,
    },
    "dataset": {
        "csv_path": os.path.join("dataset"),
        "data_folder_path": os.path.join("dataset", "64x64"),
        "limit_per_category": 500,
        "train_test_split_ratio": 0.7,
        # "global"     -> une seule moyenne/écart-type sur tous les pixels
        # "per_column" -> une moyenne/écart-type par canal (r, g, b)
        "normalization_method": "per_column",
    },
    "output": {
        "models_folder": os.path.join("trained_models"),
    },
    "model": {
        # "linear" -> LinearModel (One-vs-All)
        # "mlp"    -> MLP (One-vs-All)
        "type": "linear",
        "alpha": 0.01,
        "epochs": 300,
        # Utilisé seulement si type == "mlp" : couches cachées, sans compter
        # l'entrée (W_length, déduite du dataset) ni la sortie (toujours 1, one-vs-all)
        # couche d'entrée et couche de sortie deja définies par le dataset et le type de modèle
        "mlp_hidden_layers": [64, 32],
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