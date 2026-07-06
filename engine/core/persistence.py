import os

from engine.interop.storage import Storage
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP
from engine.interop.normalization import StandardScaler, StandardPerColumnScaler


def save_trained_models(
        models_per_category: dict[str, LinearModel | MLP],
        scaler: StandardScaler | StandardPerColumnScaler,
        output_folder: str
    ) -> None:
    """Sauvegarde chaque modèle entraîné (un par catégorie) avec le scaler partagé utilisé pour l'entraînement."""
    os.makedirs(output_folder, exist_ok=True)

    for category, model in models_per_category.items():
        filename = f"{category}.bin"
        filepath = os.path.join(output_folder, filename)

        # On écrase l'ancien modèle si le script est relancé (Storage refuse
        # sinon d'écrire par-dessus un fichier existant).
        if os.path.isfile(filepath):
            os.remove(filepath)

        Storage["save"](model, scaler, output_folder, filename)
        print(f"Modèle '{category}' sauvegardé : {filepath}")