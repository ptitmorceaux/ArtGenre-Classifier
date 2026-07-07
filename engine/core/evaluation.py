from math import tanh
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from engine.core.config import CONFIG, CATEGORIES

def _predict_scalar(model, x) -> float:
    """
    Renvoie la sortie scalaire du modèle, quel que soit son type.
    LinearModel.predict() renvoie un scalaire, MLP.predict() renvoie une liste
    (même à une seule sortie) — sans ce helper, tanh(value) planterait sur un MLP.
    """
    output = model.predict(x, is_classification=False)
    return output[0] if isinstance(output, list) else output


def evaluate_models(models_per_category: dict, df_X: dict, df_Y: dict) -> tuple[list, list]:
    """Évalue les modèles et génère les prédictions finales par rapport aux attentes."""
    predictions = dict()

    for category in CATEGORIES:
        print(f"Evaluating model for category: {category}")

        predictions[category] = dict()
        predictions[category]["values"] = [
            _predict_scalar(models_per_category[category], x) for x in df_X["test"]
        ]
        predictions[category]["prediction"] = [tanh(value) >= 0 for value in predictions[category]["values"]]

    # Détermination de la catégorie prédite (Argmax de la valeur de sortie ou "unknown")
    df_predictions_test = list()
    first_cat = list(CATEGORIES.keys())[0]

    for i in range(len(predictions[first_cat]["prediction"])):
        category_predicted = max(CATEGORIES.keys(), key=lambda c: predictions[c]["values"][i])

        unknown_is_valid = CONFIG["global"]["unknown_category"] is not None and CONFIG["global"]["unknown_category"] != ""

        if unknown_is_valid and not predictions[category_predicted]["prediction"][i]:
            df_predictions_test.append(CONFIG["global"]["unknown_category"])
        else:
            df_predictions_test.append(category_predicted)

    # Détermination de la catégorie attendue
    df_predictions_expected = []
    for i in range(len(df_Y["test"][first_cat])):
        category_expected = next((c for c in CATEGORIES if df_Y["test"][c][i] == 1), None)
        df_predictions_expected.append(category_expected)

    return df_predictions_expected, df_predictions_test


def plot_confusion_matrix(df_predictions_expected: list, df_predictions_test: list, df_X: dict) -> None:
    """Génère et affiche la matrice de confusion."""
    
    fig, ax = plt.subplots(figsize=(10, 5.5))

    labels = list(CATEGORIES.keys())
    if CONFIG["global"]["unknown_category"] is not None and CONFIG["global"]["unknown_category"] != "":
        labels.append(CONFIG["global"]["unknown_category"])

    ConfusionMatrixDisplay.from_predictions(
        df_predictions_expected,
        df_predictions_test,
        labels=labels,
        cmap="Blues",
        xticks_rotation=45,
        ax=ax
    )

    length_X_test = len(df_X["test"])
    length_X_train = CONFIG["dataset"]["count_total_dataset"]["total"] - length_X_test

    plt.title("Confusion Matrix")

    plt.suptitle(
        f"Model: {CONFIG['model']['type']} | Norm: {CONFIG['dataset']['normalization_method']} | Seed: {CONFIG['lib']['seed']}\n"
        f"Alpha: {CONFIG['model']['alpha']} | Epochs: {CONFIG['model']['epochs']}\n"
        f"Train: {length_X_train}, Test: {length_X_test}",
        fontsize=9,
        y=0.95
    )

    plt.subplots_adjust(top=0.82, bottom=0.12)
    plt.show()

if __name__ == "__main__":

    sample_df_X = {
        "train": [[0.1, 0.2, 0.3],
                  [0.4, 0.5, 0.6]],
        "test": [[0.7, 0.8, 0.9]]
    }
    sample_df_Y = {
        "train": {
            "impressionism": [1, 0],
            "realism": [0, 1],
            "romanticism": [0, 0]
        },
        "test": {
            "impressionism": [0],
            "realism": [1],
            "romanticism": [0]
        }
    }
    sample_df_predictions_expected = ["impressionism", "realism"]
    sample_df_predictions_test = ["impressionism", "realism"]
    CONFIG["dataset"]["count_total_dataset"] = {"total": 3}
    plot_confusion_matrix(sample_df_predictions_expected, sample_df_predictions_test, sample_df_X)