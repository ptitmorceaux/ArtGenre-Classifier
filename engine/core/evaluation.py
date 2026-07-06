from math import tanh
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

from engine.core.config import CONFIG, CATEGORIES


def evaluate_models(models_per_category: dict, df_X: dict, df_Y: dict) -> tuple[list, list]:
    """Évalue les modèles et génère les prédictions finales par rapport aux attentes."""
    predictions = dict()

    for category in CATEGORIES:
        print(f"Evaluating model for category: {category}")

        predictions[category] = dict()
        predictions[category]["values"] = [
            models_per_category[category].predict(x, is_classification=False) for x in df_X["test"]
        ]
        predictions[category]["prediction"] = [tanh(value) >= 0 for value in predictions[category]["values"]]

    # Détermination de la catégorie prédite (Argmax de la valeur de sortie ou "unknown")
    df_predictions_test = list()
    first_cat = list(CATEGORIES.keys())[0]

    for i in range(len(predictions[first_cat]["prediction"])):
        category_predicted = max(CATEGORIES.keys(), key=lambda c: predictions[c]["values"][i])

        if predictions[category_predicted]["prediction"][i]:
            df_predictions_test.append(category_predicted)
        else:
            df_predictions_test.append(CONFIG["global"]["unknown_category"])

    # Détermination de la catégorie attendue
    df_predictions_expected = []
    for i in range(len(df_Y["test"][first_cat])):
        category_expected = next((c for c in CATEGORIES if df_Y["test"][c][i] == 1), None)
        df_predictions_expected.append(category_expected)

    return df_predictions_expected, df_predictions_test


def plot_confusion_matrix(df_predictions_expected: list, df_predictions_test: list, df_X: dict) -> None:
    """Génère et affiche la matrice de confusion."""
    ConfusionMatrixDisplay.from_predictions(
        df_predictions_expected,
        df_predictions_test,
        labels=list(CATEGORIES.keys()) + [CONFIG["global"]["unknown_category"]],
        cmap="Blues",
        xticks_rotation=45
    )

    length_X_test = len(df_X["test"])
    length_X_train = CONFIG["dataset"]["count_total_dataset"]["total"] - length_X_test

    plt.title("Matrix de Confusion")
    plt.suptitle(
        f"Seed: {CONFIG['lib']['seed']} | "
        f"Model: Classification Linéaire | "
        f"Alpha: {CONFIG['model']['alpha']} | "
        f"Epochs: {CONFIG['model']['epochs']}\n\n"
        f"Dataset: {length_X_train} train, {length_X_test} test "
        f"(total = {CONFIG['dataset']['count_total_dataset']['total']}, "
        f"{CONFIG['dataset']['train_test_split_ratio'] * 100}% ratio)",
        fontsize=10,
        y=1.02
    )

    plt.tight_layout()
    plt.show()