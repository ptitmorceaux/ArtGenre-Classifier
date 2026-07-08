import os
import datetime
from zoneinfo import ZoneInfo
import json
import random


def select_seed(seeds_choice: list[int], seed: int | None) -> int:
    if seed is None:
        if seeds_choice is None:
            raise ValueError("select_seed(): 'seeds_choice' doit être défini si 'seed' est None.")
        seed = random.choice(seeds_choice)
    if not isinstance(seed, int):
        raise ValueError("select_seed(): 'seed' doit être un entier ou None.")
    return seed


def get_date_time_now() -> list[str, str]:
    """
    Renvoie "yyyy-mm-dd" et "hh-mm-ss_ms" : pour différencier les runs dans le dossier de sortie
    """
    return datetime.datetime.now(ZoneInfo("Europe/Paris")).strftime("%Y-%m-%d/%H-%M-%S_%f").split("/")


def get_config_documentation() -> dict:
    """
    Renvoie la documentation de la configuration sous forme de dictionnaire.
    Chaque section contient des clés avec leurs types, valeurs par défaut et options possibles.
    """
    default_dataset_data_folder_path = os.path.join("dataset", "64x64")
    default_dataset_data_csv_path = os.path.join("dataset")

    date = get_date_time_now()
    default_output_folder = os.path.join("engine", "core", "output")
    default_output_logs = os.path.join(default_output_folder, date[0], date[1])
    return {
        "lib": {
            "compile": {
                "docs": "Si True, compile la bibliothèque C. Si False, charge la bibliothèque C précompilée.",
                "type": (bool,),
                "default": True,
            },
            "lib_name": {
                "docs": "Nom de la bibliothèque C (sans l'extension).",
                "type": (str,),
                "default": "libc",
            },
            "lib_folder": {
                "docs": "Chemin vers le dossier contenant la bibliothèque C.",
                "type": (str,),
                "default": os.path.join("libc"),
            },
            "build_folder": {
                "docs": "Chemin vers le dossier de construction.",
                "type": (str,),
                "default": os.path.join("libc", "build"),
            },
            "specs_folder": {
                "docs": "Chemin vers le dossier contenant les spécifications.",
                "type": (str,),
                "default": os.path.join("libc", "specs"),
            },
            "dependencies_folder": {
                "docs": "Chemin vers le dossier contenant les dépendances.",
                "type": (str,),
                "default": r"C:\msys64\mingw64\bin",
            },
            "seeds_choice": {
                "docs": "Liste des graines pour le choix aléatoire.",
                "type": (list,),
                "default": [42, 1337, 2024, 1234, 5678],
            },
            "seed": {
                "docs": "Graine pour l'initialisation aléatoire. Si None, une graine est choisie aléatoirement parmi seeds_choice.",
                "type": (int, type(None)),
                "default": None,
            },
        },
        "dataset": {
            "csv_path": {
                "docs": "Chemin vers le fichier CSV du dataset.",
                "type": (str,),
                "default": default_dataset_data_csv_path,
            },
            "data_folder_path": {
                "docs": "Chemin vers le dossier contenant les images du dataset.",
                "type": (str,),
                "default": default_dataset_data_folder_path,
            },
            "limit_per_category": {
                "docs": "Limite de données par catégorie.",
                "type": (int,),
            },
            "train_test_split_ratio": {
                "docs": "Ratio de séparation entre les ensembles d'entraînement et de test.",
                "type": (float,),
            },
            "normalization_method": {
                "docs": "Méthode de normalisation des données.",
                "type": (str,),
                "options": ["standard", "per_column"],
            },
            "categories": {
                "docs": "Dictionnaire des catégories avec leurs chemins de données et CSV. Ex: {'impressionism': {'data_folder_path': 'path/to/impressionism', 'csv_path': 'path/to/impressionism.csv'}, ...}",
                "type": (dict,),
                "default": {
                    "impressionism": {
                        "data_folder_path": os.path.join(default_dataset_data_folder_path, "impressionism"),
                        "csv_path": os.path.join(default_dataset_data_csv_path, "impressionism_clean.csv")
                    },
                    "realism": {
                        "data_folder_path": os.path.join(default_dataset_data_folder_path, "realism"),
                        "csv_path": os.path.join(default_dataset_data_csv_path, "realism_clean.csv")
                    },
                    "romanticism": {
                        "data_folder_path": os.path.join(default_dataset_data_folder_path, "romanticism"),
                        "csv_path": os.path.join(default_dataset_data_csv_path, "romanticism_clean.csv")
                    },
                },
            },
        },
        "output": {
            "folder": {
                "docs": "Chemin vers le dossier de sortie.",
                "type": (str,),
                "default": default_output_folder,
            },
            "logs": {
                "docs": "Chemin vers le dossier de logs.",
                "type": (str,),
                "default": default_output_logs,
            },
            "models": {
                "docs": "Chemin vers le dossier des modèles entraînés.",
                "type": (str,),
                "default": os.path.join(default_output_logs, "models"),
            },
        },
        "model": {
            "type": {
                "docs": "Type de modèle à utiliser.",
                "type": (str,),
                "options": ["linear", "mlp"],
            },
            "alpha": {
                "docs": "Paramètre de régularisation pour le modèle linéaire.",
                "type": (float,),
            },
            "epochs": {
                "docs": "Nombre d'itérations pour l'entraînement.",
                "type": (int,),
            },
            "mlp_hidden_layers": {
                "docs": "Nombre de neurones dans les couches **cachées** du MLP. Utiliser seulement si le type de modèle est 'mlp'.",
                "type": (list,),
            },
        },
        "global": {
            "unknown_category": {
                "docs": "Définit la catégorie par défaut pour les données inconnues. Si None, on predit la catégorie la plus probable.",
                "type": (str, type(None)),
            },
        },
    }


def init_config(config: dict) -> dict:
    """
    Initialise la configuration en vérifiant les types et les valeurs par défaut.
    """
    docs = get_config_documentation()
    for section, section_docs in docs.items():

        required_section = any("default" not in key_docs for key_docs in section_docs.values())
        
        if required_section and section not in config:
            raise KeyError(f"init_config(): Section manquante dans la configuration : {section}")
        elif section not in config:
            config[section] = {}
        
        for key, key_docs in section_docs.items():
            if key not in config[section]:
                if "default" in key_docs:
                    config[section][key] = key_docs["default"]
                else:
                    raise KeyError(f"init_config(): Clé manquante dans la configuration : {section}.{key}")
        
            value = config[section][key]
            expected_types = key_docs["type"]
        
            if not isinstance(value, expected_types):
                raise TypeError(f"init_config(): Type incorrect pour {section}.{key}. "
                                f"Attendu: {expected_types}, Obtenu: {type(value)}")
        
            if "options" in key_docs and value not in key_docs["options"]:
                raise ValueError(f"init_config(): Valeur incorrecte pour {section}.{key}. "
                                 f"Attendu: {key_docs['options']}, Obtenu: {value}")

            if section == "lib" and key == "seed":
                config[section][key] = select_seed(config[section]["seeds_choice"], value)
    return config


def load_config_from_json(filepath: str) -> dict:
    """
    Charge la configuration depuis un fichier JSON.
    """
    config_path = os.path.join(filepath)
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Le fichier de configuration '{config_path}' est introuvable.")

    with open(config_path, "r") as f:
        loaded_config = json.load(f)
    
    return init_config(loaded_config)


# On appel CONFIG dans tous les fichiers / On initialise CONFIG dans main.py avec load_config_from_json() avant de l'utiliser.
CONFIG = None
