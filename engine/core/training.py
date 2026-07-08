import os
import datetime
import tensorflow as tf
import matplotlib.pyplot as plt

from engine.core.config import CONFIG, CATEGORIES
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP

def plot_and_save_metrics(loss_histories: dict, acc_histories: dict, session_id: str) -> tuple[str, str]:
    """Génère et sauvegarde les courbes de Loss et d'Accuracy dans le dossier de la session."""
    metrics_dir = os.path.join(CONFIG["output"]["outdir"], "metrics", session_id)
    os.makedirs(metrics_dir, exist_ok=True)
    
    # 1. Courbe de Loss
    plt.figure(figsize=(10, 5))
    for category, loss_history in loss_histories.items():
        plt.plot(loss_history, label=category)
    plt.title(f"Loss Curve ({CONFIG['model']['type'].upper()})")
    plt.xlabel("Epochs"); plt.ylabel("Loss"); plt.legend()
    loss_filename = "loss_curve.png"
    plt.savefig(os.path.join(metrics_dir, loss_filename), bbox_inches='tight')
    plt.close()
    
    # 2. Courbe d'Accuracy
    plt.figure(figsize=(10, 5))
    for category, acc_history in acc_histories.items():
        plt.plot(acc_history, label=category)
    plt.title(f"Accuracy Curve ({CONFIG['model']['type'].upper()})")
    plt.xlabel("Epochs"); plt.ylabel("Accuracy"); plt.legend()
    acc_filename = "accuracy_curve.png"
    plt.savefig(os.path.join(metrics_dir, acc_filename), bbox_inches='tight')
    plt.close()
    
    return loss_filename, acc_filename

def train_linear_models(df_X: dict, df_Y: dict, session_id: str):
    models_per_category = dict()
    loss_histories, acc_histories = dict(), dict()

    # Création du dossier de log avec la date du jour (Train_JJ_MM)
    date_folder = datetime.datetime.now().strftime("Train_%d_%m")
    log_dir = os.path.join(CONFIG["output"]["logs"], "Linear_Classification", date_folder, session_id)
    summary_writer = tf.summary.create_file_writer(log_dir)

    for category in CATEGORIES:
        models_per_category[category] = LinearModel.init_random(input_dim=CONFIG["dataset"]["W_length"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            is_classification=True,
            alpha=CONFIG["model"]["alpha"],
            epochs=CONFIG["model"]["epochs"]
        )
        
        loss_histories[category] = loss_history
        acc_histories[category] = acc_history

        with summary_writer.as_default():
            for epoch in range(CONFIG["model"]["epochs"]):
                tf.summary.scalar(f"Loss/{category}", loss_history[epoch], step=epoch)
                tf.summary.scalar(f"Accuracy/{category}", acc_history[epoch], step=epoch)
                
    summary_writer.flush()
    loss_filename, acc_filename = plot_and_save_metrics(loss_histories, acc_histories, session_id)
    
    return models_per_category, loss_filename, acc_filename

def train_models(df_X: dict, df_Y: dict, session_id: str) -> tuple[dict, str|None, str|None]:
    model_type = CONFIG["model"]["type"]
    if model_type == "linear":
        return train_linear_models(df_X, df_Y, session_id)
    elif model_type == "mlp":
        # Pour le MLP, on renverra (models_per_category, None, None) pour l'instant
        return train_mlp_models(df_X, df_Y, session_id), None, None
