import ctypes
import os
import sys
import json

class Loader:
    """Load une lib partagée en singleton"""
    _instance = None

    def __new__(cls, lib_name="libc", lib_folder="libc", build_folder="libc/build", specs_folder="libc/specs"):
        if cls._instance is not None:
            return cls._instance
        
        # print("Loader: Creating new instance") # debug

        cls._instance = super(Loader, cls).__new__(cls)
        inst = cls._instance

        inst._lib = None
        inst._specs = dict()

        inst._lib_name = inst._set_lib_name(lib_name)
        inst._lib_folder = inst._set_path(lib_folder)
        inst._build_folder = inst._set_path(build_folder)
        inst._specs_folder = inst._set_path(specs_folder)
        
        inst.ext = "dll" if sys.platform.startswith("win") else "dylib" if sys.platform.startswith("darwin") else "so"
        
        inst._load_library()
        inst._load_all_json_specs()
        inst._attribute_types()

        # print("Loader: Instance created successfully") # debug
        # print(f"specs loaded:\n{inst._specs}") # debug
        
        return cls._instance


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
            raise FileNotFoundError(f"Loader._set_path(): Unable to find the path: `{path}`")
        return path


    def _load_library(self):
        """Charge la lib partagée en fct de l'os (.dll, .so, .dylib)"""
        lib_path = os.path.join(self._build_folder, f"{self._lib_name}.{self.ext}")
        
        if not os.path.exists(lib_path):
            raise FileNotFoundError(f"Loader._load_library(): Unable to find the library: `{lib_path}`")
        
        try:
            self._lib = ctypes.cdll.LoadLibrary(lib_path)
        except OSError as e:
            raise OSError(f"Loader: Failed to load library at `{lib_path}` ==> {e}")
    

    def _load_all_json_specs(self):
        """Charge tous les fichiers json du folder specs"""
        for filename in os.listdir(self._specs_folder):
            if filename.endswith(".json"):
                info_path = os.path.join(self._specs_folder, filename)
                with open(info_path, "r") as f:
                    self._specs.update(json.load(f))


    def _get_ctype(self, type: str):
        """Return le type ctypes correspondant à une string"""
        type = type.replace("const ", "").strip()
        
        structs_ptr = ("LinearModel",)
        for struct in structs_ptr:
            type = type.replace(f"{struct}*", "void*")

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

            case _: raise TypeError(f"Loader._get_ctype(): Unknow ctype: {type}")


    def _attribute_types(self):
        """Configure les types ctypes pour chaque fonction"""
        for name, info in self._specs.items():
            try:
                func = getattr(self._lib, name)
            except AttributeError:
                raise AttributeError(f"Loader.attribute_types(): Function `{name}` not found in the library")
            
            # Configuration des types d'arguments
            func.argtypes = []
            for arg_type in info["argtypes"]:
                ctype = self._get_ctype(arg_type)
                if ctype is None:
                    raise TypeError(f"Loader.attribute_types(): Unknow argtype for `{name}` : {arg_type}")
                func.argtypes.append(ctype)
            
            # Configuration du type de retour
            func.restype = self._get_ctype(info["restype"])
            if func.restype is None:
                raise TypeError(f"Loader.attribute_types(): Unknow restype for `{name}` : {info['restype']}")


    #====== Méthode public - Utils ======#

    def is_int32(self, n: int) -> bool:
        return -2147483648 <= n <= 2147483647
    
    def is_uint32(self, n: int) -> bool:
        return 0 <= n <= 4294967295

    def is_byte(self, n: int) -> bool:
        return -128 <= n <= 127

    def is_ubyte(self, n: int) -> bool:
        return 0 <= n <= 255


    def check_ctype(self, value, ctype, prefix_errmsg: str = ""):
        """Vérifie qu'une valeur correspond au type ctypes attendu"""
        prefix = f"{prefix_errmsg}: Loader.check_ctype()" if prefix_errmsg else "Loader.check_ctype()"
        errmsg = None
        
        if ctype in (ctypes.c_byte, ctypes.c_ubyte, ctypes.c_int32, ctypes.c_uint32):
            if not isinstance(value, int):
                errmsg = f"must be of type int, got {type(value)}"
        
        elif ctype == ctypes.c_float:
            if not isinstance(value, (int, float)):
                errmsg = f"must be of type float, got {type(value)}"
        
        if errmsg:
            raise TypeError(f"{prefix}: {errmsg}")

        check_map = {
            ctypes.c_byte:   (self.is_byte, f"-128 to 127 (byte)"),
            ctypes.c_ubyte:  (self.is_ubyte, f"0 to 255 (ubyte)"),
            ctypes.c_int32:  (self.is_int32, f"-2147483648 to 2147483647 (int32)"),
            ctypes.c_uint32: (self.is_uint32, f"0 to 4294967295 (uint32)"),
        }

        check_data = check_map.get(ctype)
        if check_data:
            check_func, range = check_data
            if check_func and not check_func(value):
                errmsg = f"value {value} out of bounds ({range})"
                raise ValueError(f"{prefix}: {errmsg}")


    def check_status(self, status_code: int, prefix_errmsg: str = ""):
        """Teste le status code et lève une exception si besoin"""
        prefix = f"{prefix_errmsg}: Loader.check_status()" if prefix_errmsg else "Loader.check_status()"
        self.check_ctype(status_code, ctypes.c_ubyte, prefix)
        if status_code != 0:
            errmsg = str(self._lib.get_status_message(status_code).decode('utf-8'))
            raise RuntimeError(f"{prefix}: {errmsg}")
    

    def call(self, func_name: str, *args, prefix_errmsg: str = ""):
        """Appel une fonction C et vérifie automatiquement son status code"""
        prefix = f"{prefix_errmsg}: Loader.call({func_name})" if prefix_errmsg else f"Loader.call({func_name})"
        try:
            func = getattr(self._lib, func_name)
        except AttributeError:
            raise AttributeError(f"{prefix}: Function `{func_name}` not found in the library")
        status = func(*args)
        self.check_status(status, prefix)
        return status
