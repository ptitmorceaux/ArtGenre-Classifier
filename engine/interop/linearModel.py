import ctypes
from engine.interop.loader import Loader


class LinearModel:
    """
    Wrapper Python pour LinearModel en C.
    Cette classe permet de gérer le pointeur mémoire côté C.
    """

    #====== Constructeurs ======#

    def __init__(self, input_dim: int) -> None:
        Loader.check_primitive_values_range(input_dim, ctypes.c_uint32, "LinearModel.__init__()")
        if input_dim == 0:
            raise ValueError("LinearModel.__init__(): `input_dim` must be > 0")
        self.ptr = None
        self.input_dim = input_dim
    
    @classmethod
    def init_random(cls, input_dim: int) -> 'LinearModel':
        """Initialise un modèle de régression linéaire avec des poids aléatoires."""        
        instance = cls(input_dim)

        # On crée un pointeur vide (void*) qui recevra l'adresse du modèle C.
        instance.ptr = ctypes.c_void_p()
        instance.input_dim = input_dim

        Loader.call(
            "create_linear_model_randomly",
            ctypes.c_uint32(input_dim),
            ctypes.byref(instance.ptr),
            prefix_errmsg="LinearModel.init_random()"
        )
        return instance

    @classmethod
    def init_from_weights(cls, weights: list[float], bias: float) -> 'LinearModel':
        """Initialise un modèle de régression linéaire avec des poids et un biais donnés."""
        if not isinstance(weights, list) or len(weights) == 0:
            raise ValueError("LinearModel.init_from_weights(): `weights` must be a non-empty list of floats.")

        Loader.check_primitive_values_range(bias, ctypes.c_float, "LinearModel.init_from_weights()")

        instance = cls(len(weights))
        instance.ptr = ctypes.c_void_p()

        Loader.call(
            "create_linear_model_from_init_weights",
            (ctypes.c_float * instance.input_dim)(*weights),
            ctypes.c_uint32(instance.input_dim),
            ctypes.c_float(bias),
            ctypes.byref(instance.ptr),
            prefix_errmsg="LinearModel.init_from_weights()"
        )
        return instance
    
    #====== Méthode privée - Utils ======#
    
    def _free(self) -> None:
        """Libère la mémoire allouée pour le modèle C."""
        if self.ptr is not None and self.ptr.value is not None:
            Loader.call(
                "free_linear_model",
                ctypes.byref(self.ptr),
                prefix_errmsg="LinearModel._free()"
            )
        self.ptr = None
        self.input_dim = 0

    def __del__(self):
        try:
            self._free()
        except Exception:
            # Evite de remonter des exceptions pendant le GC/interpreter shutdown o-o
            pass
    
    #====== Méthode publique - Prédiction ======#

    def predict_linear_regression(self, input_data: list[float]) -> float:
        """Prédit une valeur continue pour un vecteur d'entrée de données."""
        if len(input_data) != self.input_dim:
            raise ValueError(f"LinearModel.predict_linear_regression(): `input_data` length must be equal to model's input_dim ({self.input_dim}).")
    
        result = ctypes.c_float()
        Loader.call(
            "predict_linear_regression",
            self.ptr,
            (ctypes.c_float * len(input_data))(*input_data),
            ctypes.byref(result),
            prefix_errmsg="LinearModel.predict_linear_regression()"
        )
        return result.value

    def predict_linear_classification(self, input_data: list[float]) -> int:
        """Prédit une classe binaire (0 ou 1) pour un vecteur d'entréer données."""
        if len(input_data) != self.input_dim:
            raise ValueError(f"LinearModel.predict_linear_classification(): `input_data` length must be equal to model's input_dim ({self.input_dim}).")

        result = ctypes.c_int32()
        Loader.call(
            "predict_linear_classification",
            self.ptr,
            (ctypes.c_float * len(input_data))(*input_data),
            ctypes.byref(result),
            prefix_errmsg="LinearModel.predict_linear_classification()"
        )
        return result.value
    
    #====== Méthode privée - Entraînement ======#

    def _check_training_data(
            self,
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            errmsg: str
            ) -> tuple[int, int, int]:
        """Vérifie que les données d'entraînement sont valides pour le modèle (renvoie le nombre d'éléments de données)."""        
        
        all_data_length = len(dataset_inputs)
        y_size = len(dataset_expected_outputs)

        if all_data_length == 0:
            raise ValueError(f"{errmsg}: `dataset_inputs` cannot be empty.")

        if all_data_length % self.input_dim != 0:
            raise ValueError(f"{errmsg}: `dataset_inputs` length must be a multiple of model's input_dim ({self.input_dim}).")

        data_size = all_data_length // self.input_dim

        if y_size == 0:
            raise ValueError(f"{errmsg}: `dataset_expected_outputs` cannot be empty.")

        if y_size != data_size:
            raise ValueError(f"{errmsg}: `dataset_expected_outputs` length must equal dataset_size ({data_size}).")
        
        return all_data_length, y_size, data_size

    #====== Méthode publique - Entraînement ======#

    def train_linear_classification(
            self,
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            alpha: float,
            epochs: int
            ) -> None:
        """Entraîne le modèle de classification binaire en utilisant la règle de Rosenblatt."""

        all_data_length, y_size, data_size = self._check_training_data(dataset_inputs, dataset_expected_outputs, "LinearModel.train_linear_classification()")

        # On vérifie les types des arguments
        Loader.check_primitive_values_range(data_size, ctypes.c_uint32, "LinearModel.train_linear_classification()")
        Loader.check_primitive_values_range(alpha, ctypes.c_float, "LinearModel.train_linear_classification()")
        Loader.check_primitive_values_range(epochs, ctypes.c_uint32, "LinearModel.train_linear_classification()")
        Loader.call(
            "train_linear_classification",
            self.ptr,
            (ctypes.c_float * all_data_length)(*dataset_inputs),
            (ctypes.c_float * y_size)(*dataset_expected_outputs),
            ctypes.c_uint32(data_size),
            ctypes.c_float(alpha),
            ctypes.c_uint32(epochs),
            prefix_errmsg="LinearModel.train_linear_classification()"
        )

    def train_linear_regression(
            self, 
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            alpha: float,
            epochs: int
            ) -> None:
        """Entraîne le modèle de régression linéaire en utilisant la descente de gradient stochastique."""

        all_data_length, y_size, data_size = self._check_training_data(dataset_inputs, dataset_expected_outputs, "LinearModel.train_linear_regression()")

        # On vérifie les types des arguments
        Loader.check_primitive_values_range(data_size, ctypes.c_uint32, "LinearModel.train_linear_regression()")
        Loader.check_primitive_values_range(alpha, ctypes.c_float, "LinearModel.train_linear_regression()")
        Loader.check_primitive_values_range(epochs, ctypes.c_uint32, "LinearModel.train_linear_regression()")

        Loader.call(
            "train_linear_regression",
            self.ptr,
            (ctypes.c_float * all_data_length)(*dataset_inputs),
            (ctypes.c_float * y_size)(*dataset_expected_outputs),
            ctypes.c_uint32(data_size),
            ctypes.c_float(alpha),
            ctypes.c_uint32(epochs),
            prefix_errmsg="LinearModel.train_linear_regression()"
        )