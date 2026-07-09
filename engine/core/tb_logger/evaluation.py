import engine.core.config as cf


def _fmt_pct(value: float) -> str:
    """Formatte un taux en pourcentage, ou 'N/A' si non défini (valeur sentinelle -1)."""
    return "N/A" if value == -1 else f"{value:.2%}"


def _mean(values: list[float]) -> float | None:
    """Moyenne d'une colonne, en ignorant les valeurs sentinelles -1 (non définies)."""
    valid = [v for v in values if v != -1]
    return sum(valid) / len(valid) if valid else None


def _stats_table_md(stats_per_category: dict) -> str:
    """
    Génère un tableau markdown Exact Match Accuracy/Balanced Accuracy/TPR/TNR/FPR/FNR par catégorie
    + une ligne de moyenne par colonne, réutilisé pour test_individual_accuracy et pour
    test_multiclass_accuracy['categories'] (même format de stats dans les deux cas).
    """
    columns = ["exact_match_accuracy", "balanced_accuracy", "TPR", "TNR", "FPR", "FNR"]
    means = {col: _mean([stats[col] for stats in stats_per_category.values()]) for col in columns}

    summary = """
| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
"""

    for category, stats in stats_per_category.items():
        summary += (
            f"| {category} | "
            f"{_fmt_pct(stats['exact_match_accuracy'])} | "
            f"{_fmt_pct(stats['balanced_accuracy'])} | "
            f"{_fmt_pct(stats['TPR'])} | "
            f"{_fmt_pct(stats['TNR'])} | "
            f"{_fmt_pct(stats['FPR'])} | "
            f"{_fmt_pct(stats['FNR'])} |\n"
        )

    summary += (
        f"| **Mean** | "
        f"**{_fmt_pct(means['exact_match_accuracy'])}** | "
        f"**{_fmt_pct(means['balanced_accuracy'])}** | "
        f"**{_fmt_pct(means['TPR'])}** | "
        f"**{_fmt_pct(means['TNR'])}** | "
        f"**{_fmt_pct(means['FPR'])}** | "
        f"**{_fmt_pct(means['FNR'])}** |\n"
    )

    return summary


def _confusion_counts_md(stats_per_category: dict) -> str:
    """Tableau TP/TN/FP/FN bruts par catégorie."""
    summary = """
## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
"""

    for category, stats in stats_per_category.items():
        summary += (
            f"| {category} | {stats['TP']} | {stats['TN']} | {stats['FP']} | {stats['FN']} |\n"
        )

    return summary


def get_test_individual_accuracy_md() -> str | None:
    """Résumé de l'accuracy de test de chaque modèle individuel (One-vs-All), évalué
    seul avec son propre seuil — indépendamment des autres modèles."""

    test_individual_accuracy = cf.CONFIG["model"].get("test_individual_accuracy")

    if test_individual_accuracy is None:
        return None

    summary = "\n# Individual Models (One-vs-All)\n"
    summary += _stats_table_md(test_individual_accuracy)
    summary += _confusion_counts_md(test_individual_accuracy)

    return summary


def get_test_multiclass_accuracy_md() -> str | None:
    """Résumé du résultat final multiclasse (argmax entre les modèles) : pour chaque
    catégorie, comment se comporte la décision finale du pipeline en One-vs-Rest, plus
    les métriques globales (exact match + balanced accuracy moyenne)."""

    test_multiclass = cf.CONFIG["model"].get("test_multiclass_accuracy")

    if test_multiclass is None:
        return None

    categories_stats = test_multiclass["categories"]
    global_stats = test_multiclass["global"]

    summary = f"""
## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | {_fmt_pct(global_stats['top1_accuracy'])} |
| Average Balanced Accuracy | {_fmt_pct(global_stats['avg_balanced_accuracy'])} |
"""

    summary += "\n## Final Multiclass Result (Argmax)\n"
    summary += _stats_table_md(categories_stats)
    summary += _confusion_counts_md(categories_stats)

    return summary


def get_evaluation_md() -> dict[str, str]:
    """Retourne toute la section Evaluation."""

    summary = {}

    multiclass_md = get_test_multiclass_accuracy_md()
    if multiclass_md:
        summary["0. Evaluation/0. Final Multiclass Result"] = multiclass_md

    individual_md = get_test_individual_accuracy_md()
    if individual_md:
        summary["0. Evaluation/1. Individual Models"] = individual_md

    return summary