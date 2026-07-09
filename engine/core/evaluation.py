from math import tanh
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import engine.core.config as cf

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

    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        print(f"\n> Evaluating model for category: {category}")

        predictions[category] = dict()
        predictions[category]["values"] = [
            _predict_scalar(models_per_category[category], x) for x in df_X["test"]
        ]
        predictions[category]["prediction"] = [tanh(value) >= 0 for value in predictions[category]["values"]]

        # Calcul de l'accuracy par catégorie
        predicted_values = [pred >= 0 for pred in predictions[category]["values"]]
        expected_values = [expected >= 0 for expected in df_Y["test"][category]]
        correct_predictions = sum(1 for expected, predicted in zip(expected_values, predicted_values) if (predicted and expected) or (not predicted and not expected))
        total_predictions = len(df_Y["test"][category])

        if total_predictions == 0:
            raise ValueError(f"No test samples for category '{category}'. Cannot compute accuracy.")
        
        accuracy = correct_predictions / total_predictions

        total_expected_positives = sum(1 for expected in df_Y["test"][category] if expected == 1)
        total_expected_negatives = total_predictions - total_expected_positives
            
        FP = sum(1 for expected, predicted in zip(df_Y["test"][category], predictions[category]["prediction"]) if expected != 1 and predicted == 1)
        FN = sum(1 for expected, predicted in zip(df_Y["test"][category], predictions[category]["prediction"]) if expected == 1 and predicted != 1)
        TP = total_expected_positives - FN
        TN = total_expected_negatives - FP

        # TPR / Recall / Sensibilité : accuracy de prédire vrai quand c'est vrai
        if total_expected_positives == 0:
            print(f"    No positive samples for category '{category}'. TPR is undefined.")
        TPR = TP / total_expected_positives if total_expected_positives > 0 else -1

        # TNR / Spécificité : accuracy de prédire faux quand c'est faux
        if total_expected_negatives == 0:
            print(f"    No negative samples for category '{category}'. TNR is undefined.")
        TNR = TN / total_expected_negatives if total_expected_negatives > 0 else -1

        # FPR : parmi les vrais négatifs, proportion prédite à tort comme positive (= 1 - TNR)
        FPR = FP / total_expected_negatives if total_expected_negatives > 0 else -1
        # FNR : parmi les vrais positifs, proportion prédite à tort comme négative (= 1 - TPR)
        FNR = FN / total_expected_positives if total_expected_positives > 0 else -1

        # Balanced Accuracy : moyenne de TPR et TNR — traite les deux classes à poids égal,
        # contrairement à l'accuracy simple qui est dominée par la classe majoritaire (négative).
        balanced_accuracy = -1 if TPR == -1 or TNR == -1 else (TPR + TNR) / 2

        if "test_accuracy" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["test_accuracy"] = dict()

        cf.CONFIG["model"]["test_accuracy"][category] = {
            "accuracy": accuracy, # pas forcement représentatif si dataset déséquilibré (ex: 95% de négatifs, 5% de positifs => accuracy = 95% même si le modèle ne prédit jamais de positifs)
            "balanced_accuracy": balanced_accuracy, # mieux pour dataset déséquilibré
            "TP": TP,
            "TN": TN,
            "FP": FP,
            "FN": FN,
            "TPR": TPR,
            "TNR": TNR,
            "FPR": FPR,
            "FNR": FNR,
        }

        print(f"    Accuracy for '{category}': {accuracy * 100:.1f}% ({correct_predictions}/{total_predictions})")
        print(f"    Balanced Accuracy: {balanced_accuracy * 100:.1f}%")
        # print(f"    TP: {TP} | TN: {TN} | FP: {FP} | FN: {FN}")
        print(f"    TPR: {TPR * 100:.1f}% | TNR: {TNR * 100:.1f}% | FPR: {FPR * 100:.1f}% | FNR: {FNR * 100:.1f}%")

    # Détermination de la catégorie prédite (Argmax de la valeur de sortie ou "unknown")
    df_predictions_test = list()
    first_cat = list(cf.CONFIG["dataset"]["categories"]["train"].keys())[0]

    for i in range(len(predictions[first_cat]["prediction"])):
        category_predicted = max(cf.CONFIG["dataset"]["categories"]["train"].keys(), key=lambda c: predictions[c]["values"][i])

        unknown_is_valid = cf.CONFIG["global"]["unknown_category"] is not None and cf.CONFIG["global"]["unknown_category"] != ""

        if unknown_is_valid and not predictions[category_predicted]["prediction"][i]:
            df_predictions_test.append(cf.CONFIG["global"]["unknown_category"])
        else:
            df_predictions_test.append(category_predicted)

    # Détermination de la catégorie attendue
    df_predictions_expected = []
    for i in range(len(df_Y["test"][first_cat])):
        category_expected = next((c for c in cf.CONFIG["dataset"]["categories"]["train"].keys() if df_Y["test"][c][i] == 1), None)
        df_predictions_expected.append(category_expected)
    
    # Calcul de l'accuracy globale
    correct_predictions = sum(1 for expected, predicted in zip(df_predictions_expected, df_predictions_test) if expected == predicted)
    total_predictions = len(df_predictions_expected)
    accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
    print(f"\n>>> Global Accuracy: {accuracy * 100:.4f}% ({correct_predictions}/{total_predictions})\n")

    return df_predictions_expected, df_predictions_test


def plot_confusion_matrix(df_predictions_expected: list, df_predictions_test: list, df_X: dict, show: bool = True) -> None:
    """Génère et affiche la matrice de confusion."""
    
    fig, ax = plt.subplots(figsize=(10, 5.5))

    labels = list(cf.CONFIG["dataset"]["categories"]["train"].keys())
    if cf.CONFIG["global"]["unknown_category"] is not None and cf.CONFIG["global"]["unknown_category"] != "":
        labels.append(cf.CONFIG["global"]["unknown_category"])

    ConfusionMatrixDisplay.from_predictions(
        df_predictions_expected,
        df_predictions_test,
        labels=labels,
        cmap="Blues",
        xticks_rotation=45,
        ax=ax
    )

    length_X_test = cf.CONFIG["dataset"]["count_total_dataset"]["test"]["total"]
    length_X_train = cf.CONFIG["dataset"]["count_total_dataset"]["train"]["total"]

    plt.title("Confusion Matrix")

    plt.suptitle(
        f"Model: {cf.CONFIG['model']['type']} | Norm: {cf.CONFIG['dataset']['normalization_method']} | Seed: {cf.CONFIG['lib']['seed']}\n"
        f"Alpha: {cf.CONFIG['model']['alpha']} | Epochs: {cf.CONFIG['model']['epochs']}\n"
        f"Train: {length_X_train}, Test: {length_X_test}",
        fontsize=9,
        y=0.95
    )

    plt.subplots_adjust(top=0.82, bottom=0.12)

    cf.CONFIG["output"]["confusion_matrix_test"] = os.path.join(cf.CONFIG["output"]["logs"], "confusion_matrix_test.png")
    plt.savefig(cf.CONFIG["output"]["confusion_matrix_test"], dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[*] Confusion matrix saved to: {cf.CONFIG['output']['confusion_matrix_test']}")
    if show:
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
    cf.CONFIG["dataset"]["count_total_dataset"] = {
        "test": {"total": "N/A"},
        "train": {"total": "N/A"}
    }
    plot_confusion_matrix(sample_df_predictions_expected, sample_df_predictions_test, sample_df_X)