import engine.core.config as cf
from .artifacts import get_artifacts_md


def get_model_md() -> str:
    """Résumé de la configuration du modèle."""

    model = cf.CONFIG["model"]

    summary = f"""
# Model

| Parameter | Value |
|---|---|
| Seed | `{cf.CONFIG["lib"]["seed"]}` |
| Type | `{model["type"]}` |
| Alpha | `{model["alpha"]}` |
| Epochs | `{model["epochs"]}` |
"""

    if model["type"] == "mlp":
        summary += (
            f"| NPL | `{model['npl']}` |\n"
        )

    return summary


def get_dataset_md() -> str:
    """Résumé du dataset."""

    dataset = cf.CONFIG["dataset"]

    summary = f"""
# Dataset

| Parameter | Value |
|---|---|
| Total samples Train | `{dataset["count_total_dataset"]["train"]["total"]}` |
| Total samples Test | `{dataset["count_total_dataset"]["test"]["total"]}` |
| Limit per category | `{dataset["limit_per_category"]}` |
| Normalization | `{dataset["normalization_method"]}` |

## Categories

| Category | Images Train | Images Test |
|---|---:|---:|
"""

    for category in dataset["categories"]["train"].keys():
        count_train = dataset["count_total_dataset"]["train"][category]
        count_test = dataset["count_total_dataset"]["test"][category]
        summary += f"| {category} | {count_train} | {count_test} |\n"

    return summary


def get_experiment_md() -> dict[str, str]:
    """Retourne toute la section Experiment."""

    return {
        "2. Experiment/0. Model": get_model_md(),
        "2. Experiment/1. Dataset": get_dataset_md(),
        "2. Experiment/2. Artifacts": get_artifacts_md(),
    }