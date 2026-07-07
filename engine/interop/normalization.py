import ctypes
import numpy as np
from engine.interop.loader import Loader


def compute_mean_std(values: list[float] | np.ndarray) -> tuple[float, float]:
    """Calcule la moyenne et l'écart-type (population) d'une liste/array de floats."""
    arr = np.asarray(values, dtype=np.float64)
    if arr.size == 0:
        raise ValueError("compute_mean_std(): le tableau ne peut pas être vide.")
    return float(arr.mean()), float(arr.std())


def normalize_list(values: list[float] | np.ndarray, mean: float, std: float) -> list[float]:
    """Normalise un tableau de floats : (x - mean) / std pour chaque x."""
    if std == 0:
        raise ValueError("normalize_list(): std ne peut pas être égal à 0 (division par zéro).")
    arr = np.asarray(values, dtype=np.float64)
    return ((arr - mean) / std).astype(np.float32).tolist()


def normalize_by_columns(
        values_flat: list[float] | np.ndarray,
        mean_per_column: list[float],
        std_per_column: list[float]
    ) -> list[float]:
    """
    TRANSFORM : applique un mean/std PAR COLONNE déjà connus (calculés au préalable,
    typiquement sur le train) à un tableau aplati organisé en groupes de N valeurs
    (N = nombre de colonnes, ex: 3 pour r,g,b,r,g,b,...).

    Ne recalcule JAMAIS mean/std à partir de `values_flat` : c'est fait exprès,
    pour pouvoir appliquer les stats du train sur le test sans fuite de données.
    """
    n_columns = len(mean_per_column)
    if len(std_per_column) != n_columns:
        raise ValueError("normalize_by_columns(): mean et std doivent avoir la même longueur.")

    arr = np.asarray(values_flat, dtype=np.float64)
    if arr.size % n_columns != 0:
        raise ValueError(
            f"normalize_by_columns(): la longueur ({arr.size}) doit être un multiple "
            f"du nombre de colonnes ({n_columns})."
        )

    means = np.asarray(mean_per_column, dtype=np.float64)
    stds = np.asarray(std_per_column, dtype=np.float64)
    if np.any(stds == 0):
        raise ValueError("normalize_by_columns(): un std est nul (division par zéro).")

    rows = arr.reshape(-1, n_columns)          # chaque LIGNE = un pixel, chaque COLONNE = un canal
    normalized = (rows - means) / stds         # broadcasting numpy sur les colonnes
    return normalized.flatten().astype(np.float32).tolist()


def fit_and_normalize_by_columns(
        values_flat: list[float] | np.ndarray,
        n_columns: int
    ) -> tuple[list[float], list[float], list[float]]:
    """
    FIT + TRANSFORM : calcule mean/std PAR COLONNE sur un tableau aplati (ex: tous les
    pixels du train, format r,g,b,r,g,b,...), puis normalise ce même tableau.

    À utiliser UNIQUEMENT sur le train (jamais sur le test, sinon fuite de données) :
    le test doit être normalisé avec normalize_by_columns() + les mean/std du train.

    Renvoie (valeurs_normalisées, mean_par_colonne, std_par_colonne).
    """
    arr = np.asarray(values_flat, dtype=np.float64)
    if arr.size % n_columns != 0:
        raise ValueError(
            f"fit_and_normalize_by_columns(): la longueur ({arr.size}) doit être un multiple "
            f"du nombre de colonnes ({n_columns})."
        )

    rows = arr.reshape(-1, n_columns)
    means = rows.mean(axis=0).astype(np.float32).tolist()
    stds = rows.std(axis=0).astype(np.float32).tolist()

    normalized = normalize_by_columns(values_flat, means, stds)

    return normalized, means, stds


class _CStandardScaler(ctypes.Structure):
    _fields_ = [
        ("method", ctypes.c_int),
        ("mean", ctypes.c_float),
        ("std", ctypes.c_float)        
    ]

class StandardScaler:
    """Classe pour la normalisation des données en utilisant la méthode StandardScaler."""
    
    def __init__(self, mean: None | float, std: None | float):
        self.mean = mean
        self.std = std
    
    @classmethod
    def from_data(cls, data: list[float] | np.ndarray) -> "StandardScaler":
        """Crée un StandardScaler à partir d'une liste/array de données (FIT)."""
        mean, std = compute_mean_std(data)
        return cls(mean, std)
    
    @classmethod
    def _init_from_normalization_ptr(cls, normalization_ptr: ctypes.c_void_p) -> "StandardScaler":
        """
        Initialise un StandardScaler à partir d'un pointeur vers une structure C.
        """
        if normalization_ptr is None or normalization_ptr.value is None:
            raise ValueError("StandardScaler._init_from_normalization_ptr(): normalization pointer is not initialized.")
        
        normalization_struct = ctypes.cast(
            normalization_ptr,
            ctypes.POINTER(_CStandardScaler)
        ).contents

        mean = normalization_struct.mean
        std = normalization_struct.std

        StandardScaler._free(normalization_ptr)

        return cls(mean, std)
    
    @staticmethod
    def _free(normalization_ptr: ctypes.c_void_p):
        """Libère la mémoire allouée pour le scaler."""
        if normalization_ptr is not None and normalization_ptr.value is not None:
            Loader.call(
                "free_StandardNormalizationData",
                ctypes.byref(normalization_ptr),
                prefix_errmsg="StandardScaler.free()"
            )

    def transform(self, X: np.ndarray | list[float]) -> list[float]:
        """TRANSFORM : normalise X avec le mean/std déjà connus du scaler (pas recalculés)."""
        if self.mean is None or self.std is None:
            raise ValueError("StandardScaler.transform(): scaler is not initialized.")
        return normalize_list(X, self.mean, self.std)


class _CStandardPerColumnScaler(ctypes.Structure):
    _fields_ = [
        ("method", ctypes.c_int),
        ("mean", ctypes.POINTER(ctypes.c_float)),
        ("std", ctypes.POINTER(ctypes.c_float)),
        ("length", ctypes.c_uint32)
    ]

class StandardPerColumnScaler:
    """Classe pour la normalisation des données par colonne (ex: canaux r,g,b)."""
    
    def __init__(self, mean: None | list[float], std: None | list[float]):
        self.length = len(mean) if mean is not None else 0
        self.mean = mean
        self.std = std

    @classmethod
    def from_data(cls, values_flat: list[float] | np.ndarray, n_columns: int) -> "StandardPerColumnScaler":
        """
        Crée un StandardPerColumnScaler à partir d'un dataset aplati (FIT).
        À utiliser uniquement sur le train.
        """
        _, means, stds = fit_and_normalize_by_columns(values_flat, n_columns)
        return cls(means, stds)

    @classmethod
    def _init_from_normalization_ptr(cls, normalization_ptr: ctypes.c_void_p) -> "StandardPerColumnScaler":
        """
        Initialise un StandardPerColumnScaler à partir d'un pointeur vers une structure C.
        """
        if normalization_ptr is None or normalization_ptr.value is None:
            raise ValueError("StandardPerColumnScaler._init_from_normalization_ptr(): normalization pointer is not initialized.")
        
        normalization_struct = ctypes.cast(
            normalization_ptr,
            ctypes.POINTER(_CStandardPerColumnScaler)
        ).contents

        length = normalization_struct.length
        mean = list(normalization_struct.mean[:length])
        std = list(normalization_struct.std[:length])

        StandardPerColumnScaler._free(normalization_ptr)
        
        return cls(mean, std)

    @staticmethod
    def _free(normalization_ptr: ctypes.c_void_p):
        """Libère la mémoire allouée pour le scaler."""
        if normalization_ptr is not None and normalization_ptr.value is not None:
            Loader.call(
                "free_StandardPerColumnNormalizationData",
                ctypes.byref(normalization_ptr),
                prefix_errmsg="StandardPerColumnScaler.free()"
            )

    def transform(self, X: list[float] | np.ndarray) -> list[float]:
        """TRANSFORM : normalise X par colonne avec le mean/std déjà connus (pas recalculés)."""
        if self.mean is None or self.std is None:
            raise ValueError("StandardPerColumnScaler.transform(): scaler is not initialized.")

        if len(self.mean) != len(self.std):
            raise ValueError("StandardPerColumnScaler.transform(): mean and std must have the same length.")

        self.length = len(self.mean)
        return normalize_by_columns(X, self.mean, self.std)
