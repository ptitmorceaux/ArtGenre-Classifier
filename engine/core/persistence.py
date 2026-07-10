import os
import json
from datetime import datetime

import engine.core.config as cf
from engine.interop.storage import Storage
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP
from engine.interop.normalization import StandardScaler, StandardPerColumnScaler

def save_trained_models(
        models_per_category: dict[str, LinearModel | MLP],
        scaler: StandardScaler | StandardPerColumnScaler,
        output_folder: str,
        model_type: str
    ) -> None:
    
    os.makedirs(output_folder, exist_ok=True)

    for category, model in models_per_category.items():
        filename = f"{model_type}__{category}__{date}.bin"
        filepath = os.path.join(output_folder, filename)

        if os.path.isfile(filepath):
            os.remove(filepath)

        Storage["save"](model, scaler, output_folder, filename)
        print(f"[*] Modèle '{category}' sauvegardé : {filepath}")
        if "saved_models" not in cf.CONFIG["model"].keys():
            cf.CONFIG["model"]["saved_models"] = dict()
        cf.CONFIG["model"]["saved_models"][category] = filepath


def save_config_json(output_folder: str, config: dict) -> None:
    """Sauvegarde la configuration dans un fichier JSON."""
    os.makedirs(output_folder, exist_ok=True)
    filepath = os.path.join(output_folder, "config.json")
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)
    print(f"[*] Configuration sauvegardée : {filepath}")
    