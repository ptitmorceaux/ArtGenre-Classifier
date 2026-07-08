import tensorflow as tf

from engine.core.config import CONFIG, CATEGORIES
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP


def _build_mlp_npl() -> list[int]:
    """Construit l'architecture (npl) du MLP : input_dim -> couches cachées -> 1 sortie (one-vs-all)."""
    input_dim = CONFIG["dataset"]["W_length"]
    hidden_layers = CONFIG["model"]["mlp_hidden_layers"]
    return [input_dim, *hidden_layers, 1]


def train_linear_models(df_X: dict, df_Y: dict) -> dict[str, LinearModel]:
    """Entraîne un LinearModel par catégorie (One-vs-All)."""
    models_per_category = dict()

    summary_writer = tf.summary.create_file_writer(CONFIG["output"]["logs"])
    print(f"\n[*] TensorBoard Logs directory: {CONFIG['output']['logs']}")
    print(f"[*] Models (bin) directory: {CONFIG['output']['models']}\n")

    for category in CATEGORIES:
        print(f"> Training LinearModel for category: {category}")
        models_per_category[category] = LinearModel.init_random(input_dim=CONFIG["dataset"]["W_length"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            is_classification=True,
            alpha=CONFIG["model"]["alpha"],
            epochs=CONFIG["model"]["epochs"]
        )

        # Écriture dans TensorBoard
        with summary_writer.as_default():
            for epoch in range(CONFIG["model"]["epochs"]):
                tf.summary.scalar(f"Loss/{category}", loss_history[epoch], step=epoch)
                tf.summary.scalar(f"Accuracy/{category}", acc_history[epoch], step=epoch)
                
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.1f}%\n")
    
    summary_writer.flush()
    return models_per_category


def train_mlp_models(df_X: dict, df_Y: dict) -> dict[str, MLP]:
    """Entraîne un MLP par catégorie (One-vs-All)."""
    models_per_category = dict()
    npl = _build_mlp_npl()

    for category in CATEGORIES:
        print(f"> Training MLP {npl} for category: {category}")
        models_per_category[category] = MLP(npl)
        models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            data_size=len(df_Y["train"][category]),  # requis par MLP.train, pas par LinearModel.train
            alpha=CONFIG["model"]["alpha"],
            epochs=CONFIG["model"]["epochs"],
            is_classification=True,
        )
        print(f"    Model for category '{category}' trained successfully.")

    return models_per_category


def train_models(df_X: dict, df_Y: dict) -> dict[str, LinearModel | MLP]:
    """Dispatch vers LinearModel ou MLP selon CONFIG['model']['type']."""
    model_type = CONFIG["model"]["type"]

    if model_type == "linear":
        return train_linear_models(df_X, df_Y)
    elif model_type == "mlp":
        return train_mlp_models(df_X, df_Y)
    else:
        raise ValueError(f"train_models(): unknown model type '{model_type}'.")