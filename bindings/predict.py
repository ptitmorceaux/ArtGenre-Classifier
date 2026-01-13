import ctypes
from bindings.loader import Loader

class PredictLib(Loader):
    
    def __init__(self, basename="predict", lib_folder="libc", build_folder="build", specs_folder="specs"):
        try:
            super().__init__(basename=basename, lib_folder=lib_folder, build_folder=build_folder, specs_folder=specs_folder)
        except Exception as e:
            raise RuntimeError(f"predictlib.__init__(): {e}")

    #====== Méthode privée ======#

    def _get_error(self, err_code: int):
        """Teste le code d'erreur et lève une exception si besoin"""
        if err_code != 0:
            error_msg = self._lib.strerror(err_code).decode("utf-8")
            raise RuntimeError(f"predictlib._get_error(): {error_msg}")

    #====== Méthodes publiques ======#

    def factorial(self, nb: int) -> int:
        if not self.is_uint32(nb):
            raise ValueError(f"predictlib.factorial(): `nb` must be between 0 and 4294967295 (uint32), got {nb}")
        result = ctypes.c_int32()
        self._get_error(self._lib.factorial(nb, ctypes.byref(result)))
        return result.value