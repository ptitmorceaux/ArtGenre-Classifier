import ctypes
from engine.interop.loader import Loader

class LinearModel:
    """
    Wrapper Python pour LinearModel en C.
    Cette classe perrmet de gérer le pointeur mémoire en C
    """


    def __init__(self, input_dim: int):
        self.input_dim = input_dim
        # On créer un pointeur vide via (void*) qui resevera l'adresse du modèle
        self.ptr = ctypes.c_void_p()

        Loader.call(
            "create_linear_model",
            ctypes.c_uint32(input_dim),
            ctypes.byref(self.ptr),
            prefix_errmsg="LinearModel.__init__()"
        )