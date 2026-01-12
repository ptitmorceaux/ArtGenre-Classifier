import ctypes
from api.wrappers.loader import init_library

class MathLib:
    
    def __init__(self, lib_folder="libc", basename="mathlib"):
        """Charge la lib et configure les types ctypes pour chaque fonction"""
        try:
            self._lib = init_library(lib_folder, basename)
        except Exception as e:
            raise RuntimeError(f"mathlib: lib_folder='{lib_folder}', basename='{basename}': {e}")

    #====== Méthode privée ======#

    def _call(self, func, a, b):
        """Exécute l'appel C et gère les erreurs de manière générique"""
        result = ctypes.c_double()
        err_code = func(a, b, ctypes.byref(result))
        
        if err_code != 0:
            # Récupération du message via la fonction strerror du C
            error_msg = self._lib.strerror(err_code).decode("utf-8")
            raise RuntimeError(f"mathlib: {error_msg}")
        
        return result.value

    #====== Méthodes publiques ======#

    def addition(self, a: float, b: float) -> float:
        return self._call(self._lib.add, a, b)

    def subtraction(self, a: float, b: float) -> float:
        return self._call(self._lib.sub, a, b)
    
    def multiplication(self, a: float, b: float) -> float:
        return self._call(self._lib.mult, a, b)

    def division(self, a: float, b: float) -> float:
        return self._call(self._lib.div, a, b)

    def power(self, base: float, exp: int) -> float:
        return self._call(self._lib.power, base, exp)
