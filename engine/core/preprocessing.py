import numpy as np

import engine.core.config as cf
from engine.interop.normalization import (
    StandardScaler,
    StandardPerColumnScaler,
    fit_and_normalize_by_columns,
)


def standardize_test_data_from_scaler(data: dict, scaler: StandardScaler | StandardPerColumnScaler) -> dict:
    """Applique la normalisation du train (déjà fit) sur les images de test, par catégorie."""
    for category, imgs in data["test"]["img"].items():
        data["test"]["img"][category] = np.array([scaler.transform(row) for row in imgs])
    return data


def standard_scaler(data: dict) -> tuple[dict, StandardScaler]:
    """Standardisation GLOBALE : FIT sur tout le train (toutes catégories confondues)."""
    all_train = np.concatenate(list(data["train"]["img"].values()), axis=0)
    scaler = StandardScaler.from_data(all_train.flatten())

    for category, imgs in data["train"]["img"].items():
        data["train"]["img"][category] = np.array([scaler.transform(row) for row in imgs])

    return data, scaler


def standard_column_scaler(data: dict) -> tuple[dict, StandardPerColumnScaler]:
    """Standardisation PAR CANAL : FIT sur tout le train, TRANSFORM catégorie par catégorie."""
    all_train = np.concatenate(list(data["train"]["img"].values()), axis=0)
    
    # --- ANCIEN CODE (RGB = 3 canaux) ---
    # _, means, stds = fit_and_normalize_by_columns(all_train.flatten(), n_columns=3)
    _, means, stds = fit_and_normalize_by_columns(all_train.flatten(), n_columns=1)
    
    scaler = StandardPerColumnScaler(mean=means, std=stds)

    for category, imgs in data["train"]["img"].items():
        data["train"]["img"][category] = np.array([scaler.transform(row) for row in imgs])

    return data, scaler


def standardize_train_data(data: dict) -> tuple[dict, StandardScaler | StandardPerColumnScaler]:
    method = cf.CONFIG["dataset"]["normalization_method"]
    if method == "standard":
        return standard_scaler(data)
    elif method == "per_column":
        return standard_column_scaler(data)
    else:
        raise ValueError(f"standardize_train_data(): unknown normalization_method '{method}'.")