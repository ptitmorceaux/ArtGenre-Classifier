from pathlib import Path

import engine.core.config as cf


def get_models_md() -> str:

    folder = Path(
        cf.CONFIG["output"]["models"]
    )

    summary = """
# Models

| Category | File | Size |
|---|---|---:|
"""

    total = 0

    for file in folder.glob("*.bin"):

        size = file.stat().st_size
        total += size

        category = file.name.split("__")[1]

        summary += (
            f"| {category} | "
            f"`{file.name}` | "
            f"{size / 1024**2:.2f} MB |\n"
        )

    summary += (
        f"\nTotal size: `{total / 1024**2:.2f} MB`"
    )

    return summary


def get_artifacts_md() -> str:

    return f"""
# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `{cf.CONFIG["output"].get("confusion_matrix_test", "Not available")}` |

{get_models_md()}
"""