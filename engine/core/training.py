import tensorflow as tf

import engine.core.config as cf
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP


def _build_mlp_npl() -> list[int]:
    """Construit l'architecture (npl) du MLP : input_dim -> couches cachées -> 1 sortie (one-vs-all)."""
    input_dim = cf.CONFIG["dataset"]["W_length"]
    hidden_layers = cf.CONFIG["model"]["mlp_hidden_layers"]
    return [input_dim, *hidden_layers, 1]


def _write_tensorboard_logs(summary_writer: tf.summary.SummaryWriter, category: str, loss_history: list[float], accuracy_history: list[float] | None) -> None:
    """Écrit les logs de perte et d'exactitude dans TensorBoard."""
    with summary_writer.as_default():
        for epoch in range(cf.CONFIG["model"]["epochs"]):
            tf.summary.scalar(f"Loss/{category}", loss_history[epoch], step=epoch)
            if accuracy_history is not None:
                tf.summary.scalar(f"Accuracy/{category}", accuracy_history[epoch], step=epoch)
    # Rend les événements immédiatement visibles dans TensorBoard.
    # Les logs sont flushés après chaque catégorie, car le code C ne renvoie
    # l'historique qu'une fois l'entraînement du modèle terminé.
    summary_writer.flush()


def train_linear_models(df_X: dict, df_Y: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, LinearModel]:
    """Entraîne un LinearModel par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in cf.CONFIG["dataset"]["categories"].keys():
        print(f"> Training LinearModel for category: {category}")
        models_per_category[category] = LinearModel.init_random(input_dim=cf.CONFIG["dataset"]["W_length"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            is_classification=True,
            alpha=cf.CONFIG["model"]["alpha"],
            epochs=cf.CONFIG["model"]["epochs"]
        )
        _write_tensorboard_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.1f}%\n")
    
    return models_per_category


def train_mlp_models(df_X: dict, df_Y: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, MLP]:
    """Entraîne un MLP par catégorie (One-vs-All)."""
    models_per_category = dict()
    npl = _build_mlp_npl()

    for category in cf.CONFIG["dataset"]["categories"].keys():
        print(f"> Training MLP {npl} for category: {category}")
        models_per_category[category] = MLP(npl)
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            data_size=len(df_Y["train"][category]),  # requis par MLP.train, pas par LinearModel.train
            alpha=cf.CONFIG["model"]["alpha"],
            epochs=cf.CONFIG["model"]["epochs"],
            is_classification=True,
        )
        _write_tensorboard_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for category '{category}' trained successfully.")
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.1f}%\n")

    return models_per_category


def train_models(df_X: dict, df_Y: dict) -> dict[str, LinearModel | MLP]:
    """Dispatch vers LinearModel ou MLP selon cf.CONFIG['model']['type']."""
    model_type = cf.CONFIG["model"]["type"]

    summary_writer = tf.summary.create_file_writer(cf.CONFIG["output"]["logs"])
    print(f"\n[*] TensorBoard Logs directory: {cf.CONFIG['output']['logs']}\n")

    try:
        if model_type == "linear":
            return train_linear_models(df_X, df_Y, summary_writer)
        elif model_type == "mlp":
            return train_mlp_models(df_X, df_Y, summary_writer)
        else:
            raise ValueError(f"train_models(): unknown model type '{model_type}'.")
    finally:
        summary_writer.close()