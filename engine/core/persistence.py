import os

from engine.core.config import CONFIG
from engine.interop.storage import Storage
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP
from engine.interop.normalization import StandardScaler, StandardPerColumnScaler

def save_trained_models(
        models_per_category: dict[str, LinearModel | MLP],
        scaler: StandardScaler | StandardPerColumnScaler,
        output_folder: str,
        session_id: str
    ) -> None:
    
    os.makedirs(output_folder, exist_ok=True)

    for category, model in models_per_category.items():
        filename = f"{CONFIG['model']['type']}__{category}__{session_id}.bin"
        filepath = os.path.join(output_folder, filename)

        if os.path.isfile(filepath):
            os.remove(filepath)

        Storage["save"](model, scaler, output_folder, filename)
        print(f"Modèle '{category}' sauvegardé : {filepath}")
