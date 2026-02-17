import sys
import os
import subprocess

# Add the project root to sys.path to allow imports from the engine package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_configure(config):
    """Compile puis charge la librairie C avant de lancer les tests"""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    print("\nCompilation of libc...")
    libc_path = os.path.join(project_root, 'libc')
    result = subprocess.run(
        f'make -C "{libc_path}" clean && make -C "{libc_path}"',
        shell=True,
        capture_output=True,
        text=True,
        cwd=os.path.dirname(__file__)
    )

    if result.returncode != 0:
        print(f"ERROR: Compilation failed:\n{result.stderr}")
        sys.exit(1)
    
    print("OK: Compilation succeeded.")
    
    from engine.interop.loader import Loader
    Loader.loadLibrary(
        lib_name="libc",
        lib_folder=os.path.join(project_root, "libc"),
        build_folder=os.path.join(project_root, "libc/build"),
        specs_folder=os.path.join(project_root, "libc/specs")
    )
