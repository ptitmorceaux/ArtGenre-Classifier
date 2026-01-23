import sys
import os
import subprocess

# Ajouter le répertoire parent au path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_configure(config):
    """Compile la librairie C avant de lancer les tests"""
    print("\nCompilation de libc...")
    result = subprocess.run(
        "make -C ../libc",
        shell=True,
        capture_output=True,
        text=True,
        cwd=os.path.dirname(__file__)
    )
    
    if result.returncode != 0:
        print(f"❌ Compilation failed:\n{result.stderr}")
        sys.exit(1)
    
    print("✅ Compilation réussie")
    
    # Réinitialiser le Loader
    from engine.interop.loader import Loader
    Loader._instance = None
    Loader()
