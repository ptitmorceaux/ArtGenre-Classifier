import ctypes
from engine.interop.loader import Loader

#====== Privée ======#

_loader = Loader()

# Fonctionne UNIQUEMENT pcque ttes les fcts ont 2 args et un retour de type float
def _call(func, a, b, prefix_errmsg: str = "") -> float:
    """Exécute l'appel C et gère les erreurs de manière générique"""
    prefix = f"{prefix_errmsg}: _call()" if prefix_errmsg else "_call()"
    _loader.check_ctype(a, ctypes.c_float, prefix)
    _loader.check_ctype(b, ctypes.c_float, prefix)
    result = ctypes.c_float()
    _loader.check_status(func(a, b, ctypes.byref(result)), prefix)
    return result.value

#====== Publique ======#

def addition(a: float, b: float) -> float:
    return _call(_loader._lib.my_add, a, b, "math.addition()")

def subtraction(a: float, b: float) -> float:
    return _call(_loader._lib.my_sub, a, b, "math.subtraction()")
    
def multiplication(a: float, b: float) -> float:
    return _call(_loader._lib.my_mult, a, b, "math.multiplication()")

def division(a: float, b: float) -> float:
    return _call(_loader._lib.my_div, a, b, "math.division()")

def power(base: float, exp: int) -> float:
    _loader.check_ctype(base, ctypes.c_float, "math.power()")
    _loader.check_ctype(exp, ctypes.c_int32, "math.power()")
    result = ctypes.c_float()
    _loader.check_status(_loader._lib.my_pow(base, exp, ctypes.byref(result)), "math.power()")
    return result.value