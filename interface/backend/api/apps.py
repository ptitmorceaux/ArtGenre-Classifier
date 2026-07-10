import os
import sys
from django.apps import AppConfig
from engine.interop.loader import Loader
from engine.core.config import CONFIG

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        if 'runserver' not in sys.argv:
            return

        if not CONFIG:
            print("Attention: CONFIG n'a pas pu être chargé.")
            return

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        
        libc_folder = os.path.join(base_dir, CONFIG["lib"]["lib_folder"])
        build_folder = os.path.join(base_dir, CONFIG["lib"]["build_folder"])
        specs_folder = os.path.join(base_dir, CONFIG["lib"]["specs_folder"])
        
        try:
            Loader.loadLibrary(
                lib_name=CONFIG["lib"]["lib_name"],
                lib_folder=libc_folder,
                build_folder=build_folder,
                specs_folder=specs_folder,
                dependencies_bin_folder=CONFIG["lib"]["dependencies_folder"]
            )
            print("Librairie C et specs JSON chargées avec succès pour l'API.")
        except RuntimeError as e:
            if "already loaded" not in str(e).lower():
                print(f"Erreur de chargement de la libc : {e}")
