import matplotlib.pyplot as plt
import sys
import os
import subprocess
import numpy as np

# ========================================================
# 1. Compilation de la librairie C
# ========================================================
sys.path.append(os.path.abspath(os.path.join('..')))
try:
    result = subprocess.run(
        "make -C ../libc clean && make -C ../libc",
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
    print(f"Build failed: {e}")
    sys.exit(1)


# ========================================================
# 2. Chargement via le Loader
# ========================================================
from engine.interop.loader import Loader

try:
    Loader.loadLibrary(
        lib_name="libc",
        lib_folder="../libc",
        build_folder="../libc/build",
        specs_folder="../libc/specs",
        seed=None
    )
except Exception as e:
    if "already loaded" not in str(e).lower():
        raise RuntimeError(f"Failed to load library: {e}")
    print("Library already loaded, skipping.")

from engine.interop.rbf import RBF 


# ========================================================
# 3. Utilitaire de visualisation (Frontière de décision)
# ========================================================
def plot_decision_boundary(model, X, Y, title="Frontière de Décision"):
    """
    Affiche les points de données et colorie le fond selon la prédiction du modèle.
    """
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    
    # On crée une grille de points
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05),
                         np.arange(y_min, y_max, 0.05))
    
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    
    # On fait prédire le modèle sur toute la grille
    predictions = []
    for point in grid_points:
        pred = model.predict(point.tolist())
        predictions.append(pred)
        
    Z = np.array(predictions).reshape(xx.shape)
    
    # Affichage avec Matplotlib
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.coolwarm)
    plt.title(title)
    plt.show()


# ========================================================
# 4. Pipeline de Tests
# ========================================================
def run_tests():
    
    print("\n====================================")
    print("     TEST 1 : Problème XOR")
    print("====================================")
    
    # Dataset XOR : Problème non-linéaire de base
    X_xor = np.array([[1, 0], [0, 1], [0, 0], [1, 1]], dtype=np.float32)
    Y_xor = np.array([1, 1, -1, -1], dtype=np.float32)
    
    # Création du modèle RBF
    # On a 4 points d'entrée, on peut prendre k=4 centres (interpolation parfaite)
    rbf_xor = RBF(input_dim=2, num_centers=4)
    
    # Entraînement
    rbf_xor.train(
        dataset_inputs=X_xor.flatten().tolist(),
        dataset_expected_outputs=Y_xor.flatten().tolist(),
        data_size=len(X_xor),
        alpha=0.01,
        epochs=1000
    )
    
    # Affichage des prédictions dans la console
    for i in range(len(X_xor)):
        pred = rbf_xor.predict(X_xor[i].tolist())
        print(f"Entrée: {X_xor[i]} | Attendu: {Y_xor[i]:.0f} | Prédit: {pred}")
        
    # Dessin du résultat
    plot_decision_boundary(rbf_xor, X_xor, Y_xor, title="RBF - Résolution du XOR")
    
    
    print("\n====================================")
    print("     TEST 2 : Problème CROSS")
    print("====================================")
    
    # Dataset Cross : Données générées aléatoirement en forme de croix
    X_cross = np.random.random((500, 2)) * 2.0 - 1.0
    Y_cross = np.array([1 if abs(p[0]) <= 0.3 or abs(p[1]) <= 0.3 else -1 for p in X_cross], dtype=np.float32)
    
    # Création du modèle RBF
    # Pour un problème plus complexe (500 points), on utilise plus de centres (ex: k=30)
    rbf_cross = RBF(input_dim=2, num_centers=30)
    
    print("Entraînement en cours sur 500 points (Cross dataset)...")
    rbf_cross.train(
        dataset_inputs=X_cross.flatten().tolist(),
        dataset_expected_outputs=Y_cross.flatten().tolist(),
        data_size=len(X_cross),
        alpha=0.01,
        epochs=1500
    )
    
    # Dessin du résultat
    print("Affichage de la frontière de décision...")
    plot_decision_boundary(rbf_cross, X_cross, Y_cross, title="RBF - Résolution du Cross")


if __name__ == "__main__":
    run_tests()