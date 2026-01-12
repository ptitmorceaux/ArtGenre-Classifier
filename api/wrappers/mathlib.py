import ctypes
from api.wrappers.loader import load_library

class MathLib:
    
    def __init__(self, dll_folder="libc", dll_basename="mathlib"):
        """Charge la lib et configure les types ctypes pour chaque fonction"""
        self._lib = load_library(dll_folder, dll_basename)
        
        functions = [
            (self._lib.addition, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)),
            (self._lib.soustraction, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)),
            (self._lib.multiplication, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)),
            (self._lib.division, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)),
            (self._lib.power, ctypes.c_double, ctypes.c_int32, ctypes.POINTER(ctypes.c_double))
        ]

        for func, type_a, type_b, type_result in functions:
            func.argtypes = [type_a, type_b, type_result]
            func.restype = ctypes.c_int32

        # Configuration de strerror
        self._lib.strerror.argtypes = [ctypes.c_int32]
        self._lib.strerror.restype = ctypes.c_char_p

    # --- Méthode privée ---

    def _call(self, func, a, b):
        """Exécute l'appel C et gère les erreurs de manière générique"""
        result = ctypes.c_double()
        err_code = func(a, b, ctypes.byref(result))
        
        if err_code != 0:
            # Récupération du message via la fonction strerror du C
            error_msg = self._lib.strerror(err_code).decode("utf-8")
            raise RuntimeError(f"mathlib: {error_msg}")
        
        return result.value

    # --- Méthodes publiques ---

    def addition(self, a: float, b: float) -> float:
        return self._call(self._lib.addition, a, b)

    def soustraction(self, a: float, b: float) -> float:
        return self._call(self._lib.soustraction, a, b)
    
    def multiplication(self, a: float, b: float) -> float:
        return self._call(self._lib.multiplication, a, b)

    def division(self, a: float, b: float) -> float:
        return self._call(self._lib.division, a, b)

    def power(self, base: float, exp: int) -> float:
        return self._call(self._lib.power, base, exp)


if __name__ == "__main__":
    try:
        mathlib = MathLib()
        print(f"10 + 5 = {mathlib.addition(10, 5)}") # 15.0
        print(f"10 / 2 = {mathlib.division(10, 2)}") # 5.0
        print(f"0 / 0 = {mathlib.division(0, 0)}") # error
    except Exception as e:
        print(f"Erreur : {e}") # Division by Zero