import engine.core.config as cf


def get_final_accuracy_md() -> str | None:
    """Résumé de la dernière accuracy d'entraînement."""

    accuracy = cf.CONFIG["model"].get("train_last_accuracy_per_category")

    if accuracy is None:
        return None

    mean = sum(accuracy.values()) / len(accuracy)

    summary = """
# Final Train Accuracy

| Category | Accuracy |
|---|---:|
"""

    for category, value in accuracy.items():
        summary += (
            f"| {category} | {value:.2%} |\n"
        )

    summary += (
        f"| **Mean** | **{mean:.2%}** |\n"
    )

    return summary


def get_training_md() -> dict[str, str]:

    summary = {}

    accuracy_md = get_final_accuracy_md()

    if accuracy_md:
        summary["1. Training/Final Train Accuracy"] = accuracy_md

    return summary