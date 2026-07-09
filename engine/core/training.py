import tensorflow as tf

import engine.core.config as cf
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP
import engine.core.tb_logger as tb


def train_linear_models(df_X: dict, df_Y: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, LinearModel]:
    """Entraîne un LinearModel par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        print(f"\n> Training LinearModel for category: {category}")
        models_per_category[category] = LinearModel.init_random(input_dim=cf.CONFIG["dataset"]["W_length"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            is_classification=True,
            alpha=cf.CONFIG["model"]["alpha"],
            epochs=cf.CONFIG["model"]["epochs"]
        )
        tb.write_training_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.2f}%")
        
        if "train_last_accuracy_per_category" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["train_last_accuracy_per_category"] = dict()
        cf.CONFIG["model"]["train_last_accuracy_per_category"][category] = acc_history[-1]
    
    return models_per_category


def train_mlp_models(df_X: dict, df_Y: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, MLP]:
    """Entraîne un MLP par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        print(f"> Training MLP {cf.CONFIG['model']['npl']} for category: {category}")
        models_per_category[category] = MLP(cf.CONFIG["model"]["npl"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            data_size=len(df_Y["train"][category]),  # requis par MLP.train, pas par LinearModel.train
            alpha=cf.CONFIG["model"]["alpha"],
            epochs=cf.CONFIG["model"]["epochs"],
            is_classification=True,
        )
        tb.write_training_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.2f}%\n")
        
        if "train_last_accuracy_per_category" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["train_last_accuracy_per_category"] = dict()
        cf.CONFIG["model"]["train_last_accuracy_per_category"][category] = acc_history[-1]

    return models_per_category


def train_models(summary_writer: tf.summary.SummaryWriter, df_X: dict, df_Y: dict) -> dict[str, LinearModel | MLP]:
    """Dispatch vers LinearModel ou MLP selon cf.CONFIG['model']['type']."""
    model_type = cf.CONFIG["model"]["type"]

    print(f"\n[*] TensorBoard Logs directory: {cf.CONFIG['output']['logs']}")

    print(f"\n========>>> TRAINING {model_type} MODELS <<<========")
    models = dict()
    
    try:
        # Choix du type de modèle à entraîner
        if model_type == "linear":
            models = train_linear_models(df_X, df_Y, summary_writer)
        elif model_type == "mlp":
            models = train_mlp_models(df_X, df_Y, summary_writer)
        else:
            raise ValueError(f"train_models(): unknown model type '{model_type}'.")
        
        print(f"\n========>>> TRAINING {model_type} MODELS COMPLETE <<<========")
        return models
    
    except Exception as e:
        summary_writer.close()
        raise e