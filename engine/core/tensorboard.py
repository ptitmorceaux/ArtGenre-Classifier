import tensorflow as tf

import engine.core.config as cf


def write_tensorboard_logs(summary_writer: tf.summary.SummaryWriter, category: str, loss_history: list[float], accuracy_history: list[float] | None) -> None:
    """Écrit les logs de perte et d'exactitude dans TensorBoard."""
    with summary_writer.as_default():
        for epoch in range(cf.CONFIG["model"]["epochs"]):
            tf.summary.scalar(f"{category}/Loss", loss_history[epoch], step=epoch)
            if accuracy_history is not None:
                tf.summary.scalar(f"{category}/Accuracy", accuracy_history[epoch], step=epoch)
    # Rend les événements immédiatement visibles dans TensorBoard.
    # Les logs sont flushés après chaque catégorie, car le code C ne renvoie
    # l'historique qu'une fois l'entraînement du modèle terminé.
    summary_writer.flush()


def get_summary_md() -> dict[str, str]:
    """Génère les sections Markdown du résumé TensorBoard."""
    model_type = cf.CONFIG["model"]["type"]
    model_config = cf.CONFIG["model"]
    dataset_config = cf.CONFIG["dataset"]
    lib_config = cf.CONFIG["lib"]

    summaries = {}

    # Model information
    summaries["Run/Model"] = f"""
# Model

- **Type:** `{model_type}`
- **Seed:** `{lib_config["seed"]}`
- **Alpha:** `{model_config["alpha"]}`
- **Epochs:** `{model_config["epochs"]}`
"""

    # MLP architecture (only for MLP models)
    if model_type == "mlp":
        summaries["Run/Architecture"] = f"""
# Architecture

`{cf.CONFIG["model"]["npl"]}`
"""

    # Dataset information
    dataset_summary = f"""
# Dataset

- **Total samples:** `{dataset_config["count_total_dataset"]["total"]}`
- **Normalization:** `{dataset_config["normalization_method"]}`

## Categories

| Category | Images |
|---|---:|
"""

    for category, count in dataset_config["count_total_dataset"].items():
        if category != "total":
            dataset_summary += f"| {category} | {count} |\n"

    summaries["Run/Dataset"] = dataset_summary

    # Final results
    final_accuracy = model_config.get("final_accuracy_per_category")

    if final_accuracy:
        mean_accuracy = sum(final_accuracy.values()) / len(final_accuracy)

        results_summary = f"""
# Final Accuracy

**Mean accuracy:** `{mean_accuracy:.2%}`

| Category | Accuracy |
|---|---:|
"""

        for category, accuracy in final_accuracy.items():
            results_summary += f"| {category} | {accuracy:.2%} |\n"

        summaries["Run/Results"] = results_summary

    return summaries