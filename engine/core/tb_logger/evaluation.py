import engine.core.config as cf


def _fmt_pct(value: float) -> str:
    """Formatte un taux en pourcentage, ou 'N/A' si non défini (valeur sentinelle -1)."""
    return "N/A" if value == -1 else f"{value:.2%}"


def get_test_accuracy_md() -> str | None:
    """Résumé de l'accuracy de test par catégorie, avec la matrice de confusion binaire
    (TP/TN/FP/FN) et les taux dérivés (TPR/TNR/FPR/FNR)."""

    test_accuracy = cf.CONFIG["model"].get("test_accuracy")

    if test_accuracy is None:
        return None

    mean_accuracy = sum(stats["accuracy"] for stats in test_accuracy.values()) / len(test_accuracy)

    summary = """
# Test Accuracy

| Category | Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|
"""

    for category, stats in test_accuracy.items():
        summary += (
            f"| {category} | "
            f"{_fmt_pct(stats['accuracy'])} | "
            f"{_fmt_pct(stats['TPR'])} | "
            f"{_fmt_pct(stats['TNR'])} | "
            f"{_fmt_pct(stats['FPR'])} | "
            f"{_fmt_pct(stats['FNR'])} |\n"
        )

    summary += (
        f"| **Mean** | **{mean_accuracy:.2%}** | | | | |\n"
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
        summary["0. Evaluation/0. Test Accuracy"] = test_accuracy_md

    return summary