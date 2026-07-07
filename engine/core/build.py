import sys
import subprocess

from engine.core.config import CONFIG
from engine.interop.loader import Loader


def compile_c_library() -> None:
    """Compile la bibliothèque C à l'aide de make."""
    if CONFIG["lib"]["compile"] is False:
        print("Compilation de la bibliothèque C désactivée dans CONFIG.")
        return

    print("Compilation de la bibliothèque C...")

    try:
        result = subprocess.run(
            f"make -C {CONFIG['lib']['lib_folder']} clean && make -C {CONFIG['lib']['lib_folder']}",
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
            lib_name=CONFIG["lib"]["lib_name"],
            lib_folder=CONFIG["lib"]["lib_folder"],
            build_folder=CONFIG["lib"]["build_folder"],
            specs_folder=CONFIG["lib"]["specs_folder"],
            dependencies_bin_folder=CONFIG["lib"]["dependencies_folder"],
            seed=CONFIG["lib"]["seed"]
        )
        print("Bibliothèque C chargée avec succès !")
    except Exception as e:
        if "already loaded" in str(e):
            print("✓ Bibliothèque C déjà chargée.")
        else:
            raise Exception(f"Erreur lors du chargement de la bibliothèque C : {e}")