import os
import sys
from django.apps import AppConfig
from engine.interop.loader import Loader

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        if 'makemigrations' in sys.argv or 'migrate' in sys.argv:
            return

        # On remonte à la racine du projet (ArtGenre-Classifier)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        
        libc_folder = os.path.join(base_dir, "libc")
        build_folder = os.path.join(base_dir, "libc", "build")
        specs_folder = os.path.join(base_dir, "libc", "specs")
        
        deps_folder = None if os.name == 'posix' else r"C:\msys64\mingw64\bin"
        
        try:
            Loader.loadLibrary(
                lib_name="libc",
                lib_folder=libc_folder,
                build_folder=build_folder,
                specs_folder=specs_folder,
                dependencies_bin_folder=deps_folder
            )
            print("Librairie C et specs JSON chargées avec succès pour l'API.")
        except Exception as e:
            if "already loaded" not in str(e).lower():
                print(f"Erreur de chargement de la libc : {e}")
