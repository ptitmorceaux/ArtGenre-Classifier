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


def compute_binary_stats(expected: list, predicted: list, positive_value) -> dict:
    """
    Calcule les statistiques de classification binaire (ou One-vs-Rest si les valeurs
    sont des catégories parmi plusieurs) : TP/TN/FP/FN, les taux dérivés
    (TPR/TNR/FPR/FNR) et les accuracy (simple + balanced).

    `positive_value` définit ce qui compte comme "positif" dans `expected`/`predicted`
    (ex: 1 pour un modèle One-vs-All, ou le nom d'une catégorie pour un résultat
    multiclasse du type argmax).

    Réutilisée à la fois pour évaluer chaque modèle individuel (One-vs-All) et pour
    évaluer le résultat final multiclasse (One-vs-Rest, une fois par catégorie).
    """
    total = len(expected)
    if total == 0:
        raise ValueError("compute_binary_stats(): 'expected' est vide, impossible de calculer les statistiques.")

    total_expected_positives = sum(1 for e in expected if e == positive_value)
    total_expected_negatives = total - total_expected_positives

    FP = sum(1 for e, p in zip(expected, predicted) if e != positive_value and p == positive_value)
    FN = sum(1 for e, p in zip(expected, predicted) if e == positive_value and p != positive_value)
    TP = total_expected_positives - FN
    TN = total_expected_negatives - FP

    accuracy = (TP + TN) / total  # pas forcement représentatif si dataset déséquilibré

    # TPR / Recall / Sensibilité : accuracy de prédire vrai quand c'est vrai
    TPR = TP / total_expected_positives if total_expected_positives > 0 else -1
    # TNR / Spécificité : accuracy de prédire faux quand c'est faux
    TNR = TN / total_expected_negatives if total_expected_negatives > 0 else -1
    # FPR : parmi les vrais négatifs, proportion prédite à tort comme positive (= 1 - TNR)
    FPR = FP / total_expected_negatives if total_expected_negatives > 0 else -1
    # FNR : parmi les vrais positifs, proportion prédite à tort comme négative (= 1 - TPR)
    FNR = FN / total_expected_positives if total_expected_positives > 0 else -1

    # Balanced Accuracy : moyenne de TPR et TNR — traite les deux classes à poids égal,
    # contrairement à l'accuracy simple qui est dominée par la classe majoritaire.
    balanced_accuracy = -1 if TPR == -1 or TNR == -1 else (TPR + TNR) / 2

    return {
        "accuracy": accuracy,
        "balanced_accuracy": balanced_accuracy,
        "TP": TP,
        "TN": TN,
        "FP": FP,
        "FN": FN,
        "TPR": TPR,
        "TNR": TNR,
        "FPR": FPR,
        "FNR": FNR,
    }


def _print_stats(label: str, stats: dict, correct: int, total: int) -> None:
    """Affichage uniforme des statistiques, réutilisé pour les modèles individuels et le multiclasse."""
    print(f"    Accuracy for '{label}': {stats['accuracy'] * 100:.1f}% ({correct}/{total})")
    print(f"    Balanced Accuracy: {stats['balanced_accuracy'] * 100:.1f}%")
    print(f"    TPR: {stats['TPR'] * 100:.1f}% | TNR: {stats['TNR'] * 100:.1f}% | FPR: {stats['FPR'] * 100:.1f}% | FNR: {stats['FNR'] * 100:.1f}%")


def evaluate_models(models_per_category: dict, df_X: dict, df_Y: dict) -> tuple[list, list]:
    """Évalue les modèles et génère les prédictions finales par rapport aux attentes."""
    predictions = dict()

    # 1. Évaluation de chaque modèle individuel (One-vs-All), stockée dans test_accuracy
    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        print(f"\n> Evaluating model for category: {category}")

        predictions[category] = dict()
        predictions[category]["values"] = [
            _predict_scalar(models_per_category[category], x) for x in df_X["test"]
        ]
        predictions[category]["prediction"] = [tanh(value) >= 0 for value in predictions[category]["values"]]

        expected = df_Y["test"][category]
        predicted = predictions[category]["prediction"]

        stats = compute_binary_stats(expected, predicted, positive_value=1)

        if "test_accuracy" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["test_accuracy"] = dict()
        cf.CONFIG["model"]["test_accuracy"][category] = stats

        correct = sum(1 for e, p in zip(expected, predicted) if (e == 1) == p)
        _print_stats(category, stats, correct, len(expected))

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

    # 2. Évaluation du résultat final multiclasse (argmax), en One-vs-Rest par catégorie,
    #    stockée séparément dans test_accuracy_multiclass (même logique, autre positive_value).
    print(f"\n> Evaluating final multiclass result (argmax)")
    cf.CONFIG["model"]["test_accuracy_multiclass"] = dict()

    for category in cf.CONFIG["dataset"]["categories"]["train"].keys():
        stats = compute_binary_stats(df_predictions_expected, df_predictions_test, positive_value=category)
        cf.CONFIG["model"]["test_accuracy_multiclass"][category] = stats

        correct = sum(1 for e, p in zip(df_predictions_expected, df_predictions_test) if (e == category) == (p == category))
        print(f"\n  > Category: {category}")
        _print_stats(category, stats, correct, len(df_predictions_expected))

    # Accuracy globale "brute" (exact match toutes catégories confondues) : une seule
    # valeur, pas de TP/TN/FP/FN pertinent ici puisque ce n'est pas du binaire.
    correct_predictions = sum(1 for expected, predicted in zip(df_predictions_expected, df_predictions_test) if expected == predicted)
    total_predictions = len(df_predictions_expected)
    accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
    cf.CONFIG["model"]["test_accuracy_multiclass"]["global"] = accuracy
    print(f"\n  > Global Accuracy (exact match): {accuracy * 100:.1f}% ({correct_predictions}/{total_predictions})")

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
