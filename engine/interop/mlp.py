import ctypes
from engine.interop.loader import Loader


class _CMLP(ctypes.Structure):
    _fields_ = [
        ("model_type", ctypes.c_int),  # ModelType
        ("d", ctypes.POINTER(ctypes.c_uint32)),  # Tableau des dimensions des couches (d[0] = input_dim, d[L] = output_dim)
        ("L", ctypes.c_uint32),  # Nombre de couches (sans compter la couche d'entrée)
        ("W", ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_float)))),  # Tableau de pointeurs vers les poids de chaque couche
        ("X", ctypes.POINTER(ctypes.POINTER(ctypes.c_float))),
        ("deltas", ctypes.POINTER(ctypes.POINTER(ctypes.c_float))),
    ]


class MLP:
    """
    Wrapper Python pour MLP en C.
    Cette classe permet de gérer le pointeur mémoire côté C.
    """

    #====== Constructeurs ======#

    def __init__(self, npl: list[int], init_without_create: bool = False) -> None:
        if len(npl) < 2:
            raise ValueError("MLP.__init__(): Le réseau doit avoir au moins 2 couches (entrée et sortie).")
        self.npl = npl
        npl_size = len(npl)

        Loader.check_primitive_values_range(npl_size, ctypes.c_uint32, "MLP.__init__()")
        for n in npl:
            Loader.check_primitive_values_range(n, ctypes.c_uint32, "MLP.__init__()")
            if n == 0:
                raise ValueError("MLP.__init__(): Toutes les couches doivent avoir au moins 1 neurone.")

        c_npl_array = (ctypes.c_uint32 * npl_size)(*npl)
        self.ptr = ctypes.c_void_p()

        if init_without_create:
            self.ptr = None
            return

        Loader.call(
            "create_mlp",
            c_npl_array,
            ctypes.c_uint32(npl_size),
            ctypes.byref(self.ptr),
            prefix_errmsg="MLP.__init__()"
        )
    
    @classmethod
    def _init_from_model_ptr(cls, model_ptr) -> "MLP":
        """Initialise un MLP à partir d'un pointeur vers un modèle C existant."""

        if model_ptr is None or model_ptr.value is None:
            raise ValueError("MLP._init_from_model_ptr(): model_ptr is NULL.")

        model_struct = ctypes.cast(
            model_ptr,
            ctypes.POINTER(_CMLP)
        ).contents

        npl = list(model_struct.d[:model_struct.L + 1])

        instance = cls(npl, init_without_create=True)
        instance.ptr = model_ptr
        
        return instance

    def close(self) -> None:
        """Libère la mémoire allouée pour le MLP côté C."""
        if self.ptr is not None:
            Loader.call(
                "free_mlp",
                ctypes.byref(self.ptr),
                prefix_errmsg="MLP.close()"
            )
            self.ptr = None
    
    def __del__(self):
        self.close()

    def predict(self, input_data: list[float], is_classification: bool) -> list[float]:
        """Fait une prédiction (Forward pass)."""
        # Vérification de la taille d'entrée
        if len(input_data) != self.npl[0]:
            raise ValueError(f"MLP.predict(): input_data doit être de taille {self.npl[0]}")

        c_input_array = (ctypes.c_float * len(input_data))(*input_data)
        output_dim = self.npl[-1]
        c_res_outputs = (ctypes.c_float * output_dim)()
        c_is_classification = ctypes.c_byte(1 if is_classification else 0)

        Loader.call(
            "predict_mlp",
            self.ptr,
            c_input_array,
            c_is_classification,
            ctypes.byref(c_res_outputs),
            prefix_errmsg="MLP.predict()"
        )
        return [c_res_outputs[i] for i in range(output_dim)]
    
    def train(
            self, 
            dataset_inputs: list[float],
            dataset_expected_outputs: list[float],
            data_size: int,
            alpha: float,
            epochs: int,
            is_classification: bool
            ) -> None:
        """Entraîne le MLP en utilisant la rétropropagation du gradient (SGD)."""
        
        # Vérifications
        Loader.check_primitive_values_range(data_size, ctypes.c_uint32, "MLP.train()")
        Loader.check_primitive_values_range(alpha, ctypes.c_float, "MLP.train()")
        Loader.check_primitive_values_range(epochs, ctypes.c_uint32, "MLP.train()")

        # Conversions des listes Python en tableaux C
        c_dataset_inputs = (ctypes.c_float * len(dataset_inputs))(*dataset_inputs)
        c_expected_outputs = (ctypes.c_float * len(dataset_expected_outputs))(*dataset_expected_outputs)
        
        c_is_classification = ctypes.c_byte(1 if is_classification else 0)

        Loader.call(
            "train_mlp",
            self.ptr,
            c_dataset_inputs,
            c_expected_outputs,
            ctypes.c_uint32(data_size),
            ctypes.c_float(alpha),
            ctypes.c_uint32(epochs),
            c_is_classification,
            prefix_errmsg="MLP.train()"
        )


    # ===== GETTER / SETTER ======#

    def get_weights(self) -> list[list[list[float]]]:
        """Renvoie les poids sous forme de liste imbriquée : weights[l][i][j]."""
        if self.ptr is None or self.ptr.value is None:
            raise ValueError("MLP.get_weights(): model is not initialized.")

        model_struct = ctypes.cast(self.ptr, ctypes.POINTER(_CMLP)).contents
        d = list(model_struct.d[:model_struct.L + 1])
        L = model_struct.L

        weights = []
        for layer_index in range(L):
            rows = d[layer_index] + 1   # +1 pour le biais
            cols = d[layer_index + 1]
            layer = [list(model_struct.W[layer_index][i][:cols]) for i in range(rows)]
            weights.append(layer)
        return weights

    def set_weights(self, weights: list[list[list[float]]]) -> None:
        """Écrit des poids donnés dans le modèle C (weights[l][i][j])."""
        if self.ptr is None or self.ptr.value is None:
            raise ValueError("MLP.set_weights(): model is not initialized.")

        model_struct = ctypes.cast(self.ptr, ctypes.POINTER(_CMLP)).contents
        d = list(model_struct.d[:model_struct.L + 1])
        L = model_struct.L

        for layer_index in range(L):
            rows = d[layer_index] + 1
            cols = d[layer_index + 1]
            for i in range(rows):
                for j in range(cols):
                    model_struct.W[layer_index][i][j] = weights[layer_index][i][j]