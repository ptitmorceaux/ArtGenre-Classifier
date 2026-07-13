import sys
import subprocess

import engine.core.config as cf
from engine.interop.loader import Loader


def compile_c_library() -> None:
    """Compile la bibliothèque C à l'aide de make."""
    if cf.CONFIG["lib"]["compile"] is False:
        print("Compilation de la bibliothèque C désactivée dans CONFIG.")
        return

    print("Compilation de la bibliothèque C...")

    try:
        result = subprocess.run(
            f"make -C {cf.CONFIG['lib']['lib_folder']} clean && make -C {cf.CONFIG['lib']['lib_folder']}",
            shell=True,
            capture_output=True,
            text=True
        )

        if result.stderr:
            print(result.stderr)

        if result.returncode != 0:
            print(f"Build failed with exit code {result.returncode}")
            sys.exit(1)
        else:
            print("Build succeeded.")

    except Exception as e:
        raise ValueError(f"Build failed: {e}")


def load_c_library() -> None:
    """Charge le Singleton Loader pour l'interopérabilité avec la bibliothèque C."""
    try:
        Loader.loadLibrary(
            lib_name=cf.CONFIG["lib"]["lib_name"],
            lib_folder=cf.CONFIG["lib"]["lib_folder"],
            build_folder=cf.CONFIG["lib"]["build_folder"],
            specs_folder=cf.CONFIG["lib"]["specs_folder"],
            dependencies_bin_folder=cf.CONFIG["lib"]["dependencies_folder"],
            seed=cf.CONFIG["lib"]["seed"]
        )
        print("Bibliothèque C chargée avec succès !")
    except Exception as e:
        if "already loaded" in str(e):
            print("✓ Bibliothèque C déjà chargée.")
        else:
            raise Exception(f"Erreur lors du chargement de la bibliothèque C : {e}")