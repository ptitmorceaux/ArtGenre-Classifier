"""
Ingestion automatique d'un run pour le rapport Word.

Usage: python ingest_run.py <run_output_folder> <run_id>

Pour un dossier de run (ex: engine/core/output/mlp/2026-07-12/21-18-42_760600) :
  1. Copie confusion_matrix_test.png -> reports/images/run_<id>.png
  2. Regenere le graphique TensorBoard (Loss/Accuracy par epoch) -> reports/tensorboard/run_<id>.png
  3. Affiche un resume texte (config + metriques du report.md) pour ecrire l'analyse
"""
import sys
import os
import json
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_tensorboard import load_scalars, plot_metrics, get_final_values

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(HERE, "images")
TENSORBOARD_DIR = os.path.join(HERE, "tensorboard")


def main():
    if len(sys.argv) < 3:
        print("Usage: python ingest_run.py <run_output_folder> <run_id>")
        sys.exit(1)

    run_folder = sys.argv[1]
    run_id = int(sys.argv[2])
    run_id_str = f"{run_id:02d}"

    if not os.path.isdir(run_folder):
        print(f"[ERREUR] Dossier introuvable : {run_folder}")
        sys.exit(1)

    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(TENSORBOARD_DIR, exist_ok=True)

    # 1. Config
    config_path = os.path.join(run_folder, "config.json")
    config = {}
    if os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        print(f"[OK] Config chargee depuis {config_path}")
    else:
        print(f"[WARN] Pas de config.json dans {run_folder}")

    # 2. Confusion matrix
    cm_path = os.path.join(run_folder, "confusion_matrix_test.png")
    if os.path.isfile(cm_path):
        dest = os.path.join(IMAGES_DIR, f"run_{run_id_str}.png")
        shutil.copy(cm_path, dest)
        print(f"[OK] Confusion matrix copiee -> {dest}")
    else:
        print(f"[WARN] Pas de confusion_matrix_test.png dans {run_folder}")

    # 3. TensorBoard
    try:
        series = load_scalars(run_folder)
        tb_dest = os.path.join(TENSORBOARD_DIR, f"run_{run_id_str}.png")
        title = f"Model: {config.get('model', {}).get('type', '?')} | Seed: {config.get('lib', {}).get('seed', '?')}"
        plot_metrics(series, tb_dest, title=title)
        print(f"[OK] Graphique TensorBoard genere -> {tb_dest}")
        final_values = get_final_values(series)
    except FileNotFoundError as e:
        print(f"[WARN] {e}")
        final_values = {}

    # 4. report.md (affichage brut pour analyse)
    report_path = os.path.join(run_folder, "report.md")
    print("\n" + "=" * 70)
    if os.path.isfile(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"[WARN] Pas de report.md dans {run_folder}")
    print("=" * 70)

    print("\n--- Valeurs finales TensorBoard (train) ---")
    for tag, val in sorted(final_values.items()):
        print(f"  {tag}: {val:.4f}")

    print(f"\n--- Config utilisee ---")
    print(json.dumps(config.get("model", {}), indent=2, ensure_ascii=False))
    print(json.dumps(config.get("dataset", {}), indent=2, ensure_ascii=False, default=str)[:1000])


if __name__ == "__main__":
    main()
