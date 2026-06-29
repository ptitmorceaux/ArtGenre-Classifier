import ctypes
from engine.interop.loader import Loader


class MLP:
    """
    Wrapper Python pour MLP en C.
    Cette classe permet de gérer le pointeur mémoire côté C.
    """

    #====== Constructeurs ======#

    def __init__(self, npl: list[int]) -> None:
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

        Loader.call(
            "create_mlp",
            c_npl_array,
            ctypes.c_uint32(npl_size),
            ctypes.byref(self.ptr),
            prefix_errmsg="MLP.__init__()"
        )

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