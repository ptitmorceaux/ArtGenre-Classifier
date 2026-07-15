"""Fusionne les sorties JSON de batch_ingest.py dans runs_data.json."""
import json
import sys

RUNS_DATA = "reports/runs_data.json"

with open(RUNS_DATA, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {r["id"] for r in data["runs"]}

for batch_file in sys.argv[1:]:
    with open(batch_file, "r", encoding="utf-8") as f:
        new_entries = json.load(f)
    for entry in new_entries:
        entry.pop("_folder", None)
        if entry["id"] in existing_ids:
            print(f"[SKIP] id {entry['id']} already exists")
            continue
        data["runs"].append(entry)
        existing_ids.add(entry["id"])
        print(f"[ADD] id {entry['id']}: {entry['title']}")

with open(RUNS_DATA, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nTotal runs: {len(data['runs'])}")
