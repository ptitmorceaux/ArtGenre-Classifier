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