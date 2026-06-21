# interface/backend/api/apps.py
import os
import platform

from engine.interop.loader import _LibLoader

from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        if not _LibLoader._isLoaded:
            # 1. Détection du nom du binaire selon l'OS (tu utilises libc.dll sous windows)
            system = platform.system()
            if system == "Windows":
                lib_name = "libc.dll"
            elif system == "Darwin":
                lib_name = "libc.dylib"
            else:
                lib_name = "libc.so"
                
            lib_folder = os.path.join(settings.PROJECT_ROOT, "libc")
            build_folder = os.path.join(settings.PROJECT_ROOT, "libc", "build")
            specs_folder = os.path.join(settings.PROJECT_ROOT, "libc", "specs")
            
            print(f"[*] Initialisation de l'interopérabilité C via _LibLoader...")
            print(f"    - Nom de la lib : {lib_name}")
            print(f"    - Dossier Build : {build_folder}")
            print(f"    - Dossier Specs : {specs_folder}")
            
            try:
                loader = _LibLoader()
                loader.loadLibrary(
                    lib_name=lib_name,
                    lib_folder=lib_folder,
                    build_folder=build_folder,
                    specs_folder=specs_folder
                )
                print("[+] Librairie C et métadonnées chargées avec succès !")
            except Exception as e:
                print(f"[-] Erreur critique lors de l'initialisation de la lib C : {e}")