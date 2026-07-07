"""
test_save.py

Test du pipeline save/load (storage.py) pour LinearModel + MLP + normalisation.

PRÉ-REQUIS :
- LinearModel._init_from_model_ptr, LinearModel.get_weights() (linearModel.py).
- MLP.get_weights() / MLP.set_weights() (mlp.py).
- storage.py construit la struct C de normalisation à la volée (aucun .ptr
  persistant sur StandardScaler / StandardPerColumnScaler).
- global.h doit définir ERR_FILE_READ (utilisé par load_mlp_model).
- Adapter LIB_NAME / LIB_FOLDER / BUILD_FOLDER / SPECS_FOLDER à ton environnement.
"""

import os
import random
import statistics
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from engine.interop.loader import Loader
from engine.interop.linearModel import LinearModel
from engine.interop.mlp import MLP
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


# ---------------------------------------------------------------------------
# 2. Helpers de comparaison
# ---------------------------------------------------------------------------
def assert_weights_close(actual: list[float], expected: list[float], tol: float = 1e-5):
    assert len(actual) == len(expected), f"Nombre de poids différent : {len(actual)} != {len(expected)}"
    for i, (a, e) in enumerate(zip(actual, expected)):
        assert abs(a - e) < tol, f"Poids #{i} différent : {a} != {e}"


def assert_mlp_weights_close(actual: list, expected: list, tol: float = 1e-5):
    assert len(actual) == len(expected), f"Nombre de couches différent : {len(actual)} != {len(expected)}"
    for layer_index, (layer_a, layer_e) in enumerate(zip(actual, expected)):
        assert len(layer_a) == len(layer_e), f"Couche {layer_index}: nombre de lignes différent"
        for i, (row_a, row_e) in enumerate(zip(layer_a, layer_e)):
            assert_weights_close(row_a, row_e, tol)


def assert_predictions_close(actual: list, expected: list, tol: float = 1e-4):
    assert len(actual) == len(expected), f"Nombre de prédictions différent : {len(actual)} != {len(expected)}"
    for a, e in zip(actual, expected):
        if isinstance(a, list):
            assert_weights_close(a, e, tol)
        else:
            assert abs(a - e) < tol, f"Prédiction différente : {a} != {e}"


# ---------------------------------------------------------------------------
# 3. Génération d'un faux jeu de données + split train/test + normalisation
# ---------------------------------------------------------------------------
def generate_fake_regression_dataset(
        n_samples: int,
        input_dim: int,
        true_weights: list[float],
        true_bias: float,
        noise: float = 0.01,
        seed: int = 123
    ) -> tuple[list[float], list[float]]:
    """Génère un dataset synthétique y = true_bias + true_weights . x + bruit (non normalisé)."""
    rng = random.Random(seed)
    dataset_inputs = []
    dataset_outputs = []

    for _ in range(n_samples):
        row = [rng.uniform(-1.0, 1.0) for _ in range(input_dim)]
        y = true_bias + sum(w * x for w, x in zip(true_weights, row)) + rng.uniform(-noise, noise)
        dataset_inputs.extend(row)
        dataset_outputs.append(y)

    return dataset_inputs, dataset_outputs


def split_dataset(
        dataset_inputs: list[float],
        dataset_outputs: list[float],
        input_dim: int,
        train_ratio: float = 0.7
    ) -> tuple[list[float], list[float], list[float], list[float]]:
    """Découpe un dataset aplati (row-major) en train/test, en respectant les lignes."""
    n_samples = len(dataset_outputs)
    n_train = int(n_samples * train_ratio)

    train_inputs = dataset_inputs[: n_train * input_dim]
    test_inputs = dataset_inputs[n_train * input_dim:]
    train_outputs = dataset_outputs[:n_train]
    test_outputs = dataset_outputs[n_train:]

    return train_inputs, train_outputs, test_inputs, test_outputs


def compute_per_column_stats(dataset_inputs: list[float], input_dim: int) -> tuple[list[float], list[float]]:
    """Moyenne/écart-type par colonne, calculés UNIQUEMENT sur les données passées (le train)."""
    columns = [dataset_inputs[i::input_dim] for i in range(input_dim)]
    means = [statistics.mean(col) for col in columns]
    stds = [statistics.pstdev(col) for col in columns]
    return means, stds


def normalize_flat(scaler: StandardScaler | StandardPerColumnScaler, flat_inputs: list[float], input_dim: int) -> list[float]:
    """Applique scaler.transform() sur un dataset aplati (row-major), quel que soit le type de scaler."""
    if isinstance(scaler, StandardPerColumnScaler):
        X = np.array(flat_inputs, dtype=np.float32).reshape(-1, input_dim)
        return scaler.transform(X).flatten().tolist()
    else:
        X = np.array(flat_inputs, dtype=np.float32)
        return scaler.transform(X).tolist()


def predict_rows(model: LinearModel | MLP, flat_inputs: list[float], input_dim: int, is_classification: bool = False) -> list:
    """Prédit ligne par ligne sur un dataset aplati."""
    n_samples = len(flat_inputs) // input_dim
    predictions = []
    for i in range(n_samples):
        row = flat_inputs[i * input_dim: (i + 1) * input_dim]
        predictions.append(model.predict(row, is_classification))
    return predictions


# ---------------------------------------------------------------------------
# 4. Test : LinearModel + StandardScaler
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
# 5. Test : LinearModel + StandardPerColumnScaler
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
# 6. Test : LinearModel - nom de fichier auto-généré
# ---------------------------------------------------------------------------
def test_linear_auto_filename():
    print("\n=== Test: LinearModel - nom de fichier auto-généré ===")

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


# ---------------------------------------------------------------------------
# 7. Test : MLP + StandardScaler
# ---------------------------------------------------------------------------
def test_mlp_standard():
    print("\n=== Test: MLP + STANDARD ===")

    npl = [2, 3, 1]
    model = MLP(npl)

    known_weights = [
        [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]],
        [[1.0], [1.1], [1.2], [1.3]],
    ]
    model.set_weights(known_weights)
    original_weights = model.get_weights()

    scaler = StandardScaler(mean=0.0, std=1.0)

    filename = "test_mlp_standard.bin"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)

    Storage["save"](model, scaler, OUTPUT_FOLDER, filename)
    assert os.path.isfile(filepath), "Le fichier n'a pas été créé."
    print(f"OK - fichier sauvegardé : {filepath}")

    loaded_model, loaded_scaler = Storage["load"](filepath)

    assert isinstance(loaded_model, MLP)
    assert isinstance(loaded_scaler, StandardScaler)
    assert loaded_model.npl == model.npl, f"npl différent : {loaded_model.npl} != {model.npl}"

    loaded_weights = loaded_model.get_weights()
    assert_mlp_weights_close(loaded_weights, original_weights)

    test_input = [0.5, -0.5]
    original_output = model.predict(test_input, is_classification=False)
    loaded_output = loaded_model.predict(test_input, is_classification=False)
    assert_weights_close(original_output, loaded_output)

    print(f"OK - rechargé : npl={loaded_model.npl}")
    print(f"OK - poids identiques : {loaded_weights}")
    print(f"OK - prédiction identique : {loaded_output}")


# ---------------------------------------------------------------------------
# 8. Test : MLP + StandardPerColumnScaler
# ---------------------------------------------------------------------------
def test_mlp_per_column():
    print("\n=== Test: MLP + STANDARD_PER_COLUMN ===")

    npl = [2, 3, 1]
    model = MLP(npl)

    known_weights = [
        [[0.05, -0.1, 0.15], [0.2, 0.25, -0.3], [-0.35, 0.4, 0.45]],
        [[0.5], [-0.55], [0.6], [-0.65]],
    ]
    model.set_weights(known_weights)
    original_weights = model.get_weights()

    scaler = StandardPerColumnScaler(mean=[1.0, -2.0], std=[0.5, 1.5])

    filename = "test_mlp_per_column.bin"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)

    Storage["save"](model, scaler, OUTPUT_FOLDER, filename)
    assert os.path.isfile(filepath), "Le fichier n'a pas été créé."
    print(f"OK - fichier sauvegardé : {filepath}")

    loaded_model, loaded_scaler = Storage["load"](filepath)

    assert isinstance(loaded_model, MLP)
    assert isinstance(loaded_scaler, StandardPerColumnScaler)
    assert loaded_model.npl == model.npl
    assert loaded_scaler.length == 2

    expected_mean = [1.0, -2.0]
    expected_std = [0.5, 1.5]
    for i in range(2):
        assert abs(loaded_scaler.mean[i] - expected_mean[i]) < 1e-5
        assert abs(loaded_scaler.std[i] - expected_std[i]) < 1e-5

    loaded_weights = loaded_model.get_weights()
    assert_mlp_weights_close(loaded_weights, original_weights)

    print(f"OK - rechargé : mean={loaded_scaler.mean}, std={loaded_scaler.std}")
    print("OK - poids identiques")


# ---------------------------------------------------------------------------
# 9. Test : MLP - nom de fichier auto-généré
# ---------------------------------------------------------------------------
def test_mlp_auto_filename():
    print("\n=== Test: MLP - nom de fichier auto-généré ===")

    npl = [2, 2, 1]
    model = MLP(npl)
    known_weights = [
        [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]],
        [[0.7], [0.8], [0.9]],
    ]
    model.set_weights(known_weights)
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
    assert loaded_model.npl == model.npl
    assert_mlp_weights_close(loaded_model.get_weights(), original_weights)
    print("OK - poids identiques après rechargement")


# ---------------------------------------------------------------------------
# 10. Test : LinearModel — mise en situation réaliste
#     split 70/30 -> fit scaler sur train -> transform train+test ->
#     train -> évalue sur test -> save (sans jeter `model`) -> load ->
#     compare poids + refait le test set, doit retomber pareil.
# ---------------------------------------------------------------------------
def test_train_and_save_linear_model():
    print("\n=== Test: LinearModel - entraînement réaliste (split + normalisation) ===")

    input_dim = 2
    true_weights = [2.0, 3.0]
    true_bias = 1.0

    dataset_inputs, dataset_outputs = generate_fake_regression_dataset(
        n_samples=100, input_dim=input_dim,
        true_weights=true_weights, true_bias=true_bias, seed=42
    )

    train_inputs, train_outputs, test_inputs, test_outputs = split_dataset(
        dataset_inputs, dataset_outputs, input_dim, train_ratio=0.7
    )
    print(f"Train: {len(train_outputs)} échantillons, Test: {len(test_outputs)} échantillons")

    # 1. mean/std calculés UNIQUEMENT sur le train
    means, stds = compute_per_column_stats(train_inputs, input_dim)
    scaler = StandardPerColumnScaler(mean=means, std=stds)

    # 2. On normalise train ET test avec les stats du train (scaler.transform)
    train_inputs_norm = normalize_flat(scaler, train_inputs, input_dim)
    test_inputs_norm = normalize_flat(scaler, test_inputs, input_dim)

    # 3. Entraînement sur le train normalisé
    model = LinearModel.init_random(input_dim=input_dim)
    model.train(
        dataset_inputs=train_inputs_norm,
        dataset_expected_outputs=train_outputs,
        alpha=0.01,
        epochs=200,
        is_classification=False,
    )
    weights_after_training = model.get_weights()
    print(f"Poids après entraînement : {weights_after_training}")

    # 4. Évaluation sur le test set normalisé (mise en situation), AVANT save
    predictions_before_save = predict_rows(model, test_inputs_norm, input_dim, is_classification=False)
    mse_before = sum((p - y) ** 2 for p, y in zip(predictions_before_save, test_outputs)) / len(test_outputs)
    print(f"MSE sur le test set (avant save) : {mse_before:.4f}")

    # 5. Sauvegarde — `model` n'est PAS supprimé, on le garde pour comparer après le load
    filename = "test_linear_trained.bin"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)

    Storage["save"](model, scaler, OUTPUT_FOLDER, filename)
    assert os.path.isfile(filepath), "Le fichier n'a pas été créé."
    print(f"OK - fichier sauvegardé : {filepath}")

    # 6. Rechargement
    loaded_model, loaded_scaler = Storage["load"](filepath)

    assert isinstance(loaded_model, LinearModel)
    assert isinstance(loaded_scaler, StandardPerColumnScaler)

    # 7. Comparaison des poids et de la normalisation
    loaded_weights = loaded_model.get_weights()
    assert_weights_close(loaded_weights, weights_after_training)

    for i in range(input_dim):
        assert abs(loaded_scaler.mean[i] - means[i]) < 1e-5
        assert abs(loaded_scaler.std[i] - stds[i]) < 1e-5

    # 8. On refait le test set avec le modèle + scaler rechargés -> doit retomber pareil
    test_inputs_norm_reloaded = normalize_flat(loaded_scaler, test_inputs, input_dim)
    predictions_after_load = predict_rows(loaded_model, test_inputs_norm_reloaded, input_dim, is_classification=False)

    assert_predictions_close(predictions_after_load, predictions_before_save)

    print("OK - poids identiques après reload")
    print(f"OK - normalisation identique après reload : mean={loaded_scaler.mean}, std={loaded_scaler.std}")
    print("OK - prédictions sur le test set identiques avant/après reload")


# ---------------------------------------------------------------------------
# 11. Test : MLP — même mise en situation réaliste
# ---------------------------------------------------------------------------
def test_train_and_save_mlp():
    print("\n=== Test: MLP - entraînement réaliste (split + normalisation) ===")

    input_dim = 2
    true_weights = [2.0, -1.0]
    true_bias = 0.5

    dataset_inputs, dataset_outputs = generate_fake_regression_dataset(
        n_samples=100, input_dim=input_dim,
        true_weights=true_weights, true_bias=true_bias, seed=7
    )

    train_inputs, train_outputs, test_inputs, test_outputs = split_dataset(
        dataset_inputs, dataset_outputs, input_dim, train_ratio=0.7
    )
    print(f"Train: {len(train_outputs)} échantillons, Test: {len(test_outputs)} échantillons")

    means, stds = compute_per_column_stats(train_inputs, input_dim)
    scaler = StandardPerColumnScaler(mean=means, std=stds)

    train_inputs_norm = normalize_flat(scaler, train_inputs, input_dim)
    test_inputs_norm = normalize_flat(scaler, test_inputs, input_dim)

    npl = [input_dim, 4, 1]
    model = MLP(npl)
    model.train(
        dataset_inputs=train_inputs_norm,
        dataset_expected_outputs=train_outputs,
        data_size=len(train_outputs),
        alpha=0.01,
        epochs=100,
        is_classification=False,
    )
    weights_after_training = model.get_weights()

    predictions_before_save = predict_rows(model, test_inputs_norm, input_dim, is_classification=False)
    flat_preds_before = [p[0] for p in predictions_before_save]  # MLP.predict -> liste (1 sortie ici)
    mse_before = sum((p - y) ** 2 for p, y in zip(flat_preds_before, test_outputs)) / len(test_outputs)
    print(f"MSE sur le test set (avant save) : {mse_before:.4f}")

    filename = "test_mlp_trained.bin"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)

    Storage["save"](model, scaler, OUTPUT_FOLDER, filename)
    assert os.path.isfile(filepath), "Le fichier n'a pas été créé."
    print(f"OK - fichier sauvegardé : {filepath}")

    loaded_model, loaded_scaler = Storage["load"](filepath)

    assert isinstance(loaded_model, MLP)
    assert isinstance(loaded_scaler, StandardPerColumnScaler)
    assert loaded_model.npl == model.npl

    loaded_weights = loaded_model.get_weights()
    assert_mlp_weights_close(loaded_weights, weights_after_training)

    for i in range(input_dim):
        assert abs(loaded_scaler.mean[i] - means[i]) < 1e-5
        assert abs(loaded_scaler.std[i] - stds[i]) < 1e-5

    test_inputs_norm_reloaded = normalize_flat(loaded_scaler, test_inputs, input_dim)
    predictions_after_load = predict_rows(loaded_model, test_inputs_norm_reloaded, input_dim, is_classification=False)

    assert_predictions_close(predictions_after_load, predictions_before_save)

    print("OK - poids identiques après reload")
    print(f"OK - normalisation identique après reload : mean={loaded_scaler.mean}, std={loaded_scaler.std}")
    print("OK - prédictions sur le test set identiques avant/après reload")


if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    test_linear_model_standard()
    test_linear_model_per_column()
    test_linear_auto_filename()
    test_mlp_standard()
    test_mlp_per_column()
    test_mlp_auto_filename()
    test_train_and_save_linear_model()
    test_train_and_save_mlp()

    print("\n✅ Tous les tests sont passés.")
