import ctypes
import os
import sys
import json
from typing import List
import re



def require_loaded(func):
    """Décorateur qui vérifie que la lib est bien load avant d'executer une func"""
    def wrapper(*args, **kwargs):
        if not _LibLoader._isLoaded:
            raise RuntimeError(f"{func.__name__}(): Library not loaded. Please call _LibLoader.loadLibrary() first.")
        return func(*args, **kwargs)
    return wrapper



class _LibLoader: # Singleton Pattern Design
    """Load une lib partagée en singleton"""
    _instance = None
    _isLoaded = False

    def __new__(cls):
        if _LibLoader._instance is None:
            _LibLoader._instance = super(_LibLoader, cls).__new__(cls)
        return _LibLoader._instance


    #====== Méthode privée - Init ======#

    def _set_lib_name(self, lib_name: str):
        lib_name = lib_name.replace("\\", "/").strip()
        if lib_name.endswith(".dll"):
            lib_name = lib_name[:-4]
        elif lib_name.endswith(".so"):
            lib_name = lib_name[:-3]
        elif lib_name.endswith(".dylib"):
            lib_name = lib_name[:-6]
        return lib_name

    def _set_path(self, path: str):
        path = path.strip()
        path = os.path.abspath(path)
        
        if not os.path.exists(path):
            raise FileNotFoundError(f"_LibLoader._set_path(): Unable to find the path: `{path}`")
        return path


    def _load_library(self):
        """Charge la lib partagée en fct de l'os (.dll, .so, .dylib)"""
        lib_path = os.path.join(self._build_folder, f"{self._lib_name}.{self.ext}")
        
        if not os.path.exists(lib_path):
            raise FileNotFoundError(f"_LibLoader._load_library(): Unable to find the library: `{lib_path}`")
        
        try:
            self._lib = ctypes.cdll.LoadLibrary(lib_path)
        except OSError as e:
            raise OSError(f"_LibLoader: Failed to load library at `{lib_path}` ==> {e}")
    

    def _load_all_json_specs(self):
        """Charge tous les fichiers json du folder specs"""
        for filename in os.listdir(self._specs_folder):
            if filename.endswith(".json"):
                info_path = os.path.join(self._specs_folder, filename)
                with open(info_path, "r") as f:
                    self._specs.update(json.load(f))


    def _normalize_str_type(self, type: str, structs_types_list: List[str]) -> str:
        """Normalize a C type string by removing 'const' and normalizing spaces."""
        type = re.sub(r'\s+', ' ', type).strip()
        type = type.replace("const ", "")
        type = re.sub(r'\s*\*\s*', '*', type)
        for struct in tuple(structs_types_list):
            type = type.replace(f"{struct}*", "void*")
        return type

    def _get_ctype(self, type: str):
        """Return le type ctypes correspondant à une string"""
        type = self._normalize_str_type(type, structs_types_list=[
            "LinearModel",
        ])
        match type:
            case "int32_t":         return ctypes.c_int32
            case "uint32_t":        return ctypes.c_uint32
            case "float":           return ctypes.c_float
            case "char":            return ctypes.c_byte
            case "unsigned char":   return ctypes.c_ubyte
                
            case "void*":           return ctypes.c_void_p
            case "int32_t*":        return ctypes.POINTER(ctypes.c_int32)
            case "uint32_t*":       return ctypes.POINTER(ctypes.c_uint32)
            case "float*":          return ctypes.POINTER(ctypes.c_float)
            case "char*":           return ctypes.c_char_p
            case "unsigned char*":  return ctypes.POINTER(ctypes.c_ubyte)

            case "void**":          return ctypes.POINTER(ctypes.c_void_p)
            case "float**":         return ctypes.POINTER(ctypes.POINTER(ctypes.c_float))

            case _: raise TypeError(f"_LibLoader._get_ctype(): Unknown ctype '{type}'")


    def _attribute_types(self):
        """Configure les types ctypes pour chaque fonction"""
        for name, info in self._specs.items():
            try:
                func = getattr(self._lib, name)
            except AttributeError:
                raise AttributeError(f"_LibLoader.attribute_types(): Function `{name}` not found in the library")
            
            # Configuration des types d'arguments
            func.argtypes = []
            for arg_type in info["argtypes"]:
                ctype = self._get_ctype(arg_type)
                if ctype is None:
                    raise TypeError(f"_LibLoader.attribute_types(): Unknow argtype for `{name}` : {arg_type}")
                func.argtypes.append(ctype)
            
            # Configuration du type de retour
            func.restype = self._get_ctype(info["restype"])
            if func.restype is None:
                raise TypeError(f"_LibLoader.attribute_types(): Unknow restype for `{name}` : {info['restype']}")



    #====== Méthode public - Init ======#

    def loadLibrary(self, lib_name: str, lib_folder: str, build_folder: str, specs_folder: str):
        if _LibLoader._isLoaded:
            raise RuntimeError("_LibLoader.loadLibrary(): Library is already loaded.")
        self._lib = None
        self._specs = dict()

        self._lib_name = self._set_lib_name(lib_name)
        self._lib_folder = self._set_path(lib_folder)
        self._build_folder = self._set_path(build_folder)
        self._specs_folder = self._set_path(specs_folder)
        
        if sys.platform.startswith("win"):
            self.ext = "dll"
        elif sys.platform.startswith("darwin"):
            self.ext = "dylib"
        else:
            self.ext = "so"

        self._load_library()
        self._load_all_json_specs()
        self._attribute_types()
        _LibLoader._isLoaded = True

    #====== Méthode public - Utils ======#

    @staticmethod
    def is_integer(n) -> bool:
        return isinstance(n, int) and not isinstance(n, bool)

    @staticmethod
    def is_int32(n: int) -> bool:
        return _LibLoader.is_integer(n) and -2147483648 <= n <= 2147483647
    
    @staticmethod
    def is_uint32(n: int) -> bool:
        return _LibLoader.is_integer(n) and 0 <= n <= 4294967295

    @staticmethod
    def is_byte(n: int) -> bool:
        return _LibLoader.is_integer(n) and -128 <= n <= 127

    @staticmethod
    def is_ubyte(n: int) -> bool:
        return _LibLoader.is_integer(n) and 0 <= n <= 255
    
    @staticmethod
    def is_float(n) -> bool:
        return isinstance(n, (int, float)) and not isinstance(n, bool)


    @staticmethod
    def check_ctype(value, ctype, prefix_errmsg: str = ""):
        """Vérifie qu'une valeur correspond au type ctypes attendu"""
        prefix_err = f"{prefix_errmsg}: _LibLoader.check_ctype()" if prefix_errmsg else "_LibLoader.check_ctype()"

        check_map = {
            ctypes.c_byte:   {"type_check": _LibLoader.is_integer, "type": "integer", "range_check": _LibLoader.is_byte, "range": f"-128 to 127 (byte)"},
            ctypes.c_ubyte:  {"type_check": _LibLoader.is_integer, "type": "integer", "range_check": _LibLoader.is_ubyte, "range": f"0 to 255 (ubyte)"},
            ctypes.c_int32:  {"type_check": _LibLoader.is_integer, "type": "integer", "range_check": _LibLoader.is_int32, "range": f"-2147483648 to 2147483647 (int32)"},
            ctypes.c_uint32: {"type_check": _LibLoader.is_integer, "type": "integer", "range_check": _LibLoader.is_uint32, "range": f"0 to 4294967295 (uint32)"},
            ctypes.c_float:  {"type_check": _LibLoader.is_float, "type": "float"},
        }

        if ctype not in check_map:
            raise TypeError(f"{prefix_err}: Unsupported ctype for check: {ctype}")
        
        if not check_map[ctype]["type_check"](value):
            raise TypeError(f"{prefix_err}: must be of type {check_map[ctype]['type']}, got {type(value)}")
        
        if "range_check" in check_map[ctype].keys() and not check_map[ctype]["range_check"](value):
            if "range" in check_map[ctype]:
                range_err = f": {check_map[ctype]['range']}"
            raise ValueError(f"{prefix_err}: value {value} out of bounds{range_err}")


    @require_loaded
    def check_status(self, status_code: int, prefix_errmsg: str = ""):
        """Vérifie le status code d'une fonction C et lève une exception si besoin"""
        prefix_err = f"{prefix_errmsg}: _LibLoader.check_status()" if prefix_errmsg else "_LibLoader.check_status()"
        _LibLoader.check_ctype(status_code, ctypes.c_ubyte, prefix_err)
        if status_code != 0:
            errmsg = str(self._lib.get_status_message(status_code).decode('utf-8'))
            raise RuntimeError(f"{prefix_err}: {errmsg}")


    @require_loaded
    def call(self, func_name: str, *args, prefix_errmsg: str = ""):
        """Appel une fonction C et vérifie automatiquement son status code"""
        prefix_err = f"{prefix_errmsg}: _LibLoader.call({func_name})" if prefix_errmsg else f"_LibLoader.call({func_name})"
        if func_name not in self._specs.keys():
            raise AttributeError(f"{prefix_err}: Function `{func_name}` not found in the JSON specs (missing or incorrect)")
        try:
            func = getattr(self._lib, func_name)
        except AttributeError as e:
            raise AttributeError(f"{prefix_err}: Function `{func_name}` not found in the library: {e}")
        status = func(*args)
        self.check_status(status, prefix_err)
        return status



# ====== Singleton instance ======#
Loader = _LibLoader()
