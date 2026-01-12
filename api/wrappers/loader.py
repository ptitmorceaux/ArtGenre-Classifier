import ctypes
import os
import sys

def load_library(dll_folder, dll_basename):
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
    
    lib_path = os.path.join(dll_folder, ext, f"{dll_basename}.{ext}")
    print(f"Chargement de la bibliothèque : {lib_path}")
    
    if not os.path.exists(lib_path):
        raise FileNotFoundError(f"Impossible de trouver la bibliothèque : {lib_path}")
    
    return ctypes.CDLL(lib_path)