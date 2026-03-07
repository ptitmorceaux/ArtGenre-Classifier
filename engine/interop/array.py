import ctypes
from engine.interop.loader import Loader


def get_float32_array_from_py_list(data: list[float | int], prefix_errmsg: str = "") -> dict[ctypes.Array, int]:
    """Convertit une liste Python de floats en un tableau C de float32 et retourne un pointeur vers ce tableau ainsi que sa longueur."""
    prefix_err = f"{prefix_errmsg}: get_float32_array_from_py_list()" if prefix_errmsg else "get_float32_array_from_py_list()"
    
    if not data or not isinstance(data, list):
        raise TypeError(f"{prefix_err}: `data` must be a non-empty list of floats")
    
    length = len(data)

    try:
        ArrayType = ctypes.c_float * length
        c_array = ArrayType(*[ctypes.c_float(x) for x in data])
    except Exception as e:
        raise TypeError(f"{prefix_err}: Error occurred while creating the C array") from e

    return {"c_array": c_array, "length": length}
