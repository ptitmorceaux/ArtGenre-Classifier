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


def extract_extra_info(config: dict) -> str:
    """
    Extracts extra, model-type-specific info to display in the 'Info' column.
    Currently only populated for MLP runs (shows the 'npl' architecture);
    empty string for any other model type.
    """
    model = config.get("model", {})
    model_type = str(model.get("type", "")).lower().strip()

    if model_type == "mlp":
        return f"npl={model.get('npl', UNKNOWN)}"

    return ""


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


def parse_run_datetime(path: str) -> datetime | None:
    """
    Parses the last 2 segments of the path (.../<date>/<time_ms>) into an aware
    datetime. Returns None if the path doesn't match the expected format
    (e.g. 'YYYY-mm-dd/HH-MM-SS_ms').
    """
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
    """Formats how long ago `run_dt` was, or UNKNOWN if `run_dt` is None."""
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
    """Walks through every file matching `pattern`, extracts the useful info, and
    silently skips (with a warning on stderr) unreadable or incomplete files.

    If `model_filter` is given, only runs whose model type matches it (case- and
    whitespace-insensitive) are kept."""
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
            print(f"[!] '{filepath}' has no top1_accuracy (incomplete run?), skipping.", file=sys.stderr)
            continue

        run = { "top1_accuracy": top1_accuracy }
        run.update(extract_run_info(config))
        run["info"] = extract_extra_info(config)

        if normalized_filter is not None and str(run["model_type"]).lower().strip() != normalized_filter:
            continue

        run["run_dt"] = parse_run_datetime(run["path"])
        run["elapsed"] = format_time_ago(run["run_dt"])
        runs.append(run)

    return runs


def assign_accuracy_ranks(runs: list[dict]) -> None:
    """Assigns each run its rank (1 = highest top1_accuracy) among the given runs, in place."""
    for rank, run in enumerate(sorted(runs, key=lambda r: r["top1_accuracy"], reverse=True), start=1):
        run["rank"] = rank


def print_top_runs(runs: list[dict], n: int, sort_by_ago: bool = False) -> None:
    """
    Displays runs in an aligned table.

    Default: sorted by descending Top-1 Accuracy, truncated to the first n.
    With sort_by_ago=True: sorted by most recent first (runs with an unparsable
    path are pushed to the end), and a 'Rank' column is added showing each run's
    Top-1 Accuracy rank among all matching runs (computed before truncation).
    """
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
    headers += ["Top-1 Acc", "Model", "Alpha", "Epochs", "Seed", "Limit", "Ratio", "Ago", "Info", "Path"]

    rows = []
    for i, run in enumerate(display_runs):
        row = [str(i + 1)]
        if sort_by_ago:
            row.append(str(run["rank"]))
        row += [
            f"{run['top1_accuracy'] * 100:.2f}%",
            str(run["model_type"]),
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
    print(f"\nShowing {count_label} runs, {order_label} ({len(runs)} valid runs found in total)\n")
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