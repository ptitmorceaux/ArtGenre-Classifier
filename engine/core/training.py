import tensorflow as tf

import engine.core.config as cf
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP
import engine.core.tensorboard as tb


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
        tb.write_tensorboard_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.1f}%\n")
        
        if "final_accuracy_per_category" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["final_accuracy_per_category"] = dict()
        cf.CONFIG["model"]["final_accuracy_per_category"][category] = acc_history[-1]
    
    return models_per_category


def train_mlp_models(df_X: dict, df_Y: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, MLP]:
    """Entraîne un MLP par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in cf.CONFIG["dataset"]["categories"].keys():
        print(f"> Training MLP {cf.CONFIG["model"]["npl"]} for category: {category}")
        models_per_category[category] = MLP(cf.CONFIG["model"]["npl"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            data_size=len(df_Y["train"][category]),  # requis par MLP.train, pas par LinearModel.train
            alpha=cf.CONFIG["model"]["alpha"],
            epochs=cf.CONFIG["model"]["epochs"],
            is_classification=True,
        )
        tb.write_tensorboard_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.1f}%\n")
        
        if "final_accuracy_per_category" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["final_accuracy_per_category"] = dict()
        cf.CONFIG["model"]["final_accuracy_per_category"][category] = acc_history[-1]

    return models_per_category


def train_models(df_X: dict, df_Y: dict) -> dict[str, LinearModel | MLP]:
    """Dispatch vers LinearModel ou MLP selon cf.CONFIG['model']['type']."""
    model_type = cf.CONFIG["model"]["type"]
    models = dict()

    summary_writer = tf.summary.create_file_writer(cf.CONFIG["output"]["logs"])
    print(f"\n[*] TensorBoard Logs directory: {cf.CONFIG['output']['logs']}\n")

    try:
        if model_type == "linear":
            models = train_linear_models(df_X, df_Y, summary_writer)
        elif model_type == "mlp":
            models = train_mlp_models(df_X, df_Y, summary_writer)
        else:
            raise ValueError(f"train_models(): unknown model type '{model_type}'.")

        with summary_writer.as_default():
            for title, markdown in tb.get_summary_md().items():
                tf.summary.text(title, markdown, step=0)

        return models
    finally:
        summary_writer.close()