import ctypes
from engine.interop.loader import Loader

#====== Privée ======#

_loader = Loader()

# Fonctionne UNIQUEMENT pcque ttes les fcts ont 2 args et un retour de type float
def _call(func_name: str, a, b, prefix_errmsg: str = "") -> float:
    """Exécute l'appel C et gère les erreurs de manière générique"""
    prefix = f"{prefix_errmsg}: _call()" if prefix_errmsg else "_call()"
    _loader.check_ctype(a, ctypes.c_float, prefix)
    _loader.check_ctype(b, ctypes.c_float, prefix)
    result = ctypes.c_float()
    _loader.call(
        func_name,
        ctypes.c_float(a),
        ctypes.c_float(b),
        ctypes.byref(result),
        prefix_errmsg=prefix
    )
    return result.value

#====== Publique ======#

def addition(a: float, b: float) -> float:
    return _call("my_add", a, b, "Math.addition()")

def subtraction(a: float, b: float) -> float:
    return _call("my_sub", a, b, "Math.subtraction()")
    
def multiplication(a: float, b: float) -> float:
    return _call("my_mult", a, b, "Math.multiplication()")

def division(a: float, b: float) -> float:
    return _call("my_div", a, b, "Math.division()")

def power(base: float, exp: int) -> float:
    prefix_errmsg = "Math.power()"
    _loader.check_ctype(base, ctypes.c_float, prefix_errmsg)
    _loader.check_ctype(exp, ctypes.c_int32, prefix_errmsg)
    result = ctypes.c_float()
    _loader.call(
        "my_pow",
        ctypes.c_float(base),
        ctypes.c_int32(exp),
        ctypes.byref(result),
        prefix_errmsg=prefix_errmsg
    )
    return result.value
