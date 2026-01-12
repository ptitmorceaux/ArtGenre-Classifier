import ctypes
import os

class MathLib:
    def __init__(self, dll_path="../dll/mathlib.dll"):

        # Vérification de l'existence de la DLL
        if not os.path.isfile(dll_path):
            raise FileNotFoundError(f"La DLL spécifiée est introuvable : {dll_path}")

        # Charger la DLL
        self._lib = ctypes.CDLL(dll_path)

        # 1. Configuration des signatures pour les opérations mathématiques
        # Toutes ont la même signature : (double, double, double*) -> int32
        math_functions = [
            self._lib.addition,
            self._lib.soustraction,
            self._lib.multiplication,
            self._lib.division
        ]
        
        for func in math_functions:
            func.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
            func.restype = ctypes.c_int32

        # 2. Configuration de strerror : (int32) -> char*
        self._lib.strerror.argtypes = [ctypes.c_int32]
        self._lib.strerror.restype = ctypes.c_char_p

    def _check_error(self, err_code):
        """Méthode interne pour gérer les codes d'erreur du C"""
        if err_code != 0:
            message = self._lib.strerror(err_code).decode("utf-8")
            raise RuntimeError(message)

    def _call_op(self, func, a, b):
        """Méthode utilitaire pour éviter la répétition"""
        result = ctypes.c_double()
        err = func(a, b, ctypes.byref(result))
        self._check_error(err)
        return result.value

    def addition(self, a: float, b: float) -> float:
        return self._call_op(self._lib.addition, a, b)

    def soustraction(self, a: float, b: float) -> float:
        return self._call_op(self._lib.soustraction, a, b)

    def multiplication(self, a: float, b: float) -> float:
        return self._call_op(self._lib.multiplication, a, b)

    def division(self, a: float, b: float) -> float:
        return self._call_op(self._lib.division, a, b)

# Exemple d'utilisation
if __name__ == "__main__":
    mathlib = MathLib()
    print(f"10 + 5 = {mathlib.addition(10, 5)}") # 15.0
    print(f"10 / 2 = {mathlib.division(10, 2)}") # 5.0
    try:
        mathlib.division(10, 0)
    except RuntimeError as e:
        print(f"Erreur : {e}") # Division by Zero