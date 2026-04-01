import ctypes
from typing import Type
from engine.interop.loader import Loader


class LinearModel:
    """
    Wrapper Python pour LinearModel en C.
    Cette classe permet de gérer le pointeur mémoire côté C.
    """

    @staticmethod
    def _check_range(value, ctype: Type[ctypes._SimpleCData], prefix_errmsg: str) -> None:
        Loader.check_primitive_values_range(value, ctype=ctype, prefix_errmsg=prefix_errmsg)  # type: ignore[arg-type]

    def __init__(self, input_dim: int):
        LinearModel._check_range(input_dim, ctypes.c_uint32, "LinearModel.__init__()")
        if input_dim == 0:
            raise ValueError("LinearModel.__init__(): `input_dim` must be > 0")

        self.input_dim = input_dim
        # On crée un pointeur vide (void*) qui recevra l'adresse du modèle C.
        self.ptr = ctypes.c_void_p()

        Loader.call(
            "create_linear_model",
            ctypes.c_uint32(input_dim),
            ctypes.byref(self.ptr),
            prefix_errmsg="LinearModel.__init__()"
        )
    
    def close(self):
        """"Libère la mémoire allouée pour le modèle C."""
        if self.ptr.value is not None and self.ptr is not None: 
            Loader.call(
                "free_linear_model",
                ctypes.byref(self.ptr),
                prefix_errmsg="LinearModel.close()"
            )

    def predict_regression(self, input_data: list[float]) -> float:
        """"Prédit une valeur continue pour un vecteur d'entrée de données."""
        Loader.call(
            "predict_regressions",
            self.ptr,
            prefix_errmsg="LinearModel.predict_regression()"
        )
        return float()

    def predict_classification(self, input_data: list[float]) -> int:
        """Prédit une classe binaire (0 ou 1) pour un vecteur d'entréer données."""
        Loader.call(
            "predict_classifications",
            self.ptr,
            prefix_errmsg="LinearModel.predict_classification()"
        )
        return int()
    
    def train_classification(
            self, 
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            alpha: float,
            epochs: int
            ) -> None:
        """"Entraîne le modèle de classification binaire en utilisant la règle de Rosenblatt."""
        
        Loader.call(
            "train_classification",
            self.ptr,
            prefix_errmsg="LinearModel.train_classification()"
        )

    def train_regression(
            self, 
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            alpha: float,
            epochs: int
            ) -> None:
        """"Entraîne le modèle de régression linéaire en utilisant la descente de gradient stochastique."""
        Loader.call(
            "train_regression",
            self.ptr,
            prefix_errmsg="LinearModel.train_regression()"
        )