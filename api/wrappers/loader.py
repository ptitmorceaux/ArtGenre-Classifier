import ctypes
import os
import sys
import json

def load_library(lib_folder: str, build_folder: str, basename: str) -> ctypes.CDLL:
    """
    Charge une bibliothèque partagée (.dll, .so, .dylib)
    de manière transparente selon l'OS.
    """
    
    # Détection de l'extension
    if sys.platform.startswith("win"):
        ext = "dll"
    elif sys.platform.startswith("darwin"):
        ext = "dylib"
    else:
        ext = "so"
    
    lib_path = os.path.join(lib_folder, build_folder, f"{basename}.{ext}")
    print(f"Chargement de la bibliothèque: {lib_path}")
    
    if not os.path.exists(lib_path):
        raise FileNotFoundError(f"Impossible de trouver la bibliothèque: {lib_path}")
    
    return ctypes.CDLL(lib_path)


def load_lib_json_specs(lib_folder: str, specs_folder: str, basename: str) -> dict:
    """Charge le fichier json décrivant les fonctions de la lib"""
    info_path = os.path.join(lib_folder, specs_folder, f"{basename}.json")
    if not os.path.exists(info_path):
        raise FileNotFoundError(f"Impossible de trouver le json: {info_path}")
    with open(info_path, "r") as f:
        return json.load(f)


def init_library(lib_folder: str, build_folder: str, specs_folder: str, basename: str) -> ctypes.CDLL:
    """Charge la lib et configure les types ctypes pour chaque fonction"""
    lib = load_library(lib_folder, build_folder, basename)
    functions = load_lib_json_specs(lib_folder, specs_folder, basename)
    for name, info in functions.items():
        func = getattr(lib, name)
        
        # Configuration des types d'arguments
        argtypes = []
        for arg_type in info["argtypes"]:
            match arg_type:
                case "double":  argtypes.append(ctypes.c_double)
                case "int32_t": argtypes.append(ctypes.c_int32)
                case "char*":   argtypes.append(ctypes.c_char_p)
                case "double*": argtypes.append(ctypes.POINTER(ctypes.c_double))
                case _: raise TypeError(f"Type d'argument inconnu : {arg_type}")
        
        func.argtypes = argtypes
        
        # Configuration du type de retour
        ret_type = info["restype"]
        match ret_type:
            case "int32_t": func.restype = ctypes.c_int32
            case "char*":   func.restype = ctypes.c_char_p
            case _: raise TypeError(f"Type de retour inconnu : {ret_type}")
    
    return lib