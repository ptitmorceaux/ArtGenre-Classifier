"""
list_top_models.py

Lists the N runs with the best Top-1 Accuracy (multiclass), based on the
config.json files saved by each training run.

Usage:
    python list_top_models.py
    python list_top_models.py -n 5
    python list_top_models.py -m mlp
    python list_top_models.py -a              # sort by most recent first instead
    python list_top_models.py -a -n 5 -m linear
    python list_top_models.py -n 20 --pattern "engine/core/output/*/*/*/*.json"
"""

import argparse
import glob
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


DEFAULT_PATTERN = "engine/core/output/*/*/*/*.json"
UNKNOWN = "?"

# A run's path looks like: .../<model_type>/<YYYY-mm-dd>/<HH-MM-SS_ms>
RUN_TIMEZONE = ZoneInfo("Europe/Paris")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List the N best runs (config.json) by multiclass Top-1 Accuracy."
    )
    parser.add_argument(
        "-n", "--n",
        dest="n",
        type=int,
        default=10,
        help="Number of runs to display (default: 10). If <= 0, shows all valid runs.",
    )
    parser.add_argument(
        "--pattern",
        dest="pattern",
        type=str,
        default=DEFAULT_PATTERN,
        help=f"Glob pattern to the config.json files (default: '{DEFAULT_PATTERN}').",
    )
    parser.add_argument(
        "-m", "--model",
        dest="model",
        type=str,
        default=None,
        help="Filter runs by model type (e.g. 'mlp', 'linear', 'rbf'). Case-insensitive.",
    )
    parser.add_argument(
        "-a", "--ago",
        dest="ago",
        action="store_true",
        help="Sort by most recent first instead of by Top-1 Accuracy. Adds a 'Rank' "
             "column showing each run's Top-1 Accuracy rank among all matching runs.",
    )
    return parser.parse_args()


def extract_top1_accuracy(config: dict) -> float | None:
    """Extracts model.test_multiclass_accuracy.global.top1_accuracy, or None if missing/incomplete."""
    try:
        return config["model"]["test_multiclass_accuracy"]["global"]["top1_accuracy"]
    except (KeyError, TypeError):
        return None


def extract_train_accuracy(config: dict) -> float | str:
    """Calcule la moyenne de l'accuracy d'entraînement sur toutes les catégories."""
    try:
        acc_dict = config["model"]["train_last_accuracy_per_category"]
        if not acc_dict:
            return UNKNOWN
        return sum(acc_dict.values()) / len(acc_dict)
    except (KeyError, TypeError):
        return UNKNOWN


def extract_extra_info(config: dict) -> str:
    """
    Extracts extra, model-type-specific info to display in the 'Info' column.
    """
    model = config.get("model", {})
    model_type = str(model.get("type", "")).lower().strip()

    if model_type == "mlp":
        return f"npl={model.get('npl', UNKNOWN)}"
    
    if model_type == "rbf":
        return f"centers={model.get('rbf_num_centers', UNKNOWN)}"

    return ""


def extract_run_info(config: dict) -> dict:
    """Extracts a few useful fields to identify/compare runs in the display."""
    model = config.get("model", {})
    dataset = config.get("dataset", {})
    lib = config.get("lib", {})
    output = config.get("output", {})

    return {
        "model_type": model.get("type", UNKNOWN),
        "norm": dataset.get("normalization_method", UNKNOWN),
        "alpha": model.get("alpha", UNKNOWN),
        "epochs": model.get("epochs", UNKNOWN),
        "seed": lib.get("seed", UNKNOWN),
        "limit_per_category": dataset.get("limit_per_category", UNKNOWN),
        "ratio": dataset.get("train_positive_ratio", UNKNOWN),
        "path": output.get("logs", UNKNOWN)
    }


def parse_run_datetime(path: str) -> datetime | None:
    if path == UNKNOWN:
        return None
    try:
        parts = Path(path).parts
        date_str, time_str = parts[-2], parts[-1]

        hours, minutes, seconds_ms = time_str.split("-")
        seconds = seconds_ms.split("_")[0]

        return datetime.strptime(
            f"{date_str} {hours}:{minutes}:{seconds}",
            "%Y-%m-%d %H:%M:%S"
        ).replace(tzinfo=RUN_TIMEZONE)
    except (ValueError, IndexError):
        return None


def format_time_ago(run_dt: datetime | None) -> str:
    if run_dt is None:
        return UNKNOWN
    now_dt = datetime.now(RUN_TIMEZONE)
    elapsed_seconds = max((now_dt - run_dt).total_seconds(), 0)

    if elapsed_seconds < 60:
        return f"{int(elapsed_seconds)}s"
    elapsed_minutes = elapsed_seconds / 60
    if elapsed_minutes < 60:
        return f"{int(elapsed_minutes)}min"
    elapsed_hours = elapsed_minutes / 60
    if elapsed_hours < 24:
        return f"{int(elapsed_hours)}h"
    elapsed_days = elapsed_hours / 24
    return f"{int(elapsed_days)}d"


def collect_runs(pattern: str, model_filter: str | None = None) -> list[dict]:
    runs = list()
    filepaths = sorted(Path(p) for p in glob.glob(pattern))

    if not filepaths:
        print(f"[!] No file found for pattern '{pattern}'.", file=sys.stderr)
        return runs

    normalized_filter = model_filter.lower().strip() if model_filter is not None else None

    for filepath in filepaths:
        try:
            with open(filepath, "r") as f:
                config = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"[!] Could not read '{filepath}': {e}", file=sys.stderr)
            continue

        top1_accuracy = extract_top1_accuracy(config)
        if top1_accuracy is None:
            # Assigne une valeur sentinelle pour permettre l'affichage des runs en cours ou en échec
            top1_accuracy = -1.0

        run = { 
            "top1_accuracy": top1_accuracy,
            "train_accuracy": extract_train_accuracy(config)
        }
        run.update(extract_run_info(config))
        run["info"] = extract_extra_info(config)

        if normalized_filter is not None and str(run["model_type"]).lower().strip() != normalized_filter:
            continue

        run["run_dt"] = parse_run_datetime(run["path"])
        run["elapsed"] = format_time_ago(run["run_dt"])
        runs.append(run)

    return runs


def assign_accuracy_ranks(runs: list[dict]) -> None:
    # Ignore les runs sans précision finale pour le classement
    valid_runs = [r for r in runs if r["top1_accuracy"] != -1.0]
    for rank, run in enumerate(sorted(valid_runs, key=lambda r: r["top1_accuracy"], reverse=True), start=1):
        run["rank"] = rank


def print_top_runs(runs: list[dict], n: int, sort_by_ago: bool = False) -> None:
    if not runs:
        print("No valid run to display.")
        return

    assign_accuracy_ranks(runs)

    if sort_by_ago:
        oldest_possible = datetime.min.replace(tzinfo=RUN_TIMEZONE)
        display_runs = sorted(runs, key=lambda r: r["run_dt"] or oldest_possible, reverse=True)
    else:
        display_runs = sorted(runs, key=lambda r: r["top1_accuracy"], reverse=True)

    if n > 0:
        display_runs = display_runs[:n]

    headers = ["#"]
    if sort_by_ago:
        headers.append("Rank")
    headers += ["Top-1 Acc", "Train Acc", "Model", "Norm", "Alpha", "Epochs", "Seed", "Limit", "Ratio", "Ago", "Info", "Path"]

    rows = []
    for i, run in enumerate(display_runs):
        row = [str(i + 1)]
        if sort_by_ago:
            row.append(str(run.get("rank", UNKNOWN)))

        # Formatage conditionnel pour repérer les WIP et les float vs str
        top1_str = f"{run['top1_accuracy'] * 100:.2f}%" if run['top1_accuracy'] != -1.0 else "WIP/Err"
        train_str = f"{run['train_accuracy'] * 100:.2f}%" if isinstance(run['train_accuracy'], float) else str(run['train_accuracy'])

        row += [
            top1_str,
            train_str,
            str(run["model_type"]),
            str(run["norm"]),
            str(run["alpha"]),
            str(run["epochs"]),
            str(run["seed"]),
            str(run["limit_per_category"]),
            f"{run['ratio'] * 100:.2f}%" if isinstance(run["ratio"], float) else str(run["ratio"]),
            str(run["elapsed"]),
            str(run["info"]),
            str(run["path"]),
        ]
        rows.append(row)

    widths = [max(len(headers[i]), max((len(row[i]) for row in rows), default=0)) for i in range(len(headers))]

    def format_row(cells: list[str]) -> str:
        return " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells))

    count_label = "all" if n <= 0 else f"top {len(display_runs)}"
    order_label = "most recent first" if sort_by_ago else "by Top-1 Accuracy"
    print(f"\nShowing {count_label} runs, {order_label} ({len(runs)} runs found in total)\n")

    print(format_row(headers))
    print("-+-".join("-" * w for w in widths))
    for row in rows:
        print(format_row(row))
    print()


def main() -> None:
    args = parse_args()
    runs = collect_runs(args.pattern, args.model)
    print_top_runs(runs, args.n, sort_by_ago=args.ago)


if __name__ == "__main__":
    main()