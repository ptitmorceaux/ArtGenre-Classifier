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
| Total samples | `{dataset["count_total_dataset"]["total"]}` |
| Limit per category | `{dataset["limit_per_category"]}` |
| Train/Test split | `{dataset["train_test_split_ratio"]}` |
| Normalization | `{dataset["normalization_method"]}` |

## Categories

| Category | Images |
|---|---:|
"""

    for category, count in dataset["count_total_dataset"].items():
        if category != "total":
            summary += f"| {category} | {count} |\n"

    return summary


def get_experiment_md() -> dict[str, str]:
    """Retourne toute la section Experiment."""

    return {
        "1.Experiment/0.Model": get_model_md(),
        "1.Experiment/1.Dataset": get_dataset_md(),
        "1.Experiment/2.Artifacts": get_artifacts_md(),
    }