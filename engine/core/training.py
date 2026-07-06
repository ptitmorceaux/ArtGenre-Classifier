from engine.core.config import CONFIG, CATEGORIES
from engine.interop.linearModel import LinearModel


def train_models(df_X: dict, df_Y: dict) -> dict[str, LinearModel]:
    """Entraîne un modèle linéaire par catégorie (One-vs-All)."""
    models_per_category = dict()

    for category in CATEGORIES:
        print(f"Training model for category: {category}")
        models_per_category[category] = LinearModel.init_random(input_dim=CONFIG["dataset"]["W_length"])
        models_per_category[category].train(
            dataset_inputs=df_X["train"],
            dataset_expected_outputs=df_Y["train"][category],
            is_classification=True,
            alpha=CONFIG["model"]["alpha"],
            epochs=CONFIG["model"]["epochs"]
        )
        print(f"Model for category '{category}' trained successfully.\n")

    return models_per_category