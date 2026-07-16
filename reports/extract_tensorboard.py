"""
Lit les fichiers events.out.tfevents.* d'un dossier de run et regenere le graphique
Accuracy/Loss par categorie (meme presentation visuelle que TensorBoard).
Usage: python extract_tensorboard.py <run_output_folder> <out_png_path>
"""
import sys
import os
import glob

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
from tensorboard.util import tensor_util


def load_scalars(run_folder: str) -> dict:
    """Charge tous les Loss/<cat> et Accuracy/<cat> (loggues comme 'tensors' par tf.summary.scalar en TF2),
    de tous les tfevents du dossier, tries par step. Ignore les autres tensors (texte/markdown du report.md)."""
    event_files = sorted(glob.glob(os.path.join(run_folder, "events.out.tfevents.*")))
    if not event_files:
        raise FileNotFoundError(f"Aucun fichier tfevents trouve dans {run_folder}")

    series = {}  # tag -> list[(step, value)]

    for ef in event_files:
        ea = EventAccumulator(ef, size_guidance={"tensors": 0})
        ea.Reload()
        for tag in ea.Tags().get("tensors", []):
            if not (tag.startswith("Loss/") or tag.startswith("Accuracy/")):
                continue
            events = ea.Tensors(tag)
            series.setdefault(tag, [])
            for e in events:
                value = tensor_util.make_ndarray(e.tensor_proto).item()
                series[tag].append((e.step, value))

    # Tri par step et dedoublonnage (garde la derniere valeur pour un step donne)
    for tag in series:
        by_step = dict(series[tag])
        series[tag] = sorted(by_step.items())

    return series


def plot_metrics(series: dict, out_path: str, title: str = "") -> None:
    categories = sorted(set(tag.split("/")[1] for tag in series if "/" in tag))
    metrics = ["Accuracy", "Loss"]

    fig, axes = plt.subplots(len(metrics), len(categories), figsize=(4.2 * len(categories), 3.6 * len(metrics)))
    if len(categories) == 1:
        axes = axes.reshape(-1, 1)

    for row, metric in enumerate(metrics):
        for col, cat in enumerate(categories):
            ax = axes[row][col]
            tag = f"{metric}/{cat}"
            if tag in series:
                steps, values = zip(*series[tag])
                ax.plot(steps, values, linewidth=1.5)
                final_val = values[-1]
                ax.set_title(f"{metric}/{cat}\nfinal={final_val:.4f}", fontsize=10)

                # Zoom auto sur la zone "stabilisee" (comme TensorBoard) : on ignore le
                # transitoire des tout premiers epochs pour calibrer l'axe Y, sinon le pic
                # de depart ecrase l'echelle et cache les variations fines une fois converge.
                skip = max(2, round(len(values) * 0.05))
                if len(values) > skip:
                    stable = values[skip:]
                    lo, hi = min(stable), max(stable)
                    pad = (hi - lo) * 0.15 if hi > lo else abs(hi) * 0.01 or 0.01
                    ax.set_ylim(lo - pad, hi + pad)
            else:
                ax.set_title(f"{metric}/{cat}\n(absent)", fontsize=10)
            ax.grid(True, alpha=0.3)
            if row == len(metrics) - 1:
                ax.set_xlabel("epoch")

    if title:
        fig.suptitle(title, fontsize=10, y=1.02)

    plt.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def get_final_values(series: dict) -> dict:
    """Renvoie {tag: valeur finale} pour tous les tags."""
    return {tag: values[-1][1] for tag, values in series.items() if values}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_tensorboard.py <run_output_folder> <out_png_path>")
        sys.exit(1)

    run_folder = sys.argv[1]
    out_path = sys.argv[2]

    series = load_scalars(run_folder)
    plot_metrics(series, out_path)

    print(f"[OK] Graphique sauvegarde : {out_path}")
    print("\nValeurs finales :")
    for tag, val in sorted(get_final_values(series).items()):
        print(f"  {tag}: {val:.4f}")
