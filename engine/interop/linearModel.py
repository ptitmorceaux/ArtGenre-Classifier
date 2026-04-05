import ctypes
from typing import Type
from engine.interop.loader import Loader


class LinearModel:
    """
    Wrapper Python pour LinearModel en C.
    Cette classe permet de gérer le pointeur mémoire côté C.
    """

    def __init__(self, input_dim: int):
        Loader.check_primitive_values_range(input_dim, ctypes.c_uint32, "LinearModel.__init__()")
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
    
    def _close(self):
        """"Libère la mémoire allouée pour le modèle C."""
        if self.ptr is not None:
            Loader.call(
                "free_linear_model",
                ctypes.byref(self.ptr),
                prefix_errmsg="LinearModel._close()"
            )

    def __del__(self):
        self._close()

    def predict_linear_regression(self, input_data: list[float]) -> float:
        """"Prédit une valeur continue pour un vecteur d'entrée de données."""
        result = ctypes.c_float()
        Loader.call(
            "predict_linear_regressions",
            self.ptr,
            input_data,
            ctypes.byref(result),
            prefix_errmsg="LinearModel.predict_linear_regression()"
        )
        return result.value

    def predict_linear_classification(self, input_data: list[float]) -> int:
        """Prédit une classe binaire (0 ou 1) pour un vecteur d'entréer données."""
        result = ctypes.c_int32()
        Loader.call(
            "predict_linear_classifications",
            self.ptr,
            input_data,
            ctypes.byref(result),
            prefix_errmsg="LinearModel.predict_linear_classification()"
        )
        return result.value
    
    def train_linear_classification(
            self, 
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            data_size: int,
            alpha: float,
            epochs: int
            ) -> None:
        """"Entraîne le modèle de classification binaire en utilisant la règle de Rosenblatt."""
        
        # On vérifie les types des arguments
        Loader.check_primitive_values_range(data_size, ctypes.c_uint32, "LinearModel.train_linear_classification()")
        Loader.check_primitive_values_range(alpha, ctypes.c_float, "LinearModel.train_linear_classification()")
        Loader.check_primitive_values_range(epochs, ctypes.c_uint32, "LinearModel.train_linear_classification()")
        Loader.call(
            "train_linear_classification",
            self.ptr,
            dataset_inputs,
            dataset_expected_outputs,
            data_size,
            alpha,
            epochs,
            prefix_errmsg="LinearModel.train_linear_classification()"
        )

    def train_linear_regression(
            self, 
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            data_size: int,
            alpha: float,
            epochs: int
            ) -> None:
        """"Entraîne le modèle de régression linéaire en utilisant la descente de gradient stochastique."""
        
        # On vérifie les types des arguments
        Loader.check_primitive_values_range(data_size, ctypes.c_uint32, "LinearModel.train_linear_regression()")
        Loader.check_primitive_values_range(alpha, ctypes.c_float, "LinearModel.train_linear_regression()")
        Loader.check_primitive_values_range(epochs, ctypes.c_uint32, "LinearModel.train_linear_regression()")

        Loader.call(
            "train_linear_regression",
            self.ptr,
            dataset_inputs,
            dataset_expected_outputs,
            data_size,
            alpha,
            epochs,
            prefix_errmsg="LinearModel.train_linear_regression()"
        )