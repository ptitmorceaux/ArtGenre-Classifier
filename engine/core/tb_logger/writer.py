import os
import tensorflow as tf

import engine.core.config as cf


def write_training_logs(
    summary_writer: tf.summary.SummaryWriter,
    category: str,
    loss_history: list[float],
    accuracy_history: list[float] | None
) -> None:
    """Écrit les courbes d'entraînement dans TensorBoard."""

    with summary_writer.as_default():
        for epoch in range(cf.CONFIG["model"]["epochs"]):

            tf.summary.scalar(
                f"Loss/{category}",
                loss_history[epoch],
                step=epoch
            )

            if accuracy_history is not None:
                tf.summary.scalar(
                    f"Accuracy/{category}",
                    accuracy_history[epoch],
                    step=epoch
                )

    summary_writer.flush()


def write_images(
    summary_writer: tf.summary.SummaryWriter
) -> None:
    """Ajoute les images d'évaluation dans TensorBoard."""

    confusion_matrix_path = os.path.join(
        cf.CONFIG["output"]["logs"],
        "confusion_matrix_test.png"
    )

    if not os.path.exists(confusion_matrix_path):
        return

    image = tf.io.read_file(confusion_matrix_path)
    image = tf.image.decode_png(image, channels=3)
    image = tf.expand_dims(image, axis=0)

    with summary_writer.as_default():
        tf.summary.image(
            "Evaluation/Confusion Matrix",
            image,
            step=0
        )


def write_markdown_from_dict(
    summary_writer: tf.summary.SummaryWriter,
    summaries: dict[str, str]
) -> None:
    """Écrit les sections Markdown dans TensorBoard."""

    with summary_writer.as_default():
        for title, markdown in summaries.items():
            tf.summary.text(
                title,
                markdown,
                step=0
            )

    summary_writer.flush()