import ctypes
from engine.interop.loader import Loader


class MLP:
    """
    Wrapper Python pour MLP en C.
    Cette classe permet de gérer le pointeur mémoire côté C.
    """

    #====== Constructeurs ======#

    def __init__(self, input_dim: int) -> None:
        Loader.check_primitive_values_range(input_dim, ctypes.c_uint32, "LinearModel.__init__()")
        if input_dim == 0:
            raise ValueError("LinearModel.__init__(): `input_dim` must be > 0")
        self.ptr = None
        self.input_dim = input_dim
    
    #====== Méthode privée - Utils ======#

    
