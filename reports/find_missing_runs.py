"""Compare le leaderboard complet (top_models.py) avec les dossiers deja ingeres (batch_*.json)."""
import json
import io

known = set()
batch_files = [
    "batch_linear2.json", "batch_linear_out.json", "batch_missed.json", "batch_mlp_out.json",
    "batch_new52.json", "batch_rbf_combo.json", "batch_rbf_redo.json", "batch_rbf_round2.json",
    "batch_recover.json",
]
for bf in batch_files:
    try:
        entries = json.load(io.open(f"reports/{bf}", encoding="utf-8"))
        for e in entries:
            if "_folder" in e:
                known.add(e["_folder"].replace("\\", "/"))
    except FileNotFoundError:
        pass

paths_lb = []
with io.open("reports/leaderboard_full.txt", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines[3:]:
    line = line.rstrip("\n")
    if not line.strip() or line.startswith("-"):
        continue
    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 2:
        continue
    path = parts[-1].strip()
    if path.startswith("engine"):
        paths_lb.append(path.replace("\\", "/"))

paths_lb_set = set(paths_lb)
missing = sorted(paths_lb_set - known)

print("Total dans leaderboard:", len(paths_lb_set))
print("Total deja connus:", len(known))
print("MANQUANTS:", len(missing))
for m in missing:
    print(" -", m)

with io.open("reports/missing_runs.txt", "w", encoding="utf-8") as f:
    for m in missing:
        f.write(m + "\n")
