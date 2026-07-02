import os
import sys
import datetime
import subprocess
import random
from math import tanh
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# ══════════════════════════════════════════════════════════════════════════════
#  1. CONFIGURATION DYNAMIQUE DES CHEMINS
# ══════════════════════════════════════════════════════════════════════════════

# Détection automatique de la racine du projet (s'adapte si exécuté depuis engine/core/ ou notebooks/)
if os.path.exists("libc"):
    BASE_DIR = "."
elif os.path.exists("../libc"):
    BASE_DIR = ".."
elif os.path.exists("../../libc"):
    BASE_DIR = "../.."
else:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Ajout de la racine au sys.path pour permettre les imports 'engine.*'
if os.path.abspath(BASE_DIR) not in sys.path:
    sys.path.append(os.path.abspath(BASE_DIR))

# Configuration globale unifiée (fusionnée pour éviter les écrasements du notebook)
config = {
    "lib": {
        "lib_name": "libc",
        "lib_folder": os.path.join(BASE_DIR, "libc"),
        "build_folder": os.path.join(BASE_DIR, "libc", "build"),
        "specs_folder": os.path.join(BASE_DIR, "libc", "specs"),
        "dependencies_folder": None,  # Géré globalement sous Linux/WSL via build-essential
        "seeds_choice": [42, 1337, 2024, 1234, 5678],
        "seed": None,
    },
    "dataset": {
        "csv_path": os.path.join(BASE_DIR, "dataset"),
        "data_folder_path": os.path.join(BASE_DIR, "dataset", "64x64"),
        "limit_per_category": 1000,
        "train_test_split_ratio": 0.7,  # 70% train, 30% test
    },
    "model": {
        "alpha": 0.001,  # Taux d'apprentissage ajusté à 0.001 selon la cellule de classification
        "epochs": 1000,
    },
    "global": {
        "unknown_category": "unknown",  # Catégorie par défaut si aucun modèle ne valide l'œuvre
    }
}

# Sélection d'une graine aléatoire si configurée
if config["lib"]["seeds_choice"] is not None:
    config["lib"]["seed"] = random.choice(config["lib"]["seeds_choice"])

# ══════════════════════════════════════════════════════════════════════════════
#  2. COMPILATION AUTOMATIQUE DE LA LIBRAIRIE C
# ══════════════════════════════════════════════════════════════════════════════

lib_folder = config["lib"]["lib_folder"]
make_command = f"make -C {lib_folder} clean && make -C {lib_folder}"

print(f"[*] Compilation de la bibliothèque C dans : {lib_folder}...")
try:
    result = subprocess.run(make_command, shell=True, capture_output=True, text=True)
    if result.stderr and result.returncode != 0:
        print("[ERREUR MAKEFILE] :\n", result.stderr)
    
    if result.returncode != 0:
        print(f"Le build a échoué avec le code : {result.returncode}")
        sys.exit(1)
    else:
        print("[+] Compilation réussie (binaire et spécifications JSON créés).")
except Exception as e:
    print(f"Échec du lancement du processus de build : {e}")
    sys.exit(1)

# ══════════════════════════════════════════════════════════════════════════════
#  3. CHARGEMENT DU LOADER (INTEROPÉRABILITÉ PYTHON/C)
# ══════════════════════════════════════════════════════════════════════════════

from engine.interop.loader import Loader
from engine.interop.linearModel import LinearModel

try:
    Loader.loadLibrary(
        lib_name=config["lib"]["lib_name"],
        lib_folder=config["lib"]["lib_folder"],
        build_folder=config["lib"]["build_folder"],
        specs_folder=config["lib"]["specs_folder"],
        dependencies_bin_folder=config["lib"]["dependencies_folder"],
        seed=config["lib"]["seed"]
    )
    print("✓ Bibliothèque C chargée en mémoire avec succès !")
except Exception as e:
    if "already loaded" in str(e):
        print("✓ Bibliothèque C déjà chargée.")
    else:
        raise RuntimeError(f"Erreur lors du chargement de la bibliothèque C : {e}")

# ══════════════════════════════════════════════════════════════════════════════
#  4. PRÉPARATION ET REGROUPEMENT DU DATASET (CSV)
# ══════════════════════════════════════════════════════════════════════════════

categories = {
    "impressionism": {
        "data_folder_path": os.path.join(config["dataset"]["data_folder_path"], "impressionism"),
        "csv_path": os.path.join(config["dataset"]["csv_path"], "impressionism_clean.csv")
    },
    "realism": {
        "data_folder_path": os.path.join(config["dataset"]["data_folder_path"], "realism"),
        "csv_path": os.path.join(config["dataset"]["csv_path"], "realism_clean.csv")
    },
    "romanticism": {
        "data_folder_path": os.path.join(config["dataset"]["data_folder_path"], "romanticism"),
        "csv_path": os.path.join(config["dataset"]["csv_path"], "romanticism_clean.csv")
    }
}

print("\n[*] Traitement et split du dataset...")
df_csv_categories = dict()
df_csv_all_shuffled = {"train": pd.DataFrame(), "test": pd.DataFrame()}

for category in categories:
    df = pd.read_csv(categories[category]["csv_path"])
    
    if df.empty:
        raise ValueError(f"Le fichier CSV pour {category} est vide ou introuvable.")
    
    if config["dataset"]["limit_per_category"] > 0:
        df = df.head(config["dataset"]["limit_per_category"])
        
    if "count_total_dataset" not in config["dataset"]:
        config["dataset"]["count_total_dataset"] = dict()
        
    config["dataset"]["count_total_dataset"][category] = len(df)
    if "total" not in config["dataset"]["count_total_dataset"]:
        config["dataset"]["count_total_dataset"]["total"] = 0
    config["dataset"]["count_total_dataset"]["total"] += len(df)

    df["filepath"] = df["Nom_Fichier"].apply(lambda x: os.path.join(categories[category]["data_folder_path"], x))

    # Logique One-vs-All (1 pour la classe cible, -1 pour les autres)
    for c in categories:
        df[c] = 1 if c == category else -1
    
    # Split Train / Test
    df_train = df.sample(frac=config["dataset"]["train_test_split_ratio"], random_state=config["lib"]["seed"])
    df_test = df.drop(df_train.index)
    
    df_csv_categories[category] = {"train": df_train, "test": df_test}

    if df_csv_all_shuffled["train"].empty:
        df_csv_all_shuffled["train"] = df_train
        df_csv_all_shuffled["test"] = df_test
    else:
        df_csv_all_shuffled["train"] = pd.concat([df_csv_all_shuffled["train"], df_train], ignore_index=True)
        df_csv_all_shuffled["test"] = pd.concat([df_csv_all_shuffled["test"], df_test], ignore_index=True)

# Mélange des lignes pour casser l'ordre des dossiers
df_csv_all_shuffled["train"] = df_csv_all_shuffled["train"].sample(frac=1, random_state=config["lib"]["seed"]).reset_index(drop=True)
df_csv_all_shuffled["test"] = df_csv_all_shuffled["test"].sample(frac=1, random_state=config["lib"]["seed"]).reset_index(drop=True)

# Extraction des chemins et des tableaux Y attendus
df_X_filepaths = {
    "train": df_csv_all_shuffled["train"]["filepath"].tolist(),
    "test": df_csv_all_shuffled["test"]["filepath"].tolist()
}

df_Y = {"train": dict(), "test": dict()}
for category in categories:
    df_Y["train"][category] = list(df_csv_all_shuffled["train"][category])
    df_Y["test"][category] = list(df_csv_all_shuffled["test"][category])

# ══════════════════════════════════════════════════════════════════════════════
#  5. CHARGEMENT ET NORMALISATION DES IMAGES (PILLOW)
# ══════════════════════════════════════════════════════════════════════════════

print("\n[*] Chargement et vectorisation des fichiers images...")
df_X = dict()

for step in df_X_filepaths:
    df_X[step] = []
    filepaths = df_X_filepaths[step]
    total = len(filepaths)

    for i, filepath in enumerate(filepaths):
        if i % 100 == 0 or i == total - 1:
            print(f"\r    Chargement {step}... {i+1}/{total} ({100*(i+1)/total:.1f}%)", end="", flush=True)

        with Image.open(filepath).convert("RGB") as img:
            img_array = (np.array(img).flatten()).astype(np.float32)

            if "W_length" not in config["dataset"]:
                config["dataset"]["W_length"] = len(img_array)
            elif len(img_array) != config["dataset"]["W_length"]:
                raise ValueError(f"Taille d'image incohérente pour {filepath}")

            df_X[step].append(img_array)
    print()

# Aplatissement du train en un vecteur géant continu pour le récepteur C
df_X["train"] = np.concatenate(df_X["train"])

# Standardisation globale
X_train_mean = np.mean(df_X["train"])
X_train_std = np.std(df_X["train"])

if X_train_std == 0:
    X_train_std = 1.0

df_X["train"] = ((df_X["train"] - X_train_mean) / X_train_std).astype(np.float32).tolist()

for i, X_test in enumerate(df_X["test"]):
    df_X["test"][i] = ((np.array(X_test) - X_train_mean) / X_train_std).astype(np.float32).tolist()

# ══════════════════════════════════════════════════════════════════════════════
#  6. ENTRAÎNEMENT DU MODÈLE ET SUIVI TENSORBOARD
# ══════════════════════════════════════════════════════════════════════════════

import tensorflow as tf

models = dict()
history = dict()

# Préparation du répertoire de log pour TensorBoard
current_time = datetime.datetime.now().strftime("Art %d-%H:%M:%S")
log_dir = os.path.join(BASE_DIR, "logs", "artgenre_linear", current_time)
summary_writer = tf.summary.create_file_writer(log_dir)

print(f"\n[*] Début de l'entraînement multiclasse. Logs TensorBoard : {log_dir}")

for category in categories:
    print(f"    -> Entraînement du classifieur pour la catégorie : {category}...")

    # Calcul de la dimension d'entrée par image
    W_length = len(df_X["train"]) // len(df_Y["train"][category])
    models[category] = LinearModel.init_random(input_dim=W_length)
    
    # Appel de la fonction native d'entraînement en C (Règle de Rosenblatt)
    history[category] = models[category].train(
        dataset_inputs=df_X["train"],
        dataset_expected_outputs=df_Y["train"][category],
        is_classification=True,
        alpha=config["model"]["alpha"], 
        epochs=config["model"]["epochs"]
    )

    # Exportation des métriques de Loss vers TensorBoard
    with summary_writer.as_default():
        for epoch, loss_value in enumerate(history[category]):
            tf.summary.scalar(f"Loss/{category}", loss_value, step=epoch)
            
summary_writer.flush()
print("[+] Entraînement terminé avec succès !")

# ══════════════════════════════════════════════════════════════════════════════
#  7. ÉVALUATION ET MATRICE DE CONFUSION
# ══════════════════════════════════════════════════════════════════════════════

print("\n[*] Phase d'évaluation sur le jeu de test...")
predictions = dict()

for category in categories:
    predictions[category] = dict()
    # Correction du bug d'origine : utilisation du dictionnaire 'models'
    predictions[category]["values"] = [models[category].predict(x, is_classification=False) for x in df_X["test"]]
    predictions[category]["prediction"] = [tanh(value) >= 0 for value in predictions[category]["values"]]

# Détermination de la meilleure classe prédite (ArgMax des valeurs brutes)
df_predictions_test = []
for i in range(len(predictions[list(categories.keys())[0]]["prediction"])):
    category_predicted = max(categories, key=lambda c: predictions[c]["values"][i])

    if predictions[category_predicted]["prediction"][i]:
        df_predictions_test.append(category_predicted)
    else:
        df_predictions_test.append(config["global"]["unknown_category"])

# Détermination des classes réelles attendues
df_predictions_expected = []
for i in range(len(df_Y["test"][list(categories.keys())[0]])):
    category_expected = next((c for c in categories if df_Y["test"][c][i] == 1), None)
    df_predictions_expected.append(category_expected)

# Construction de la Matrice de Confusion graphique
print("[*] Génération de la matrice de confusion...")
ConfusionMatrixDisplay.from_predictions(
    df_predictions_expected,
    df_predictions_test,
    labels=list(categories.keys()) + [config["global"]["unknown_category"]],
    cmap="Blues",
    xticks_rotation=45
)

length_X_test = len(df_X["test"])
length_X_train = config["dataset"]["count_total_dataset"]["total"] - length_X_test

plt.title("Matrice de Confusion - Modèle Linéaire")
plt.suptitle(
    f"Seed: {config['lib']['seed']} | Alpha: {config['model']['alpha']} | Epochs: {config['model']['epochs']}\n"
    f"Dataset: {length_X_train} train, {length_X_test} test (Total: {config['dataset']['count_total_dataset']['total']})",
    fontsize=9,
    y=0.98
)

plt.tight_layout()
print("[+] Affichage du graphique. Script terminé.")
plt.show()