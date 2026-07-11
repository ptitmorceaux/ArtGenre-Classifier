#!/usr/bin/env python3
"""
list_top_models.py

Liste les N runs avec la meilleure Top-1 Accuracy (multiclasse), à partir des
fichiers config.json sauvegardés par chaque run d'entraînement.

Usage:
    python list_top_models.py
    python list_top_models.py -n 5
    python list_top_models.py -n 20 --pattern "engine/core/output/*/*/*/*.json"
"""

import argparse
import glob
import json
import sys
from pathlib import Path


DEFAULT_PATTERN = "engine/core/output/*/*/*/*.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Liste les N meilleurs runs (config.json) par Top-1 Accuracy multiclasse."
    )
    parser.add_argument(
        "-n", "--n",
        dest="n",
        type=int,
        default=10,
        help="Nombre de runs à afficher (défaut: 10).",
    )
    parser.add_argument(
        "--pattern",
        dest="pattern",
        type=str,
        default=DEFAULT_PATTERN,
        help=f"Pattern glob vers les config.json (défaut: '{DEFAULT_PATTERN}').",
    )
    return parser.parse_args()


def extract_top1_accuracy(config: dict) -> float | None:
    """Extrait model.test_multiclass_accuracy.global.top1_accuracy, ou None si absent/incomplet."""
    try:
        return config["model"]["test_multiclass_accuracy"]["global"]["top1_accuracy"]
    except (KeyError, TypeError):
        return None


def extract_run_info(config: dict) -> dict:
    """Extrait quelques infos utiles pour identifier/comparer les runs dans l'affichage."""
    model = config.get("model", {})
    dataset = config.get("dataset", {})
    lib = config.get("lib", {})

    return {
        "model_type": model.get("type", "?"),
        "alpha": model.get("alpha", "?"),
        "epochs": model.get("epochs", "?"),
        "seed": lib.get("seed", "?"),
        "ratio": dataset.get("train_positive_ratio", "?"),
    }


def collect_runs(pattern: str) -> list[dict]:
    """Parcourt tous les fichiers matchant `pattern`, extrait les infos utiles, et
    ignore silencieusement (avec un warning sur stderr) les fichiers illisibles ou
    incomplets."""
    runs = list()

    filepaths = sorted(Path(p) for p in glob.glob(pattern))

    if not filepaths:
        print(f"[!] Aucun fichier trouvé pour le pattern '{pattern}'.", file=sys.stderr)
        return runs

    for filepath in filepaths:
        try:
            with open(filepath, "r") as f:
                config = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"[!] Impossible de lire '{filepath}': {e}", file=sys.stderr)
            continue

        top1_accuracy = extract_top1_accuracy(config)
        if top1_accuracy is None:
            print(f"[!] '{filepath}' ne contient pas de top1_accuracy (run incomplet ?), ignoré.", file=sys.stderr)
            continue

        run = {"path": filepath, "top1_accuracy": top1_accuracy}
        run.update(extract_run_info(config))
        runs.append(run)

    return runs


def print_top_runs(runs: list[dict], n: int) -> None:
    """Trie par top1_accuracy décroissante et affiche les n premiers dans un tableau aligné."""
    if not runs:
        print("Aucun run valide à afficher.")
        return

    top_runs = sorted(runs, key=lambda r: r["top1_accuracy"], reverse=True)[:n]

    headers = ["#", "Top-1 Acc", "Model", "Alpha", "Epochs", "Seed", "Ratio", "Path"]
    rows = [
        [
            str(i + 1),
            f"{run['top1_accuracy'] * 100:.2f}%",
            str(run["model_type"]),
            str(run["alpha"]),
            str(run["epochs"]),
            str(run["seed"]),
            str(run["ratio"]),
            str(run["path"]),
        ]
        for i, run in enumerate(top_runs)
    ]

    widths = [max(len(headers[i]), max((len(row[i]) for row in rows), default=0)) for i in range(len(headers))]

    def format_row(cells: list[str]) -> str:
        return " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells))

    print(f"\nTop {len(top_runs)} runs par Top-1 Accuracy ({len(runs)} runs valides trouvés au total)\n")
    print(format_row(headers))
    print("-+-".join("-" * w for w in widths))
    for row in rows:
        print(format_row(row))
    print()


def main() -> None:
    args = parse_args()
    runs = collect_runs(args.pattern)
    print_top_runs(runs, args.n)


if __name__ == "__main__":
    main()