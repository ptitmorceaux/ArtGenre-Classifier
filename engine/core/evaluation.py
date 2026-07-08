import os
import sys
import matplotlib.pyplot as plt

from sklearn.metrics import ConfusionMatrixDisplay
from math import tanh
from engine.core.config import CONFIG, CATEGORIES

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

def _predict_scalar(model, x) -> float:
    output = model.predict(x, is_classification=False)
    return output[0] if isinstance(output, list) else output

def evaluate_models(models_per_category: dict, df_X: dict, df_Y: dict) -> tuple[list, list, float]:
    predictions = dict()

    for category in CATEGORIES:
        print(f"Evaluating model for category: {category}")
        predictions[category] = dict()
        predictions[category]["values"] = [
            _predict_scalar(models_per_category[category], x) for x in df_X["test"]
        ]
        predictions[category]["prediction"] = [tanh(value) >= 0 for value in predictions[category]["values"]]

    df_predictions_test = list()
    first_cat = list(CATEGORIES.keys())[0]

    for i in range(len(predictions[first_cat]["prediction"])):
        category_predicted = max(CATEGORIES.keys(), key=lambda c: predictions[c]["values"][i])
        unknown_is_valid = CONFIG["global"]["unknown_category"] is not None and CONFIG["global"]["unknown_category"] != ""

        if unknown_is_valid and not predictions[category_predicted]["prediction"][i]:
            df_predictions_test.append(CONFIG["global"]["unknown_category"])
        else:
            df_predictions_test.append(category_predicted)

    df_predictions_expected = []
    for i in range(len(df_Y["test"][first_cat])):
        category_expected = next((c for c in CATEGORIES if df_Y["test"][c][i] == 1), None)
        df_predictions_expected.append(category_expected)

    # CALCUL ACCURACY GLOB
    correct = sum(1 for e, t in zip(df_predictions_expected, df_predictions_test) if e == t)
    global_accuracy = correct / len(df_predictions_expected) if len(df_predictions_expected) > 0 else 0
    print(f"[*] Précision (Accuracy) sur le Test Set : {global_accuracy * 100:.2f}%")

    return df_predictions_expected, df_predictions_test, global_accuracy

def plot_confusion_matrix(df_predictions_expected: list, df_predictions_test: list, df_X: dict, session_id: str) -> str:
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
        f"Model: {CONFIG['model']['type']} | Norm: {CONFIG['dataset']['normalization_method']} | Session: {session_id}\n"
        f"Alpha: {CONFIG['model']['alpha']} | Epochs: {CONFIG['model']['epochs']}\n"
        f"Train: {length_X_train}, Test: {length_X_test}",
        fontsize=9,
        y=0.95
    )
    plt.subplots_adjust(top=0.82, bottom=0.12)

    # SAUVEGARDE DE LA MATRICE
    metrics_dir = os.path.join(CONFIG["output"]["outdir"], "metrics", session_id)
    os.makedirs(metrics_dir, exist_ok=True)
    
    filename = "confusion_matrix.png"
    filepath = os.path.join(metrics_dir, filename)
    plt.savefig(filepath, bbox_inches='tight')
    plt.close()
    return filename
