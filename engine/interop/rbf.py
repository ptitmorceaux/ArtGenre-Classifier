import ctypes
from engine.interop.loader import Loader


class RBF:
    """
    Wrapper Python pour le modèle RBF en C.
    Cette classe permet de gérer le pointeur mémoire côté C.
    """

    #====== Constructeurs ======#

    def __init__(self, input_dim: int, num_centers: int, gamma: float = 1.0) -> None:
        """
        Initialise un réseau RBF.
        """
        self.input_dim = input_dim
        self.num_centers = num_centers
        self.gamma = gamma
        self.ptr = ctypes.c_void_p()

        Loader.call(
            "create_rbf",
            ctypes.c_uint32(input_dim),
            ctypes.c_uint32(num_centers),
            ctypes.c_float(gamma),
            ctypes.byref(self.ptr),
            prefix_errmsg="RBF.__init__()"
        )

    def close(self) -> None:
        """Libère la mémoire allouée pour le RBF côté C."""
        if self.ptr is not None:
            Loader.call(
                "free_rbf",
                ctypes.byref(self.ptr),
                prefix_errmsg="RBF.close()"
            )
            self.ptr = None
    
    def __del__(self):
        self.close()

    #====== Prédiction ======#

    def predict(self, input_data: list[float], is_classification: bool = True) -> float | int:
        """
        Fait une prédiction (Forward pass).
        Si is_classification = True : prédit une classe binaire signée (-1 ou 1).
        Si is_classification = False : prédit une valeur continue (régression).
        """
       # Vérification de la taille d'entrée
        if len(input_data) != self.input_dim:
            raise ValueError(f"RBF.predict(): input_data doit être de taille {self.input_dim}")

        c_input_array = (ctypes.c_float * len(input_data))(*input_data)

        # Le type du résultat dépend du mode : int32 pour la classe, float pour la valeur continue
        c_res_output = ctypes.c_int32() if is_classification else ctypes.c_float()

        Loader.call(
            "predict_rbf" if is_classification else "predict_rbf_regression",
            self.ptr,
            c_input_array,
            ctypes.byref(c_res_output),
            prefix_errmsg="RBF.predict()"
        )
        return c_res_output.value
    
    #====== Entraînement ======#

    def train(
            self, 
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            data_size: int,
            alpha: float,
            epochs: int,
            is_classification: bool = True
            ) -> None:
        """
        Entraîne le RBF (Phase 1: K-Means / Phase 2: calcul de Gamma).
        Si is_classification = True : Phase 3 = règle de Rosenblatt (classification -1/1).
        Si is_classification = False : Phase 3 = descente de gradient (régression).
        """
        
        # Vérifications des primitives (Sécurité Ctypes)
        Loader.check_primitive_values_range(data_size, ctypes.c_uint32, "RBF.train()")
        Loader.check_primitive_values_range(alpha, ctypes.c_float, "RBF.train()")
        Loader.check_primitive_values_range(epochs, ctypes.c_uint32, "RBF.train()")

        # Conversions des listes Python en tableaux C
        c_dataset_inputs = (ctypes.c_float * len(dataset_inputs))(*dataset_inputs)
        c_expected_outputs = (ctypes.c_float * len(dataset_expected_outputs))(*dataset_expected_outputs)

        Loader.call(
            "train_rbf" if is_classification else "train_rbf_regression",
            self.ptr,
            c_dataset_inputs,
            c_expected_outputs,
            ctypes.c_uint32(data_size),
            ctypes.c_float(alpha),
            ctypes.c_uint32(epochs),
            prefix_errmsg="RBF.train()"
        )