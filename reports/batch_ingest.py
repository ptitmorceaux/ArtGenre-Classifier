"""
Ingestion en masse de plusieurs dossiers de run en une fois.
Usage: python batch_ingest.py <start_id> <folder1> <folder2> ...

Pour chaque dossier (dans l'ordre donne, id = start_id, start_id+1, ...) :
  - Copie confusion_matrix_test.png -> reports/images/run_XX.png
  - Genere le graphique TensorBoard si des tfevents existent -> reports/tensorboard/run_XX.png
  - Parse config.json (si present) pour les metriques
  - Construit une entree JSON prete a fusionner dans runs_data.json

Affiche le tableau JSON complet a la fin (a copier dans runs_data.json).
"""
import sys
import os
import json
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_tensorboard import load_scalars, plot_metrics
from batch_parse_reports import parse_run

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(HERE, "images")
TENSORBOARD_DIR = os.path.join(HERE, "tensorboard")
CATS = ["impressionism", "realism", "romanticism"]


def pct(x):
    return round(x * 100, 1) if x is not None else None


def build_entry(run_id: int, folder: str) -> dict:
    r = parse_run(folder)
    run_id_str = f"{run_id:02d}"

    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(TENSORBOARD_DIR, exist_ok=True)

    cm_src = os.path.join(folder, "confusion_matrix_test.png")
    if os.path.isfile(cm_src):
        shutil.copy(cm_src, os.path.join(IMAGES_DIR, f"run_{run_id_str}.png"))

    if r.get("has_tfevents"):
        try:
            series = load_scalars(folder)
            plot_metrics(series, os.path.join(TENSORBOARD_DIR, f"run_{run_id_str}.png"))
        except Exception as e:
            print(f"[WARN] tfevents non exploitable pour {folder}: {e}", file=sys.stderr)

    if "error" in r:
        return {
            "id": run_id,
            "title": f"Run auto-importe (pas de config.json) — {folder}",
            "model": "?",
            "architecture": "inconnue",
            "seed": None, "alpha": None, "epochs": None,
            "normalization": None, "train": None, "test": None,
            "accuracy": None,
            "analysis": {"recall": {}, "observations": [f"Dossier source: {folder}. Pas de config.json disponible."], "conclusion": ""},
            "_folder": folder,
        }

    arch = r.get("mlp_hidden_layers")
    model = r.get("model_type")
    limit = r.get("limit_per_category")
    limit_note = f" | limit_per_category={limit}" if not isinstance(limit, (int, float)) or limit != 6000 else ""

    entry = {
        "id": run_id,
        "title": f"{'MLP ' + str(arch) if model == 'mlp' else 'Linear'} — seed {r.get('seed')}, limit={limit}, pos_ratio={r.get('train_positive_ratio')} (batch import)",
        "model": model,
        "architecture": str(arch) if model == "mlp" else "perceptron (Rosenblatt), one-vs-rest",
        "seed": r.get("seed"),
        "alpha": r.get("alpha"),
        "epochs": r.get("epochs"),
        "normalization": r.get("normalization"),
        "train": r.get("train_total"),
        "test": r.get("test_total"),
        "accuracy": pct(r.get("top1_accuracy")),
        "analysis": {
            "recall": {c: pct(r["recall"].get(c)) for c in CATS} if r.get("recall") else {},
            "train_accuracy": {c: pct(r["train_accuracy"].get(c)) for c in CATS} if r.get("train_accuracy") else {},
            "observations": [
                f"Run importe en lot depuis {folder}.",
                f"train_positive_ratio={r.get('train_positive_ratio')}{limit_note}."
            ],
            "conclusion": ""
        },
        "_folder": folder,
    }
    return entry


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python batch_ingest.py <start_id> <folder1> [folder2] ...")
        sys.exit(1)

    start_id = int(sys.argv[1])
    folders = sys.argv[2:]

    entries = []
    for i, folder in enumerate(folders):
        run_id = start_id + i
        entry = build_entry(run_id, folder)
        entries.append(entry)
        acc = entry.get("accuracy")
        print(f"[{run_id}] {folder} -> acc={acc}%", file=sys.stderr)

    print(json.dumps(entries, indent=2, ensure_ascii=False))
