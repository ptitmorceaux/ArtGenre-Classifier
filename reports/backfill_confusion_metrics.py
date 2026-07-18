"""
Complete TNR/FPR/FNR/balanced_accuracy dans runs_data.json pour tous les runs deja
ingeres, en relisant leur config.json d'origine (dossiers sources conserves dans les
fichiers batch_*.json avant que merge_batch.py ne supprime le champ _folder).
"""
import json
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_parse_reports import parse_run

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS_DATA = os.path.join(HERE, "runs_data.json")
CATS = ["impressionism", "realism", "romanticism"]

BATCH_FILES = [
    "batch_mlp_out.json", "batch_linear_out.json", "batch_missed.json",
    "batch_new52.json", "batch_linear2.json", "batch_new73.json",
    "batch_recover.json", "batch_rbf_redo.json", "batch_rbf_round2.json",
    "batch_rbf_combo.json", "batch_mlp_round3.json", "batch_multiclass_rbf.json",
]

id_to_folder = {}
for bf in BATCH_FILES:
    path = os.path.join(HERE, bf)
    if not os.path.isfile(path):
        continue
    with io.open(path, "r", encoding="utf-8") as f:
        entries = json.load(f)
    for e in entries:
        if "_folder" in e:
            id_to_folder[e["id"]] = e["_folder"]

# Dossiers connus manuellement (runs traites via ingest_run.py, pas batch_ingest.py)
id_to_folder.setdefault(17, "engine/core/output/mlp/2026-07-12/21-18-42_760600")
id_to_folder.setdefault(18, "engine/core/output/mlp/2026-07-13/07-37-56_165400")

print(f"{len(id_to_folder)} dossiers sources retrouves.")

with io.open(RUNS_DATA, "r", encoding="utf-8") as f:
    data = json.load(f)

updated, no_data, no_folder = [], [], []
for run in data["runs"]:
    rid = run["id"]
    if run["analysis"].get("tnr"):
        continue  # deja present

    folder = id_to_folder.get(rid)
    if not folder or not os.path.isdir(folder):
        no_folder.append(rid)
        continue

    r = parse_run(folder)
    if "error" in r or not r.get("tnr") or all(v is None for v in r["tnr"].values()):
        no_data.append(rid)
        continue

    def pct(x):
        return round(x * 100, 1) if x is not None else None

    run["analysis"]["tnr"] = {c: pct(r["tnr"].get(c)) for c in CATS}
    run["analysis"]["fpr"] = {c: pct(r["fpr"].get(c)) for c in CATS}
    run["analysis"]["fnr"] = {c: pct(r["fnr"].get(c)) for c in CATS}
    run["analysis"]["balanced_accuracy"] = {c: pct(r["balanced_accuracy"].get(c)) for c in CATS}
    updated.append(rid)

print(f"Runs mis a jour : {len(updated)} -> {updated}")
print(f"Runs sans donnees TNR/FPR/FNR dans leur config.json : {no_data}")
print(f"Runs sans dossier source retrouve (probablement transcrits a la main, ex: 1-16, 19-23) : {no_folder}")

with io.open(RUNS_DATA, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("runs_data.json sauvegarde.")
