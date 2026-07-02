import numpy as np


class StandardScaler:
    """Classe pour la normalisation des données en utilisant la méthode StandardScaler."""
    
    def __init__(self, mean: None | float, std: None | float):
        self.mean = mean
        self.std = std

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Normalise les données X en utilisant la moyenne et l'écart type."""
        if self.mean is None or self.std is None:
            raise ValueError("StandardScaler.transform(): scaler is not initialized.")
        return (X - self.mean) / self.std


class StandardPerColumnScaler:
    """Classe pour la normalisation des données par colonne en utilisant la méthode StandardScaler."""
    
    def __init__(self, mean: None | np.ndarray, std: None | np.ndarray):
        self.length = len(mean) if mean is not None else 0
        self.mean = mean
        self.std = std

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