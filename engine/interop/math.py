import ctypes
from engine.interop.loader import Loader

#====== Privée ======#

_loader = Loader()

# Fonctionne UNIQUEMENT pcque ttes les fcts ont 2 args et un retour de type float
def _call(func, a, b, prefix_errmsg: str = "") -> float:
    """Exécute l'appel C et gère les erreurs de manière générique"""
    prefix = f"{prefix_errmsg}: _call()" if prefix_errmsg else "_call()"
    _loader._check_ctype(a, ctypes.c_float, prefix)
    _loader._check_ctype(b, ctypes.c_float, prefix)
    result = ctypes.c_float()
    _loader._check_error(func(a, b, ctypes.byref(result)), prefix)
    return result.value

#====== Publique ======#

def addition(a: float, b: float) -> float:
    return _call(_loader._lib.add, a, b, "Math.addition()")

def subtraction(a: float, b: float) -> float:
    return _call(_loader._lib.sub, a, b, "Math.subtraction()")
    
def multiplication(a: float, b: float) -> float:
    return _call(_loader._lib.mult, a, b, "Math.multiplication()")

def division(a: float, b: float) -> float:
    return _call(_loader._lib.div, a, b, "Math.division()")

def power(base: float, exp: int) -> float:
    _loader._check_ctype(base, ctypes.c_float, "Math.power()")
    _loader._check_ctype(exp, ctypes.c_int32, "Math.power()")
    result = ctypes.c_float()
    _loader._check_error(_loader._lib.pow(base, exp, ctypes.byref(result)), "Math.power()")
    return result.value