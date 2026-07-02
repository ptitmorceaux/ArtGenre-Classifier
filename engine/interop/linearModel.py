import ctypes
import numpy as np
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
    
    # input_dim = longueur des poids (len(W))
    @classmethod
    def init_random(cls, input_dim: int) -> 'LinearModel':
        """Initialise un modèle de régression linéaire avec des poids aléatoires."""
        instance = cls(input_dim)

        # On crée un pointeur vide (void*) qui recevra l'adresse du modèle C.
        instance.ptr = ctypes.c_void_p()

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

        instance = cls(len(weights))  # add_a_bias is set to True for this constructor
        instance.ptr = ctypes.c_void_p()

        Loader.call(
            "create_linear_model_from_init_weights",
            (ctypes.c_float * instance.input_dim)(*weights),
            ctypes.c_uint32(instance.input_dim), # the library needs to know the length without the "bias" column
            ctypes.c_float(bias),
            ctypes.byref(instance.ptr),
            prefix_errmsg="LinearModel.init_from_weights()"
        )
        return instance
    
    @classmethod
    def init_and_calculate_best_weights_with_pseudo_inverse(
            cls,
            dataset_inputs_without_bias: list[float],
            dataset_expected_outputs: list[float]
            ) -> 'LinearModel':
        """
        Initialise un modèle de régression linéaire et ses poids à partir de listes d'entrées et de sorties attendues.
        Renvoie un modèle entraîné via la pseudo-inverse.
        """
        if not dataset_expected_outputs:
            raise ValueError("LinearModel.init_and_calculate_best_weights_with_pseudo_inverse(): `dataset_expected_outputs` cannot be empty.")
            
        # 1. Déduction dynamique de la dimension d'entrée (input_dim = n = colonnes)
        # On calcule d'abord le nombre de lignes (m) qui est égal au nombre de sorties attendues
        row_count = len(dataset_expected_outputs)
        all_data_length = len(dataset_inputs_without_bias)
        
        if row_count == 0 or all_data_length % row_count != 0:
            raise ValueError("LinearModel.init_and_calculate_best_weights_with_pseudo_inverse(): Invalid dataset dimensions.")
            
        col_count = all_data_length // row_count

        # 2. Utilisation propre de ta fonction de validation centralisée
        # On lui passe bien explicitement la dimension calculée en premier paramètre !
        all_data_length, y_size, row_count = LinearModel._check_training_data(
            col_count,
            dataset_inputs_without_bias, 
            dataset_expected_outputs, 
            "LinearModel.init_and_calculate_best_weights_with_pseudo_inverse()"
        )

        # On crée un pointeur vide (void*) qui recevra l'adresse du modèle C.
        model_ptr = ctypes.c_void_p()

        arr_inputs = np.asarray(dataset_inputs_without_bias, dtype=np.float32)
        arr_outputs = np.asarray(dataset_expected_outputs, dtype=np.float32)

        # 3. Appel à la bibliothèque C avec les bonnes dimensions validées
        Loader.call(
            "get_linear_regression_weights_from_list",
            arr_inputs.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
            arr_outputs.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
            ctypes.c_uint32(row_count), # row = m
            ctypes.c_uint32(col_count), # col = n
            ctypes.byref(model_ptr),
            prefix_errmsg="LinearModel.init_and_calculate_best_weights_with_pseudo_inverse()"
        )

        # 4. Instanciation de l'objet Python avec la bonne dimension d'entrée
        model_instance = cls(col_count)
        model_instance.ptr = model_ptr
        return model_instance
    
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
    
    #====== Méthode privée - Entraînement ======#

    @staticmethod
    def _check_training_data(
            input_dim: int,
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            errmsg: str
            ) -> tuple[int, int, int]:
        """Vérifie que les données d'entraînement sont valides pour le modèle (renvoie le nombre d'éléments de données)."""        
        
        all_data_length = len(dataset_inputs)
        y_size = len(dataset_expected_outputs)

        if all_data_length == 0:
            raise ValueError(f"{errmsg}: `dataset_inputs` cannot be empty.")

        if all_data_length % input_dim != 0:
            raise ValueError(f"{errmsg}: `dataset_inputs` length must be a multiple of model's input_dim ({input_dim}).")

        row_count = all_data_length // input_dim

        if y_size == 0:
            raise ValueError(f"{errmsg}: `dataset_expected_outputs` cannot be empty.")

        if y_size != row_count:
            raise ValueError(f"{errmsg}: `dataset_expected_outputs` length must equal dataset_size ({row_count}).")
        
        return all_data_length, y_size, row_count
    
    #====== Méthode publique - Prédiction ======#

    def predict(self, input_data: list[float], is_classification: bool) -> float | int:
        """
        Si is_classification = True: Prédit une classe binaire signée (-1 ou 1) pour un vecteur d'entrée.
        Si is_classification = False: Prédit une valeur continue pour un vecteur d'entrée.
        """
        if len(input_data) != self.input_dim:
            raise ValueError(f"LinearModel.predict(): `input_data` length must be equal to model's input_dim ({self.input_dim}).")
    
        result = ctypes.c_int32() if is_classification else ctypes.c_float()

        arr = np.ascontiguousarray (input_data, dtype=np.float32)

        Loader.call(
            "predict_linear_classification" if is_classification else "predict_linear_regression",
            self.ptr,
            arr.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
            ctypes.byref(result),
            prefix_errmsg="LinearModel.predict()"
        )
        return result.value

    #====== Méthode publique - Entraînement ======#

    def train(
            self,
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            alpha: float,
            epochs: int,
            is_classification: bool
            ) -> tuple[list[float], list[float]]:
        """
        Si is_classification = True: Entraîne le modèle de classification binaire signée (-1 / 1) en utilisant la règle de Rosenblatt.
        Si is_classification = False: Entraîne le modèle de régression linéaire en utilisant la descente de gradient stochastique.
        """

        all_data_length, y_size, row_count = LinearModel._check_training_data(
            self.input_dim,
            dataset_inputs,
            dataset_expected_outputs,
            "LinearModel.train()"
        )

        c_loss_history = (ctypes.c_float * epochs)()
        c__accuracy_history = (ctypes.c_float * epochs)() if is_classification else None

        # On vérifie les types des arguments
        Loader.check_primitive_values_range(row_count, ctypes.c_uint32, "LinearModel.train()")
        Loader.check_primitive_values_range(alpha, ctypes.c_float, "LinearModel.train()")
        Loader.check_primitive_values_range(epochs, ctypes.c_uint32, "LinearModel.train()")

        arr_inputs = np.asarray(dataset_inputs, dtype=np.float32)
        arr_outputs = np.asarray(dataset_expected_outputs, dtype=np.float32)

        Loader.call(
            "train_linear_classification" if is_classification else "train_linear_regression",
            self.ptr,
            arr_inputs.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
            arr_outputs.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
            ctypes.c_uint32(row_count),
            ctypes.c_float(alpha),
            ctypes.c_uint32(epochs),
            c_loss_history,
            c__accuracy_history,
            prefix_errmsg="LinearModel.train()"
        )
        return list(c_loss_history), list(c__accuracy_history)