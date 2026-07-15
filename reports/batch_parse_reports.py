"""
Parse en masse tous les config.json + report.md des dossiers de run pour extraire
les metriques cles sans avoir a lire chaque report.md individuellement.
Usage: python batch_parse_reports.py <folder1> [folder2] ...
Affiche un resume compact (une ligne par run) + JSON structure complete.
"""
import sys
import os
import json
import re

CATS = ["impressionism", "realism", "romanticism"]


def parse_run(folder: str) -> dict:
    result = {"folder": folder}

    config_path = os.path.join(folder, "config.json")
    if os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        result["model_type"] = config.get("model", {}).get("type")
        result["seed"] = config.get("lib", {}).get("seed")
        result["alpha"] = config.get("model", {}).get("alpha")
        result["epochs"] = config.get("model", {}).get("epochs")
        result["npl"] = config.get("model", {}).get("npl")
        result["mlp_hidden_layers"] = config.get("model", {}).get("mlp_hidden_layers")
        result["limit_per_category"] = config.get("dataset", {}).get("limit_per_category")
        result["train_positive_ratio"] = config.get("dataset", {}).get("train_positive_ratio")
        result["normalization"] = config.get("dataset", {}).get("normalization_method")

        test_acc = config.get("model", {}).get("test_multiclass_accuracy", {})
        result["top1_accuracy"] = test_acc.get("global", {}).get("top1_accuracy")
        cats = test_acc.get("categories", {})
        result["recall"] = {c: cats.get(c, {}).get("TPR") for c in CATS}
        result["balanced_accuracy"] = {c: cats.get(c, {}).get("balanced_accuracy") for c in CATS}

        train_acc = config.get("model", {}).get("train_last_accuracy_per_category", {})
        result["train_accuracy"] = {c: train_acc.get(c) for c in CATS}

        count = config.get("dataset", {}).get("count_total_dataset", {})
        if count:
            result["train_total"] = count.get("train", {}).get("total")
            result["test_total"] = count.get("test", {}).get("total")
    else:
        result["error"] = "no config.json"

    result["has_report_md"] = os.path.isfile(os.path.join(folder, "report.md"))
    result["has_tfevents"] = any(f.startswith("events.out.tfevents") for f in os.listdir(folder)) if os.path.isdir(folder) else False
    result["has_confusion_matrix"] = os.path.isfile(os.path.join(folder, "confusion_matrix_test.png"))

    return result


if __name__ == "__main__":
    folders = sys.argv[1:]
    if not folders:
        print("Usage: python batch_parse_reports.py <folder1> [folder2] ...")
        sys.exit(1)

    all_results = []
    for folder in folders:
        r = parse_run(folder)
        all_results.append(r)

        if "error" in r:
            print(f"[SKIP] {folder}: {r['error']}")
            continue

        acc = r.get("top1_accuracy")
        acc_str = f"{acc*100:.1f}%" if acc is not None else "?"
        arch = r.get("mlp_hidden_layers") or "-"
        print(f"[OK] {folder} | {r.get('model_type')} | seed={r.get('seed')} | alpha={r.get('alpha')} | epochs={r.get('epochs')} | arch={arch} | limit={r.get('limit_per_category')} | pos_ratio={r.get('train_positive_ratio')} | acc={acc_str} | tfevents={r.get('has_tfevents')}")

    print("\n" + "=" * 80)
    print(json.dumps(all_results, indent=2, ensure_ascii=False))
