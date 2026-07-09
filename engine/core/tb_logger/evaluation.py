import engine.core.config as cf


def _fmt_pct(value: float) -> str:
    """Formatte un taux en pourcentage, ou 'N/A' si non défini (valeur sentinelle -1)."""
    return "N/A" if value == -1 else f"{value:.2%}"


def _mean(values: list[float]) -> float | None:
    """Moyenne d'une colonne, en ignorant les valeurs sentinelles -1 (non définies)."""
    valid = [v for v in values if v != -1]
    return sum(valid) / len(valid) if valid else None


def get_test_accuracy_md() -> str | None:
    """Résumé de l'accuracy de test par catégorie, avec la matrice de confusion binaire
    (TP/TN/FP/FN) et les taux dérivés (TPR/TNR/FPR/FNR/Balanced Accuracy), plus une ligne
    de moyenne par colonne (et non juste une moyenne d'accuracy globale)."""

    test_accuracy = cf.CONFIG["model"].get("test_accuracy")

    if test_accuracy is None:
        return None

    columns = ["accuracy", "balanced_accuracy", "TPR", "TNR", "FPR", "FNR"]
    means = {col: _mean([stats[col] for stats in test_accuracy.values()]) for col in columns}

    summary = """
# Test Accuracy

| Category | Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
"""

    for category, stats in test_accuracy.items():
        summary += (
            f"| {category} | "
            f"{_fmt_pct(stats['accuracy'])} | "
            f"{_fmt_pct(stats['balanced_accuracy'])} | "
            f"{_fmt_pct(stats['TPR'])} | "
            f"{_fmt_pct(stats['TNR'])} | "
            f"{_fmt_pct(stats['FPR'])} | "
            f"{_fmt_pct(stats['FNR'])} |\n"
        )

    summary += (
        f"| **Mean** | "
        f"**{_fmt_pct(means['accuracy'])}** | "
        f"**{_fmt_pct(means['balanced_accuracy'])}** | "
        f"**{_fmt_pct(means['TPR'])}** | "
        f"**{_fmt_pct(means['TNR'])}** | "
        f"**{_fmt_pct(means['FPR'])}** | "
        f"**{_fmt_pct(means['FNR'])}** |\n"
    )

    summary += """
## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
"""

    for category, stats in test_accuracy.items():
        summary += (
            f"| {category} | {stats['TP']} | {stats['TN']} | {stats['FP']} | {stats['FN']} |\n"
        )

    return summary


def get_evaluation_md() -> dict[str, str]:
    """Retourne toute la section Evaluation."""

    summary = {}

    test_accuracy_md = get_test_accuracy_md()

    if test_accuracy_md:
        summary["0. Evaluation/Test Accuracy"] = test_accuracy_md

    return summary