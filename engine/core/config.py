import os
# import json


CONFIG = {
    "lib": {
        "compile": True,
        "lib_name": "libc",
        "lib_folder": os.path.join("libc"),
        "build_folder": os.path.join("libc", "build"),
        "specs_folder": os.path.join("libc", "specs"),
        "dependencies_folder": r"C:\msys64\mingw64\bin",
        "seeds_choice": [42, 1337, 2024, 1234, 5678],
        "seed": None, # Si None, une seed aléatoire sera choisie parmi seeds_choice
    },
    "dataset": {
        "csv_path": os.path.join("dataset"),
        "data_folder_path": os.path.join("dataset", "64x64"),
        "limit_per_category": 1000,
        "train_test_split_ratio": 0.7,
        # "standard"     -> une seule moyenne/écart-type sur tous les pixels
        # "per_column" -> une moyenne/écart-type par canal (r, g, b)
        "normalization_method": "per_column",
    },
    "output": {
        "outdir": os.path.join("engine", "core", "output"),
        "logs": os.path.join("engine", "core", "output", "logs"),
        "models": os.path.join("engine", "core", "output", "trained_models"),
        "metrics": os.path.join("engine", "core", "output", "metrics"),
    },
    "model": {
        # "linear" -> LinearModel (One-vs-All)
        # "mlp"    -> MLP (One-vs-All)
        "type": "linear",
        "alpha": 0.001,
        "epochs": 50,
        # Utilisé seulement si type == "mlp" : couches cachées, sans compter
        # l'entrée (W_length, déduite du dataset) ni la sortie (toujours 1, one-vs-all)
        # couche d'entrée et couche de sortie deja définies par le dataset et le type de modèle
        "mlp_hidden_layers": [64, 32],
    },
    "global": {
        # Si vide ou None, on force la meilleure catégorie parmi celles connues. Sinon, on renvoie "unknown" si aucune catégorie n'est prédite.
        # Exemple : "unknown" / "autre" ou encore None / "" (vide) pour forcer la meilleure catégorie connue.
        "unknown_category": None,
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


# def load_config_from_json(filepath: str = "conf/config.json"):
#     """
#     Charge la configuration depuis un fichier JSON.
#     """
#     # TODO: A finir
#     config_path = os.path.join(filepath)
#     if not os.path.exists(config_path):
#         raise FileNotFoundError(f"Le fichier de configuration '{config_path}' est introuvable.")
#     with open(config_path, "r") as f:
#         loaded_config = json.load(f)
#         CONFIG.update(loaded_config)

# def load_categories_from_json(filepath: str = "conf/categories.json"):
#     """
#     Charge les catégories depuis un fichier JSON.
#     """
#     # TODO: A finir
#     categories_path = os.path.join(filepath)
#     if not os.path.exists(categories_path):
#         raise FileNotFoundError(f"Le fichier de catégories '{categories_path}' est introuvable.")
#     with open(categories_path, "r") as f:
#         CATEGORIES = json.load(f)
    
