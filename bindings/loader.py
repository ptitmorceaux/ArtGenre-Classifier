import ctypes
import os
import sys
import json

class Loader:
    """Classe de chargement des bibliothèques C via ctypes"""
    
    def __init__(self, basename, lib_folder="libc", build_folder="build", specs_folder="specs"):
        """Charge la lib et configure les types ctypes pour chaque fonction"""
        self._lib = None
        self._specs = dict()

        self.basename = basename
        self.lib_folder = lib_folder
        self.build_folder = build_folder
        self.specs_folder = specs_folder
        
        self.ext = "dll" if sys.platform.startswith("win") else "dylib" if sys.platform.startswith("darwin") else "so"
        self._load_library()
        self._load_json_specs()
        self._attribute_types()

    #====== Méthode privée - Init ======#

    def _load_library(self):
        """
        Charge une bibliothèque partagée (.dll, .so, .dylib)
        de manière transparente selon l'OS.
        """
        lib_path = os.path.join(self.lib_folder, self.build_folder, f"{self.basename}.{self.ext}")
        
        if not os.path.exists(lib_path):
            raise FileNotFoundError(f"Unable to find the library: `{lib_path}`")
        
        self._lib = ctypes.CDLL(lib_path)


    def _load_json_specs(self):
        """Charge le fichier json décrivant les fonctions de la lib"""
        info_path = os.path.join(self.lib_folder, self.specs_folder, f"{self.basename}.json")
        
        if not os.path.exists(info_path):
            raise FileNotFoundError(f"Loader._load_json_specs(): Unable to find the json: {info_path}")
        
        with open(info_path, "r") as f:
            self._specs = json.load(f)
        
        if not self._specs:
            raise ValueError(f"Loader._load_json_specs(): Empty json: {info_path}")


    def _attribute_types(self):
        """Configure les types ctypes pour chaque fonction"""
        for name, info in self._specs.items():
            try:
                func = getattr(self._lib, name)
            except AttributeError:
                raise AttributeError(f"loader.init_library(): Function `{name}` not found in the library")
            
            # Configuration des types d'arguments
            argtypes = []
            for arg_type in info["argtypes"]:
                match arg_type:
                    case "int32_t":     argtypes.append(ctypes.c_int32)
                    case "uint32_t":    argtypes.append(ctypes.c_uint32)
                    case "double":      argtypes.append(ctypes.c_double)
                    case "char":        argtypes.append(ctypes.c_char)
                    case "int32_t*":    argtypes.append(ctypes.POINTER(ctypes.c_int32))
                    case "uint32_t*":   argtypes.append(ctypes.POINTER(ctypes.c_uint32))
                    case "double*":     argtypes.append(ctypes.POINTER(ctypes.c_double))
                    case "char*":       argtypes.append(ctypes.c_char_p)
                    case _: raise TypeError(f"loader.init_library(): Unknow argtype for `{name}` : {arg_type}")
            
            func.argtypes = argtypes
            
            # Configuration du type de retour
            ret_type = info["restype"]
            match ret_type:
                case "int32_t": func.restype = ctypes.c_int32
                case "char*":   func.restype = ctypes.c_char_p
                case _: raise TypeError(f"loader.init_library(): Unknow restype for `{name}` : {ret_type}")

    #====== Méthode privée - Utils ======#

    def _is_uint32(self, n: int) -> bool:
        return 0 <= n <= 4294967295

    def _is_int32(self, n: int) -> bool:
        return -2147483648 <= n <= 2147483647
