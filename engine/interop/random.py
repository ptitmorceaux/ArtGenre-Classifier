import ctypes
from engine.interop.loader import Loader

#====== Publique ======#

def random_float32(a: float, b: float) -> float:
    """base ^ exp"""
    prefix_errmsg = "Random.random_float32()"
    Loader.check_primitive_values_range(a, ctypes.c_float, prefix_errmsg)
    Loader.check_primitive_values_range(b, ctypes.c_float, prefix_errmsg)
    result = ctypes.c_float()
    Loader.call(
        "random_float",
        ctypes.c_float(a),
        ctypes.c_float(b),
        ctypes.byref(result),
        prefix_errmsg=prefix_errmsg
    )
    return result.value
