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

    if model["type"] in ("mlp", "mlp_multiclass"):
        summary += (
            f"| NPL | `{model['npl']}` |\n"
        )

    return summary


def get_dataset_md() -> str:
    """Résumé du dataset."""

    dataset = cf.CONFIG["dataset"]
    categories = list(dataset["categories"]["train"].keys())
    model_type = cf.CONFIG["model"]["type"]

    loaded = dataset["count_total_dataset"]["loaded"]
    train_counts = dataset["count_total_dataset"]["used_during_train"]

    # En One-vs-All (mlp/linear/rbf), chaque catégorie a son propre dataset
    # ("model_<cat>"). En multiclasse, un seul dataset partagé ("model_multiclass")
    # couvre toutes les catégories -> on indirige la clé de lookup selon le type.
    def _count_key(category: str) -> str:
        return "model_multiclass" if model_type == "mlp_multiclass" else f"model_{category}"

    # Diagonale (train_counts[_count_key(cat)]["categories"][cat]) = nb d'images
    # CHARGÉES par catégorie, jamais affecté par le ratio (seuls les négatifs
    # sont sous-échantillonnés, et le multiclasse n'en a pas) -> total d'images en
    # RAM reconstruit à partir de ça.
    total_train_loaded = sum(train_counts[_count_key(cat)]["categories"][cat] for cat in categories)
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
        count_train = train_counts[_count_key(category)]["categories"][category]
        count_test = loaded["test"]["categories"][category]
        summary += f"| {category} | {count_train} | {count_test} |\n"

    if model_type == "mlp_multiclass":
        # Un seul dataset partagé, utilisé une seule fois par toutes les catégories :
        # la matrice de répartition One-vs-All ci-dessous n'a pas de sens ici (déjà
        # entièrement résumée par le tableau ci-dessus).
        return summary

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