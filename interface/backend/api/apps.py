# interface/backend/api/apps.py
import os
from pathlib import Path
import platform

from engine.interop.loader import Loader

from django.apps import AppConfig
from django.conf import settings

# --- 1. DÉFINITION DES CHEMINS ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):      
            lib_name = 'libc.dll' if platform.system() == 'Windows' else 'libc.so'
            lib_folder = os.path.join(settings.PROJECT_ROOT, "libc")
            build_folder = os.path.join(settings.PROJECT_ROOT, "libc", "build")
            specs_folder = os.path.join(settings.PROJECT_ROOT, "libc", "specs")
            
            print(f"[*] Initialisation de l'interopérabilité C via _LibLoader...")
            print(f"    - Nom de la lib : {lib_name}")
            print(f"    - Dossier Build : {build_folder}")
            print(f"    - Dossier Specs : {specs_folder}")
            
            try:
                Loader.loadLibrary(
                    lib_name=lib_name,
                    lib_folder=lib_folder,
                    build_folder=build_folder,
                    specs_folder=specs_folder,
                    seed=None
                )
                print("[+] Librairie C et métadonnées chargées avec succès !")
            except Exception as e:
                print(f"[ERREUR C] Échec du chargement : {e}")
