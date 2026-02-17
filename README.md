# ArtGenre-Classifier 🎨

[![C Python Interop](https://img.shields.io/badge/Interop-C%20%2F%20Python-blue.svg)](https://docs.python.org/3/library/ctypes.html)
[![Project Status](https://img.shields.io/badge/Status-En%20D%C3%A9veloppement-orange.svg)]()
[![CI - Build & Pytest](https://github.com/ptitmorceaux/ArtGenre-Classifier/actions/workflows/build_pytest.yml/badge.svg)](https://github.com/ptitmorceaux/ArtGenre-Classifier/actions/workflows/build_pytest.yml)

## 📌 Présentation
ArtGenre-Classifier est un projet de classification d'œuvres d'art conçu pour identifier trois mouvements majeurs : le **Cubisme**, la **Renaissance** et le **Surréalisme**. 

La particularité de ce projet réside dans l'implémentation "from scratch" d'un moteur de Machine Learning en **C**, interfacé avec **Python** pour le traitement de données et une interface **Web** pour l'utilisateur final.

## ⚙️ Architecture Technique
Le projet est divisé en trois couches principales :

1.  **Core Engine (C)** : Implémentation bas niveau des algorithmes sans bibliothèques externes (uniquement `<math.h>`).
    * Modèles : Linéaire, Perceptron Multicouche (PMC/MLP), et Radial Basis Function (RBF).
2.  **Bridge (Python/ctypes)** : Wrapper assurant l'interopérabilité. Il gère la conversion des données Python vers les pointeurs C.
3.  **Application (Django & Vue.js)** : Une API REST et un frontend moderne permettant l'upload d'images et la visualisation des scores de confiance en temps réel.

## 🚀 Fonctionnalités
* **Calcul Matriciel Optimisé** : Fonctions C dédiées pour les opérations mathématiques.
* **Multi-modèles** : Entraînement et prédiction via Modèle Linéaire et PMC.
* **Persistance** : Sauvegarde et chargement des poids du modèle au format `.bin`.
* **Dockerisé** : Déploiement simplifié avec Docker Compose (Backend & Frontend).

## 🛠️ Installation & Compilation

### Prérequis
* GCC & Make: [Setup via MSYS2 sous Windows](./docs/setup_windows_msys2.md)
* Python 3.8+
* Docker & Docker Compose

### Compilation de la bibliothèque C
```bash
make -C libc clean && make -C libc all
```

### Lancement de l'application (Docker)

```bash
docker-compose up --build
```

## 📈 État d'avancement

* [ **x** ] Structure globale et interopérabilité (ctypes)
* [ **-** ] Implémentation du Modèle Linéaire
* [ **-** ] Finalisation du Perceptron Multicouche (PMC)
* [ **-** ] Implémentation des fonctions RBF
* [ **-** ] Dataset complet et évaluation des performances

Légende:
* [ **-** ] : pas commencé
* [ **e** ] : en cours
* [ **x** ] : fini

## 👥 Équipe (Groupe 3)

Projet Annuel réalisé dans le cadre du cursus **ESGI 3IABD 2026**