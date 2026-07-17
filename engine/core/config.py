import os
import datetime
from zoneinfo import ZoneInfo
import json
import random


def select_seed(seeds_choice: list[int], seed: int | None) -> int:
    if seed is None:
        if seeds_choice is None:
            return random.randint(0, 2**32 - 1)
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
    default_dataset_data_csv_path = {
        "test": os.path.join("dataset", "test"),
        "train": os.path.join("dataset", "train"),
    }
    default_dataset_data_folder_path = {
        "test": os.path.join("dataset", "images", "64x64"),
        "train": os.path.join("dataset", "images", "64x64"),
    }
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
                "docs": "Liste des graines pour le choix aléatoire. Si 'seed' et 'seeds_choice' sont None, une graine est choisie aléatoirement dans l'intervalle [0, 2**32 - 1] (uint32).",
                "type": (list, type(None)),
                "default": None,
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
                "type": (dict,),
                "default": default_dataset_data_csv_path,
            },
            "data_folder_path": {
                "docs": "Chemin vers le dossier contenant les images du dataset.",
                "type": (dict,),
                "default": default_dataset_data_folder_path,
            },
            "limit_per_category": {
                "docs": "Limite de données par catégorie (int uniforme, ou dict[str, int] {catégorie: limite}).",
                "type": (dict, int,),
            },
            "normalization_method": {
                "docs": "Méthode de normalisation des données.",
                "type": (str,),
                "options": ["standard", "per_column"],
            },
            "train_positive_ratio": {
                "docs": (
                    "Ratio cible de positifs dans le dataset d'entraînement One-vs-All, par catégorie. "
                    "-1 = pas de rework (ratio naturel, toutes les négatives gardées). "
                    "Sinon valeur dans ]0, 1[ (ex: 0.5 = 50% positifs ; les négatifs sont SOUS-échantillonnés, "
                    "jamais dupliqués, et répartis le plus équitablement possible entre les autres catégories). "
                    "S'applique APRÈS 'limit_per_category'."
                ),
                "type": (float, int),
                "default": -1,
            },
            "categories": {
                "docs": "Dictionnaire des catégories avec leurs chemins de données et CSV. Ex: {'impressionism': {'data_folder_path': 'path/to/impressionism', 'csv_path': 'path/to/impressionism.csv'}, ...}",
                "type": (dict,),
                "default": {
                    "test": {
                        "impressionism": {
                            "data_folder_path": os.path.join(default_dataset_data_folder_path["test"], "impressionism"),
                            "csv_path": os.path.join(default_dataset_data_csv_path["test"], "test.impressionism_clean.csv"),
                        },
                        "realism": {
                            "data_folder_path": os.path.join(default_dataset_data_folder_path["test"], "realism"),
                            "csv_path": os.path.join(default_dataset_data_csv_path["test"], "test.realism_clean.csv"),
                        },
                        "romanticism": {
                            "data_folder_path": os.path.join(default_dataset_data_folder_path["test"], "romanticism"),
                            "csv_path": os.path.join(default_dataset_data_csv_path["test"], "test.romanticism_clean.csv"),
                        },
                    },
                    "train": {
                        "impressionism": {
                            "data_folder_path": os.path.join(default_dataset_data_folder_path["train"], "impressionism"),
                            "csv_path": os.path.join(default_dataset_data_csv_path["train"], "train.impressionism_clean.csv"),
                        },
                        "realism": {
                            "data_folder_path": os.path.join(default_dataset_data_folder_path["train"], "realism"),
                            "csv_path": os.path.join(default_dataset_data_csv_path["train"], "train.realism_clean.csv"),
                        },
                        "romanticism": {
                            "data_folder_path": os.path.join(default_dataset_data_folder_path["train"], "romanticism"),
                            "csv_path": os.path.join(default_dataset_data_csv_path["train"], "train.romanticism_clean.csv"),
                        },
                    },
                },
            },
        },
        "output": {
            "folder": {
                "docs": "Chemin vers le dossier de sortie.",
                "type": (str,),
                "default": os.path.join("engine", "core", "output"),
            },
        },
        "model": {
            "type": {
                "docs": (
                    "Type de modèle à utiliser. 'mlp' = One-vs-All (un MLP à 1 sortie par "
                    "catégorie). 'mlp_multiclass' = un seul MLP partagé, avec une sortie par "
                    "catégorie et décision finale par argmax. 'rbf' = One-vs-All par RBF."
                ),
                "type": (str,),
                "options": ["linear", "mlp", "mlp_multiclass", "rbf"],
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
                "docs": "Nombre de neurones dans les couches **cachées** du MLP. Utiliser seulement si le type de modèle est 'mlp' ou 'mlp_multiclass'.",
                "type": (list, type(None)),
                "default": None,
            },
            "rbf_num_centers": {
                "docs": "Nombre de centres (neurones cachés) du RBF. Utiliser seulement si le type de modèle est 'rbf'.",
                "type": (int, type(None)),
                "default": None,
            },
        },
        "global": {
            "unknown_category": {
                "docs": "Définit la catégorie par défaut pour les données inconnues. Si None, on predit la catégorie la plus probable.",
                "type": (str, type(None)),
                "default": None,
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

            elif section == "dataset" and key == "train_positive_ratio":
                if value != -1 and not (0 < value < 1):
                    raise ValueError(
                        f"init_config(): 'dataset.train_positive_ratio' doit être -1 ou dans ]0, 1[. "
                        f"Obtenu: {value}"
                    )
            
            elif section == "dataset" and key == "limit_per_category":
                if isinstance(value, dict):
                    for cat, limit in value.items():
                        if not isinstance(limit, int):
                            raise TypeError(f"init_config(): Type incorrect pour {section}.{key}[{cat}]. "
                                            f"Attendu: int, Obtenu: {type(limit)}")
    
    # Ajoute les chemins de sortie pour les logs et les modèles
    date, time = get_date_time_now()
    config["output"]["logs"] = os.path.join(config["output"]["folder"], config["model"]["type"], date, time)
    config["output"]["models"] = os.path.join(config["output"]["logs"], "models")
    
    return config


def finalize_mlp_config(config: dict) -> dict:
    """
    Construit (ou vérifie) l'architecture 'npl' du MLP. À appeler APRÈS le chargement
    des images, une fois que 'dataset.W_length' est connu.

    La taille de la couche de sortie dépend du type de modèle :
    - 'mlp'            -> 1 seule sortie (One-vs-All : un modèle par catégorie).
    - 'mlp_multiclass' -> 1 sortie par catégorie (un seul modèle partagé, décision par argmax).
    """
    if config["model"]["type"] not in ("mlp", "mlp_multiclass"):
        return config

    n_categories = len(config["dataset"]["categories"]["train"])
    output_dim = 1 if config["model"]["type"] == "mlp" else n_categories

    if "npl" not in config["model"]:
        config["model"]["npl"] = [config["dataset"]["W_length"], *config["model"]["mlp_hidden_layers"], output_dim]
    else:
        W_length = config["model"]["npl"][0]
        if W_length != config["dataset"]["W_length"]:
            raise ValueError(f"finalize_mlp_config(): W_length incohérent. "
                            f"Obtenu: {W_length}, Attendu: {config['dataset']['W_length']}")

        npl = config["model"]["npl"][1:-1]
        if npl != config["model"]["mlp_hidden_layers"]:
            raise ValueError(f"finalize_mlp_config(): mlp_hidden_layers incohérent. "
                            f"Obtenu: {npl}, Attendu: {config['model']['mlp_hidden_layers']}")

        if config["model"]["npl"][-1] != output_dim:
            raise ValueError(f"finalize_mlp_config(): dernière couche ('npl[-1]') incohérente pour "
                            f"le type '{config['model']['type']}'. Obtenu: {config['model']['npl'][-1]}, "
                            f"Attendu: {output_dim}")

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