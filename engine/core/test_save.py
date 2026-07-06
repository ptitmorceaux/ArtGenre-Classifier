"""
test_save.py

Test du pipeline save/load (storage.py) pour LinearModel + normalisation.

PRÉ-REQUIS :
- LinearModel._init_from_model_ptr et LinearModel.get_weights() doivent exister
  dans linearModel.py.
- storage.py doit construire la struct C de normalisation à la volée
  (_build_c_normalization_struct), StandardScaler/StandardPerColumnScaler
  n'ayant jamais de .ptr.
- Adapter LIB_NAME / LIB_FOLDER / BUILD_FOLDER / SPECS_FOLDER à ton environnement.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from engine.interop.loader import Loader
from engine.interop.linearModel import LinearModel
from engine.interop.normalization import StandardScaler, StandardPerColumnScaler
from engine.interop.storage import Storage


# ---------------------------------------------------------------------------
# 1. Chargement de la librairie C — ADAPTE CES CHEMINS
# ---------------------------------------------------------------------------
LIB_NAME = "libc"
LIB_FOLDER = r"C:\Users\milha\Documents\Ecole\2 - ESGI\3ESGI CL A ALT RO - 2025-2026\PA\ArtGenre-Classifier\libc"
BUILD_FOLDER = os.path.join(LIB_FOLDER, "build")
SPECS_FOLDER = os.path.join(LIB_FOLDER, "specs")
DEPENDENCIES_BIN_FOLDER = r"C:\msys64\mingw64\bin"
OUTPUT_FOLDER = "./test_output"

Loader.loadLibrary(
    lib_name=LIB_NAME,
    lib_folder=LIB_FOLDER,
    build_folder=BUILD_FOLDER,
    specs_folder=SPECS_FOLDER,
    dependencies_bin_folder=DEPENDENCIES_BIN_FOLDER,
    seed=42,
)


def assert_weights_close(actual: list[float], expected: list[float], tol: float = 1e-5):
    assert len(actual) == len(expected), f"Nombre de poids différent : {len(actual)} != {len(expected)}"
    for i, (a, e) in enumerate(zip(actual, expected)):
        assert abs(a - e) < tol, f"Poids #{i} différent : {a} != {e}"


# ---------------------------------------------------------------------------
# 2. Test : LinearModel + StandardScaler
# ---------------------------------------------------------------------------
def test_linear_model_standard():
    print("\n=== Test: LinearModel + STANDARD ===")

    bias = 0.5
    weights = [1.0, 2.0, 3.0]

    model = LinearModel.init_from_weights(weights, bias)
    original_weights = model.get_weights()
    print(f"Poids originaux : {original_weights}")

    scaler = StandardScaler(mean=2.5, std=1.2)

    filename = "test_linear_standard.bin"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)

    Storage["save"](model, scaler, OUTPUT_FOLDER, filename)
    assert os.path.isfile(filepath), "Le fichier n'a pas été créé."
    print(f"OK - fichier sauvegardé : {filepath}")

    loaded_model, loaded_scaler = Storage["load"](filepath)

    assert isinstance(loaded_model, LinearModel)
    assert isinstance(loaded_scaler, StandardScaler)
    assert loaded_model.input_dim == model.input_dim
    assert abs(loaded_scaler.mean - 2.5) < 1e-5
    assert abs(loaded_scaler.std - 1.2) < 1e-5

    loaded_weights = loaded_model.get_weights()
    assert_weights_close(loaded_weights, original_weights)

    print(f"OK - rechargé : input_dim={loaded_model.input_dim}, "
          f"mean={loaded_scaler.mean}, std={loaded_scaler.std}")
    print(f"OK - poids identiques : {loaded_weights}")


# ---------------------------------------------------------------------------
# 3. Test : LinearModel + StandardPerColumnScaler
# ---------------------------------------------------------------------------
def test_linear_model_per_column():
    print("\n=== Test: LinearModel + STANDARD_PER_COLUMN ===")

    bias = -0.3
    weights = [4.0, -1.5, 0.25]

    model = LinearModel.init_from_weights(weights, bias)
    original_weights = model.get_weights()
    print(f"Poids originaux : {original_weights}")

    scaler = StandardPerColumnScaler(mean=[1.0, 2.0, 3.0], std=[0.5, 0.6, 0.7])

    filename = "test_linear_per_column.bin"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)

    Storage["save"](model, scaler, OUTPUT_FOLDER, filename)
    assert os.path.isfile(filepath), "Le fichier n'a pas été créé."
    print(f"OK - fichier sauvegardé : {filepath}")

    loaded_model, loaded_scaler = Storage["load"](filepath)

    assert isinstance(loaded_model, LinearModel)
    assert isinstance(loaded_scaler, StandardPerColumnScaler)
    assert loaded_model.input_dim == model.input_dim
    assert loaded_scaler.length == 3

    expected_mean = [1.0, 2.0, 3.0]
    expected_std = [0.5, 0.6, 0.7]
    for i in range(3):
        assert abs(loaded_scaler.mean[i] - expected_mean[i]) < 1e-5
        assert abs(loaded_scaler.std[i] - expected_std[i]) < 1e-5

    loaded_weights = loaded_model.get_weights()
    assert_weights_close(loaded_weights, original_weights)

    print(f"OK - rechargé : mean={loaded_scaler.mean}, std={loaded_scaler.std}")
    print(f"OK - poids identiques : {loaded_weights}")


# ---------------------------------------------------------------------------
# 4. Test : nom de fichier auto-généré
# ---------------------------------------------------------------------------
def test_auto_filename():
    print("\n=== Test: nom de fichier auto-généré ===")

    weights = [0.1, 0.2]
    bias = 1.0
    model = LinearModel.init_from_weights(weights, bias)
    original_weights = model.get_weights()

    scaler = StandardScaler(mean=0.0, std=1.0)

    before = set(os.listdir(OUTPUT_FOLDER))
    Storage["save"](model, scaler, OUTPUT_FOLDER, None)
    after = set(os.listdir(OUTPUT_FOLDER))

    new_files = after - before
    assert len(new_files) == 1, f"Un seul fichier attendu, trouvé : {new_files}"
    new_filename = new_files.pop()
    print(f"OK - fichier auto-généré : {new_filename}")

    filepath = os.path.join(OUTPUT_FOLDER, new_filename)
    loaded_model, _ = Storage["load"](filepath)
    assert_weights_close(loaded_model.get_weights(), original_weights)
    print(f"OK - poids identiques après rechargement : {loaded_model.get_weights()}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    test_linear_model_standard()
    test_linear_model_per_column()
    test_auto_filename()

    print("\n✅ Tous les tests sont passés.")
