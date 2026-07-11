#!/usr/bin/env python3
"""
list_top_models.py

Lists the N runs with the best Top-1 Accuracy (multiclass), based on the
config.json files saved by each training run.

Usage:
    python list_top_models.py
    python list_top_models.py -n 5
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
# (see config.py -> get_date_time_now(), which produces these two segments
# using the Europe/Paris timezone).
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
    return parser.parse_args()


def extract_top1_accuracy(config: dict) -> float | None:
    """Extracts model.test_multiclass_accuracy.global.top1_accuracy, or None if missing/incomplete."""
    try:
        return config["model"]["test_multiclass_accuracy"]["global"]["top1_accuracy"]
    except (KeyError, TypeError):
        return None


def extract_run_info(config: dict) -> dict:
    """Extracts a few useful fields to identify/compare runs in the display."""
    model = config.get("model", {})
    dataset = config.get("dataset", {})
    lib = config.get("lib", {})
    output = config.get("output", {})

    return {
        "model_type": model.get("type", UNKNOWN),
        "alpha": model.get("alpha", UNKNOWN),
        "epochs": model.get("epochs", UNKNOWN),
        "seed": lib.get("seed", UNKNOWN),
        "limit_per_category": dataset.get("limit_per_category", UNKNOWN),
        "ratio": dataset.get("train_positive_ratio", UNKNOWN),
        "path": output.get("logs", UNKNOWN)
    }


def format_time_ago(path: str) -> str:
    """
    Parses the last 2 segments of the path (.../<date>/<time_ms>) to work out
    how long ago the run was launched. Returns UNKNOWN if the path doesn't match
    the expected format (e.g. 'YYYY-mm-dd/HH-MM-SS_ms').
    """
    if path == UNKNOWN:
        return UNKNOWN

    try:
        parts = Path(path).parts
        date_str, time_str = parts[-2], parts[-1]

        hours, minutes, seconds_ms = time_str.split("-")
        seconds = seconds_ms.split("_")[0]

        run_dt = datetime.strptime(
            f"{date_str} {hours}:{minutes}:{seconds}",
            "%Y-%m-%d %H:%M:%S"
        ).replace(tzinfo=RUN_TIMEZONE)

        now_dt = datetime.now(RUN_TIMEZONE)
        elapsed_seconds = max((now_dt - run_dt).total_seconds(), 0)

        if elapsed_seconds < 60:
            return f"{int(elapsed_seconds)} s"

        elapsed_minutes = elapsed_seconds / 60
        if elapsed_minutes < 60:
            return f"{int(elapsed_minutes)} min"

        elapsed_hours = elapsed_minutes / 60
        if elapsed_hours < 24:
            return f"{int(elapsed_hours)} h"

        elapsed_days = elapsed_hours / 24
        return f"{int(elapsed_days)} d"

    except (ValueError, IndexError):
        return UNKNOWN


def collect_runs(pattern: str) -> list[dict]:
    """Walks through every file matching `pattern`, extracts the useful info, and
    silently skips (with a warning on stderr) unreadable or incomplete files."""
    runs = list()

    filepaths = sorted(Path(p) for p in glob.glob(pattern))

    if not filepaths:
        print(f"[!] No file found for pattern '{pattern}'.", file=sys.stderr)
        return runs

    for filepath in filepaths:
        try:
            with open(filepath, "r") as f:
                config = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"[!] Could not read '{filepath}': {e}", file=sys.stderr)
            continue

        top1_accuracy = extract_top1_accuracy(config)
        if top1_accuracy is None:
            print(f"[!] '{filepath}' has no top1_accuracy (incomplete run?), skipping.", file=sys.stderr)
            continue

        run = { "top1_accuracy": top1_accuracy }
        run.update(extract_run_info(config))
        run["elapsed"] = format_time_ago(run["path"])
        runs.append(run)

    return runs


def print_top_runs(runs: list[dict], n: int) -> None:
    """Sorts by descending top1_accuracy and prints the first n in an aligned table."""
    if not runs:
        print("No valid run to display.")
        return

    top_runs = sorted(runs, key=lambda r: r["top1_accuracy"], reverse=True)
    if n > 0:
        top_runs = top_runs[:n]

    headers = ["#", "Top-1 Acc", "Model", "Alpha", "Epochs", "Seed", "Limit", "Ratio", "Ago", "Path"]
    rows = [
        [
            str(i + 1),
            f"{run['top1_accuracy'] * 100:.2f}%",
            str(run["model_type"]),
            str(run["alpha"]),
            str(run["epochs"]),
            str(run["seed"]),
            str(run["limit_per_category"]),
            f"{run['ratio'] * 100:.2f}%" if isinstance(run["ratio"], float) else str(run["ratio"]),
            str(run["elapsed"]),
            str(run["path"]),
        ]
        for i, run in enumerate(top_runs)
    ]

    widths = [max(len(headers[i]), max((len(row[i]) for row in rows), default=0)) for i in range(len(headers))]

    def format_row(cells: list[str]) -> str:
        return " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells))

    label = "all" if n <= 0 else f"top {len(top_runs)}"
    print(f"\nShowing {label} runs by Top-1 Accuracy ({len(runs)} valid runs found in total)\n")
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