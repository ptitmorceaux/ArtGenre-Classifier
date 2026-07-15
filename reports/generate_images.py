"""
Regenere les images de matrice de confusion pour chaque run dans runs_data.json.
Style identique a celui de engine/core/evaluation.py::plot_confusion_matrix().
A relancer a chaque mise a jour de runs_data.json (idempotent, ecrase les images existantes).
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "runs_data.json")
IMAGES_DIR = os.path.join(HERE, "images")

os.makedirs(IMAGES_DIR, exist_ok=True)

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

labels = data["labels"]

for run in data["runs"]:
    if "confusion_matrix" not in run:
        print(f"[SKIP] run_{run['id']:02d} (pas de confusion_matrix stockee)")
        continue
    matrix = np.array(run["confusion_matrix"])

    fig, ax = plt.subplots(figsize=(6.5, 4.2))

    disp = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=labels)
    disp.plot(cmap="Blues", ax=ax, colorbar=True, xticks_rotation=45)

    ax.set_title("Confusion Matrix", fontsize=11)

    fig.suptitle(
        f"Model: {run['model']} | Norm: {run['normalization']} | Seed: {run['seed']}\n"
        f"Alpha: {run['alpha']} | Epochs: {run['epochs']}\n"
        f"Train: {run['train']}, Test: {run['test']}",
        fontsize=8.5,
        y=1.02
    )

    plt.tight_layout()

    out_path = os.path.join(IMAGES_DIR, f"run_{run['id']:02d}.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] run_{run['id']:02d}.png ({run['title']})")

print(f"\n{len(data['runs'])} images generees dans {IMAGES_DIR}")
