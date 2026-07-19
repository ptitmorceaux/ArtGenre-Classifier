import tensorflow as tf

import engine.core.config as cf
from engine.core.dataset import build_one_vs_all_train_arrays, build_multiclass_train_arrays
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP
from engine.interop.rbf import RBF
import engine.core.tb_logger as tb

# Clé unique du dict models_per_category quand cf.CONFIG["model"]["type"] == "mlp_multiclass"
# (un seul modèle partagé, contrairement au One-vs-All qui a une clé par catégorie).
# Réutilisée telle quelle dans evaluation.py et persistence.py.
MULTICLASS_KEY = "multiclass"


def train_linear_models(data: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, LinearModel]:
    """Entraîne un LinearModel par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        print(f"\n> Training LinearModel for category: {category}")
        X, Y = build_one_vs_all_train_arrays(data, category)

        models_per_category[category] = LinearModel.init_random(input_dim=cf.CONFIG["dataset"]["W_length"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=X,
            dataset_expected_outputs=Y,
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


def train_mlp_models(data: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, MLP]:
    """Entraîne un MLP par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        print(f"\n> Training MLP {cf.CONFIG['model']['npl']} for category: {category}")
        X, Y = build_one_vs_all_train_arrays(data, category)

        models_per_category[category] = MLP(cf.CONFIG["model"]["npl"])
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=X,
            dataset_expected_outputs=Y,
            data_size=len(Y),  # requis par MLP.train, pas par LinearModel.train
            alpha=cf.CONFIG["model"]["alpha"],
            epochs=cf.CONFIG["model"]["epochs"],
            is_classification=True,
        )
        tb.write_training_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.2f}%")

        if "train_last_accuracy_per_category" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["train_last_accuracy_per_category"] = dict()
        cf.CONFIG["model"]["train_last_accuracy_per_category"][category] = acc_history[-1]

    return models_per_category

def train_rbf_models(data: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, RBF]:
    """Entraîne un RBF par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        print(f"\n> Training RBF ({cf.CONFIG['model']['rbf_num_centers']} centres) for category: {category}")
        X, Y = build_one_vs_all_train_arrays(data, category)

        models_per_category[category] = RBF(
            input_dim=cf.CONFIG["dataset"]["W_length"],
            num_centers=cf.CONFIG["model"]["rbf_num_centers"]
        )
        loss_history, acc_history = models_per_category[category].train(
            dataset_inputs=X,
            dataset_expected_outputs=Y,
            data_size=len(Y),
            alpha=cf.CONFIG["model"]["alpha"],
            epochs=cf.CONFIG["model"]["epochs"]
        )
        tb.write_training_logs(summary_writer, category, loss_history, acc_history)
        print(f"    Model for '{category}' trained successfully. Final Acc: {acc_history[-1]*100:.2f}%")

        if "train_last_accuracy_per_category" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["train_last_accuracy_per_category"] = dict()
        cf.CONFIG["model"]["train_last_accuracy_per_category"][category] = acc_history[-1]

    return models_per_category


def train_mlp_multiclass_model(data: dict, summary_writer: tf.summary.SummaryWriter) -> dict[str, MLP]:
    """
    Entraîne UN SEUL MLP partagé, avec une sortie par catégorie et décision finale
    par argmax (contrairement à train_mlp_models(), qui entraîne un MLP par
    catégorie en One-vs-All).

    Renvoie un dict à une seule clé (MULTICLASS_KEY) pour rester compatible avec la
    signature dict[str, Model] attendue par save_trained_models() / evaluate_models()
    (option A : pas de vrai sens One-vs-All par catégorie ici, juste un seul modèle).

    L'ordre catégorie -> index de sortie (`categories_order`, renvoyé par
    build_multiclass_train_arrays) est stocké dans cf.CONFIG["model"]["categories_order"]
    pour être réutilisé tel quel à l'évaluation et à l'inférence.
    """
    print(f"\n> Training multiclass MLP {cf.CONFIG['model']['npl']}")
    X, Y, categories_order = build_multiclass_train_arrays(data)
    n_categories = len(categories_order)

    cf.CONFIG["model"]["categories_order"] = categories_order

    model = MLP(cf.CONFIG["model"]["npl"])
    loss_history, acc_history = model.train(
        dataset_inputs=X,
        dataset_expected_outputs=Y,
        data_size=len(Y) // n_categories,  # Y est aplati (n_samples * n_categories) -> nombre de samples
        alpha=cf.CONFIG["model"]["alpha"],
        epochs=cf.CONFIG["model"]["epochs"],
        is_classification=True,
    )
    tb.write_training_logs(summary_writer, MULTICLASS_KEY, loss_history, acc_history)
    print(f"    Multiclass model trained successfully. Final Acc: {acc_history[-1]*100:.2f}%")

    cf.CONFIG["model"]["train_last_accuracy_per_category"] = {MULTICLASS_KEY: acc_history[-1]}

    return {MULTICLASS_KEY: model}


def train_models(summary_writer: tf.summary.SummaryWriter, data: dict) -> dict[str, LinearModel | MLP | RBF]:
    """Dispatch vers LinearModel, MLP (One-vs-All ou multiclasse) ou RBF selon cf.CONFIG['model']['type']."""
    model_type = cf.CONFIG["model"]["type"]

    print(f"\n[*] TensorBoard Logs directory: {cf.CONFIG['output']['logs']}")

    print(f"\n========>>> TRAINING {model_type} MODELS <<<========")
    models = dict()

    try:
        if model_type == "linear":
            models = train_linear_models(data, summary_writer)
        elif model_type == "mlp":
            models = train_mlp_models(data, summary_writer)
        elif model_type == "mlp_multiclass":
            models = train_mlp_multiclass_model(data, summary_writer)
        elif model_type == "rbf":
            models = train_rbf_models(data, summary_writer)
        else:
            raise ValueError(f"train_models(): unknown model type '{model_type}'.")

        print(f"\n========>>> TRAINING {model_type} MODELS COMPLETE <<<========")
        return models

    except Exception as e:
        summary_writer.close()
        raise e