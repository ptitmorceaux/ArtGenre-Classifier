import ctypes
import numpy as np


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

        return cls(mean, std)

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Normalise les données X en utilisant la moyenne et l'écart type."""
        if self.mean is None or self.std is None:
            raise ValueError("StandardScaler.transform(): scaler is not initialized.")
        return (X - self.mean) / self.std


class _CStandardPerColumnScaler(ctypes.Structure):
    _fields_ = [
        ("method", ctypes.c_int),
        ("mean", ctypes.POINTER(ctypes.c_float)),
        ("std", ctypes.POINTER(ctypes.c_float)),
        ("length", ctypes.c_uint32)
    ]

class StandardPerColumnScaler:
    """Classe pour la normalisation des données par colonne en utilisant la méthode StandardScaler."""
    
    def __init__(self, mean: None | list[float], std: None | list[float]):
        self.length = len(mean) if mean is not None else 0
        self.mean = mean
        self.std = std
    
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

        return cls(mean, std)

    def transform(self, X: list[float] | np.ndarray) -> np.ndarray:
        """Normalise les données X par colonne en utilisant la moyenne et l'écart type."""
        self.length = len(self.mean) if self.mean is not None else 0

        if not isinstance(X, np.ndarray):
            X = np.array(X, dtype=np.float32)
        
        if self.mean is None or self.std is None:
            raise ValueError("StandardPerColumnScaler.transform(): scaler is not initialized.")
        
        if len(self.mean) != len(self.std):
            raise ValueError("StandardPerColumnScaler.transform(): mean and std must have the same length.")
        
        if self.length != X.shape[1]:
            raise ValueError(f"StandardPerColumnScaler.transform(): scaler length ({self.length}) does not match input data shape ({X.shape[1]}).")
        
        return (X - self.mean) / self.std