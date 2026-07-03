import ctypes
import numpy as np


class _CStandardScaler:
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

        mean = normalization_struct.mean.value
        std = normalization_struct.std.value

        return cls(mean, std)

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Normalise les données X en utilisant la moyenne et l'écart type."""
        if self.mean is None or self.std is None:
            raise ValueError("StandardScaler.transform(): scaler is not initialized.")
        return (X - self.mean) / self.std


class _CStandardPerColumnScaler:
    __fields__ = [
        ("method", ctypes.c_int),
        ("mean", ctypes.POINTER(ctypes.c_float)),
        ("std", ctypes.POINTER(ctypes.c_float)),
        ("length", ctypes.c_uint32)
    ]

class StandardPerColumnScaler:
    """Classe pour la normalisation des données par colonne en utilisant la méthode StandardScaler."""
    
    def __init__(self, mean: None | np.ndarray, std: None | np.ndarray):
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

        length = normalization_struct.length.value
        mean = np.ctypeslib.as_array(normalization_struct.mean, shape=(length,))
        std = np.ctypeslib.as_array(normalization_struct.std, shape=(length,))

        return cls(mean, std)

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Normalise les données X par colonne en utilisant la moyenne et l'écart type."""
        self.length = len(self.mean) if self.mean is not None else 0
        
        if self.mean is None or self.std is None:
            raise ValueError("StandardPerColumnScaler.transform(): scaler is not initialized.")
        
        if len(self.mean) != len(self.std):
            raise ValueError("StandardPerColumnScaler.transform(): mean and std must have the same length.")
        
        if self.length != X.shape[1]:
            raise ValueError(f"StandardPerColumnScaler.transform(): scaler length ({self.length}) does not match input data shape ({X.shape[1]}).")
        
        return (X - self.mean) / self.std