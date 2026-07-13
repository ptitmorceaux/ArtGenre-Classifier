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
    categories = list(dataset["categories"]["train"].keys())

    loaded = dataset["count_total_dataset"]["loaded"]
    train_counts = dataset["count_total_dataset"]["used_during_train"]

    # Diagonale (train_counts["model_<cat>"]["categories"][cat]) = nb d'images
    # CHARGÉES par catégorie, jamais affecté par le ratio (seuls les négatifs
    # sont sous-échantillonnés) -> total d'images en RAM reconstruit à partir de ça.
    total_train_loaded = sum(train_counts[f"model_{cat}"]["categories"][cat] for cat in categories)
    total_test = loaded["test"]["total"]

    ratio = dataset.get("train_positive_ratio", -1)
    ratio_display = "désactivé (-1)" if ratio == -1 else f"{ratio:.2f}"

    summary = f"""
# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `{total_train_loaded}` |
| Total samples Test | `{total_test}` |
| Limit per category | `{dataset["limit_per_category"]}` |
| Train positive ratio | `{ratio_display}` |
| Normalization | `{dataset["normalization_method"]}` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
"""

    for category in categories:
        count_train = train_counts[f"model_{category}"]["categories"][category]
        count_test = loaded["test"]["categories"][category]
        summary += f"| {category} | {count_train} | {count_test} |\n"

    # Matrice de répartition One-vs-All : pour chaque modèle, combien d'images
    # de chaque catégorie ont réellement été utilisées (utile pour vérifier
    # visuellement l'effet de train_positive_ratio), + la taille totale du
    # dataset d'entraînement RÉEL de ce modèle (varie avec le ratio, contrairement
    # au total "chargées" ci-dessus qui ne bouge jamais).
    summary += "\n## Répartition par modèle (One-vs-All)\n"
    summary += "\n| Modèle \\ Catégorie utilisée | " + " | ".join(categories) + " | **Total dataset modèle** |\n"
    summary += "|---|" + "---:|" * len(categories) + "---:|\n"

    for model_category in categories:
        model_entry = train_counts[f"model_{model_category}"]
        row = model_entry["categories"]
        summary += (
            f"| **{model_category}** | "
            + " | ".join(str(row[c]) for c in categories)
            + f" | **{model_entry['total']}** |\n"
        )

    return summary


def get_experiment_md() -> dict[str, str]:
    """Retourne toute la section Experiment."""

    return {
        "2. Experiment/0. Model": get_model_md(),
        "2. Experiment/1. Dataset": get_dataset_md(),
        "2. Experiment/2. Artifacts": get_artifacts_md(),
    }