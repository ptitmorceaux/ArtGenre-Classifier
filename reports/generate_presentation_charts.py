"""
Genere les graphiques pour la presentation PowerPoint (section Experimentation).
Sortie: reports/presentation_charts/*.png
"""
import json
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import ConfusionMatrixDisplay

matplotlib.use("Agg")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "presentation_charts")
os.makedirs(OUT, exist_ok=True)

with open(os.path.join(HERE, "runs_data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

runs = {r["id"]: r for r in data["runs"]}

BLUE = "#2E75B6"
RED = "#C0504D"
GREEN = "#4CAF50"
GRAY = "#888888"
plt.rcParams.update({"font.size": 11})


# ============================================================
# 1. Phase 1 - Scaling architecture MLP
# ============================================================
archs = ["[64, 32]", "[128, 64]", "[256, 128]"]
accs = [runs[4]["accuracy"], runs[6]["accuracy"], runs[8]["accuracy"]]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(archs, accs, color=BLUE, width=0.5)
ax.axhline(33.3, color=GRAY, linestyle="--", linewidth=1.5, label="Hasard (33,3%)")
for bar, acc in zip(bars, accs):
    ax.text(bar.get_x() + bar.get_width()/2, acc + 0.8, f"{acc}%", ha="center", fontweight="bold")
ax.set_ylabel("Accuracy (%)")
ax.set_xlabel("Architecture MLP (couches cachées)")
ax.set_title("Phase 1 — Accuracy selon la taille du réseau\n(alpha=0.001, epochs=50, seed=42, 1000 images/classe)")
ax.set_ylim(0, 60)
ax.legend(loc="lower right")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "01_phase1_architecture_scaling.png"), dpi=150)
plt.close(fig)


# ============================================================
# 2. Phase 2 - Overfitting Linear (train vs test)
# ============================================================
cats = ["Impressionism", "Realism", "Romanticism"]
train_acc = [runs[9]["analysis"]["train_accuracy"][c.lower()] for c in cats]
test_acc = runs[9]["accuracy"]

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(cats))
width = 0.35
ax.bar(x - width/2, train_acc, width, label="Accuracy TRAIN (par classe)", color=RED)
ax.bar(x + width/2, [test_acc]*3, width, label=f"Accuracy TEST (globale, {test_acc}%)", color=BLUE)
ax.set_xticks(x)
ax.set_xticklabels(cats)
ax.set_ylabel("Accuracy (%)")
ax.set_title("Phase 2 — Surapprentissage détecté (Linear, 1000 img/classe, 100 epochs)\nÉcart Train/Test révélé par TensorBoard")
ax.set_ylim(0, 110)
ax.legend()
ax.grid(axis="y", alpha=0.3)
for i, v in enumerate(train_acc):
    ax.text(i - width/2, v + 1.5, f"{v}%", ha="center", fontsize=9)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "02_phase2_overfitting_linear.png"), dpi=150)
plt.close(fig)


# ============================================================
# 3. Phase 3 - Impact du fix de biais (avant/apres)
# ============================================================
fig, ax = plt.subplots(figsize=(7, 5.5))
labels = ["Avant\n(biais df.head())", "Après\n(tirage aléatoire)"]
values = [52.2, 41.8]
colors = [RED, GREEN]
bars = ax.bar(labels, values, color=colors, width=0.5)
ax.axhline(33.3, color=GRAY, linestyle="--", linewidth=1.5, label="Hasard (33,3%)")
for bar, v in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, v + 1, f"{v}%", ha="center", fontweight="bold", fontsize=13)
ax.set_ylabel("Accuracy (%)")
ax.set_title("Phase 3 — Impact du fix de sampling\nMLP [256,128], même config exacte, seule la sélection d'images change")
ax.set_ylim(0, 65)
ax.legend(loc="upper right")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "03_phase3_bias_fix_impact.png"), dpi=150)
plt.close(fig)


# ============================================================
# 4. Phase 4/5 - Scaling des donnees (MLP et Linear)
# ============================================================
fig, ax = plt.subplots(figsize=(9, 5.5))

mlp_x = [1000, 6000, 44000]
mlp_y = [runs[18]["accuracy"], runs[17]["accuracy"], runs[36]["accuracy"]]
mlp_labels_x = ["1000", "6000", "Dataset\ncomplet"]

linear_full_best = max(runs[i]["accuracy"] for i in [64,65,66,67,68,69,70,71,72])
linear_x = [1000, 6000, 44000]
linear_y = [41.9, 42.8, linear_full_best]  # runs 9, 10 approx, puis moyenne des runs full dataset

ax.plot(mlp_x, mlp_y, marker="o", markersize=9, linewidth=2.5, color=BLUE, label="MLP [256,256]")
ax.plot(linear_x, linear_y, marker="s", markersize=9, linewidth=2.5, color=RED, label="Linear (perceptron)")

for xi, yi in zip(mlp_x, mlp_y):
    ax.annotate(f"{yi}%", (xi, yi), textcoords="offset points", xytext=(0, 10), ha="center", color=BLUE, fontweight="bold")
for xi, yi in zip(linear_x, linear_y):
    ax.annotate(f"{yi}%", (xi, yi), textcoords="offset points", xytext=(0, -18), ha="center", color=RED, fontweight="bold")

ax.axhline(33.3, color=GRAY, linestyle="--", linewidth=1.2, label="Hasard (33,3%)")
ax.set_xscale("log")
ax.set_xticks(mlp_x)
ax.set_xticklabels(mlp_labels_x)
ax.set_xlabel("Images d'entraînement par classe (échelle log)")
ax.set_ylabel("Accuracy (%)")
ax.set_title("Phase 4-5 — Effet de la taille du dataset (tirage aléatoire corrigé)\nLes deux modèles progressent avec plus de données")
ax.set_ylim(30, 55)
ax.legend(loc="upper left")
ax.grid(alpha=0.3)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "04_phase4_5_data_scaling.png"), dpi=150)
plt.close(fig)


# ============================================================
# 5. Tableau recapitulatif final (pire -> meilleur)
# ============================================================
final_data = [
    ("MLP [256,128]\nalpha mal réglé", 44.1, "#E57373"),
    ("Linear\n≤6000 img/cl", 43.0, "#EF9A9A"),
    ("MLP [256,128] 1000img\nbiais head() (invalide)", 52.2, "#BDBDBD"),
    ("MLP [256,128] 1000img\ntirage corrigé", 41.8, "#FFB74D"),
    ("MLP [256,256]\n6000 img/cl", 46.7, "#AED581"),
    ("Linear\ndataset complet", 46.5, "#81C784"),
    ("MLP [256,256]\ndataset complet", 49.5, "#4CAF50"),
]
labels = [d[0] for d in final_data]
values = [d[1] for d in final_data]
colors = [d[2] for d in final_data]

fig, ax = plt.subplots(figsize=(10, 6.5))
y_pos = np.arange(len(labels))
bars = ax.barh(y_pos, values, color=colors)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=10)
ax.invert_yaxis()
ax.axvline(33.3, color=GRAY, linestyle="--", linewidth=1.5, label="Hasard (33,3%)")
for bar, v in zip(bars, values):
    ax.text(v + 0.8, bar.get_y() + bar.get_height()/2, f"{v}%", va="center", fontweight="bold")
ax.set_xlabel("Accuracy (%)")
ax.set_title("Récapitulatif final — du pire au meilleur réglage")
ax.set_xlim(0, 62)
ax.legend(loc="lower right")
ax.grid(axis="x", alpha=0.3)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "05_recap_final_pire_a_meilleur.png"), dpi=150)
plt.close(fig)


# ============================================================
# 7. Slide 6 - Linear : tentatives de correction du surapprentissage
# ============================================================
labels7 = ["Baseline\n1000 img/cl", "+Données\n2000 img/cl", "-Epochs\n100→50", "Alpha ÷10", "Norm.\nstandard"]
values7 = [runs[9]["accuracy"], runs[10]["accuracy"], runs[11]["accuracy"], runs[12]["accuracy"], runs[13]["accuracy"]]
colors7 = [GRAY, BLUE, BLUE, BLUE, BLUE]

fig, ax = plt.subplots(figsize=(9, 5.5))
bars = ax.bar(labels7, values7, color=colors7, width=0.55)
ax.axhline(33.3, color=GRAY, linestyle="--", linewidth=1.2, label="Hasard (33,3%)")
ax.axhline(values7[0], color=RED, linestyle=":", linewidth=1.5, label=f"Baseline ({values7[0]}%)")
for bar, v in zip(bars, values7):
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.6, f"{v}%", ha="center", fontweight="bold")
ax.set_ylabel("Accuracy (%)")
ax.set_title("Linear — Tentatives de correction du surapprentissage\n(dataset limité à ≤2000 images/classe à ce stade)")
ax.set_ylim(0, 55)
ax.legend(loc="lower right", fontsize=9)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "07_linear_correction_attempts.png"), dpi=150)
plt.close(fig)


# ============================================================
# 8. Slide 7 - Linear seul : scaling des donnees jusqu'au dataset complet
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5.5))
lx = [1000, 6000, 44000]
ly = [runs[9]["accuracy"], runs[10]["accuracy"], linear_full_best]
lx_labels = ["1000", "6000", "Dataset\ncomplet"]

ax.plot(lx, ly, marker="s", markersize=11, linewidth=3, color=RED)
for xi, yi in zip(lx, ly):
    ax.annotate(f"{yi}%", (xi, yi), textcoords="offset points", xytext=(0, 12), ha="center", fontweight="bold", fontsize=12, color=RED)
ax.axhline(33.3, color=GRAY, linestyle="--", linewidth=1.2, label="Hasard (33,3%)")
ax.axhspan(41, 45, color=RED, alpha=0.08, label="Plage \"plafond\" observée\nà ≤6000 img/classe")
ax.set_xscale("log")
ax.set_xticks(lx)
ax.set_xticklabels(lx_labels)
ax.set_xlabel("Images d'entraînement par classe (échelle log)")
ax.set_ylabel("Accuracy (%)")
ax.set_title("Linear — Le \"plafond\" disparaît sur le dataset complet")
ax.set_ylim(30, 52)
ax.legend(loc="upper left")
ax.grid(alpha=0.3)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "08_linear_full_dataset_reveal.png"), dpi=150)
plt.close(fig)


# ============================================================
# 9. Slide 8 - Comparaison finale tete-a-tete MLP vs Linear
# ============================================================
fig, ax = plt.subplots(figsize=(7.5, 6))
models9 = ["Linear\n(perceptron)", "MLP\n[256,256]"]
best9 = [linear_full_best, runs[36]["accuracy"]]
colors9 = [RED, BLUE]

bars = ax.bar(models9, best9, color=colors9, width=0.45)
ax.axhline(33.3, color=GRAY, linestyle="--", linewidth=1.2, label="Hasard (33,3%)")
for bar, v in zip(bars, best9):
    ax.text(bar.get_x() + bar.get_width()/2, v + 1, f"{v}%", ha="center", fontweight="bold", fontsize=15)
ax.annotate(
    f"écart : {round(best9[1]-best9[0],1)} pts",
    xy=(0.5, (best9[0]+best9[1])/2), xycoords=("data", "data"),
    ha="center", fontsize=11, color="#333333",
    bbox=dict(boxstyle="round", fc="white", ec="#999999")
)
ax.set_ylabel("Accuracy (%)")
ax.set_title("Meilleur résultat de chaque modèle\n(dataset complet, tirage aléatoire corrigé)")
ax.set_ylim(0, 60)
ax.legend(loc="upper left")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
fig.savefig(os.path.join(OUT, "09_comparaison_finale_mlp_vs_linear.png"), dpi=150)
plt.close(fig)


# ============================================================
# 6. Matrice de confusion du meilleur modele (run 36)
# ============================================================
r36 = runs[36]
if "confusion_matrix" in r36:
    matrix = np.array(r36["confusion_matrix"])
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    disp = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=["Impressionism", "Realism", "Romanticism"])
    disp.plot(cmap="Blues", ax=ax, colorbar=True, xticks_rotation=30)
    ax.set_title(f"Meilleur modèle — MLP [256,256], dataset complet\nAccuracy = {r36['accuracy']}%")
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, "06_confusion_matrix_best_model.png"), dpi=150)
    plt.close(fig)
    print("Confusion matrix run 36 generee (donnees stockees)")
else:
    print("Pas de confusion_matrix stockee pour run 36 - a recuperer depuis l'image source si besoin")

print(f"\nTous les graphiques generes dans {OUT}")
for f in sorted(os.listdir(OUT)):
    print(" -", f)
