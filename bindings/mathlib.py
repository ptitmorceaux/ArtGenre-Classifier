import ctypes
from bindings.loader import Loader

class MathLib(Loader):
    
    def __init__(self, basename="mathlib", lib_folder="libc", build_folder="build", specs_folder="specs"):
        try:
            super().__init__(basename=basename, lib_folder=lib_folder, build_folder=build_folder, specs_folder=specs_folder)
        except Exception as e:
            raise RuntimeError(f"mathlib.__init__(): {e}")

    #====== Méthode privée ======#

    def _get_error(self, err_code: int):
        """Teste le code d'erreur et lève une exception si besoin"""
        if err_code != 0:
            error_msg = self._lib.strerror(err_code).decode("utf-8")
            raise RuntimeError(f"mathlib._get_error(): {error_msg}")

    # Fonctionne UNIQUEMENT pcque ttes les fcts ont 2 args et un retour de type double
    def _call(self, func, a, b):
        """Exécute l'appel C et gère les erreurs de manière générique"""
        result = ctypes.c_double()
        self._get_error(func(a, b, ctypes.byref(result)))
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
        if not self._is_int32(exp):
            raise ValueError(f"mathlib.power(): `exp` must be between -2147483648 and 2147483647 (int32), got {exp}")
        return self._call(self._lib.power, base, exp)
