# Projet de Classification d'Art

Système de classification de genres artistiques combinant **machine learning en Python** et **calculs optimisés en C** pour des performances maximales.

---

## Prérequis

- **Python 3.8+**
- **GCC**
- **Make**
- **Docker** (optionnel, pour déploiement)

---

## Installation

### 1. Installer les dépendances Python

```sh
pip install -r requirements.txt
```

### 2. Compiler les bibliothèques C

*Pas besoin de le faire, c'est géré dans les notebooks*

```sh
make clean && make
```

Cela va compiler les fonctions C dans `libc/src/` et générer les bibliothèques partagées utilisables depuis Python.

### 3.1 Lancer avec Docker (Dev)
```sh
docker compose -f docker-compose.yml up -d --build
```

### 3.2 Lancer avec Docker (Production)
```sh
docker compose -f docker-compose.prod.yml up -d --build
```

---

## Architecture du Projet

### Vue d'ensemble

```
┌─────────────────────────────────────────────────────────────────┐
│                         UTILISATEUR                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                    ┌────▼────┐
                    │ Frontend│ (Vue.js)
                    │  :3000  │
                    └────┬────┘
                         │ HTTP/REST
                    ┌────▼────┐
                    │ Backend │ (Django)
                    │  :8000  │
                    └────┬────┘
                         │
            ┌────────────┴─────────────┐
            │                          │
       ┌────▼───────┐            ┌─────▼─────┐
       │---Python---│            │ Librairie │
       │   Engine   │◄───────────┤     C     │
       | classifier |            |           |
       └────────────┘            └───────────┘
            ▲
            │
       ┌────▼─────┐
       │  Modèle  │
       │ (.bin)   │
       └──────────┘
```

### Composants

#### **Engine** (`engine/`)
- **Prétraitement** : redimensionnement, normalisation des images
- **Bindings Python** : interface entre Python et les fonctions C
- **Classification** : logique de prédiction

#### **Librairie C** (`libc/`)
- **mathlib.c** : opérations matricielles optimisées
- **model.c** : algorithmes de ML (forward pass, backpropagation)
- **Compilation** : génère des `.dll`/`.so` pour performances maximales

#### **Backend** (`interface/backend/`)
- **API REST** : endpoints pour upload et prédiction
- **Traitement** : gestion des requêtes, appel au moteur de prédiction
- **Persistance** : sauvegarde des modèles et historique

#### **Frontend** (`interface/frontend/`)
- **Interface utilisateur** : drag & drop d'images
- **Dashboard** : visualisation des résultats et statistiques
- **Communication** : consommation de l'API backend

---

## Flow Fonctionnel

### Phase 1 : Entraînement (Training)

```
DATASET D'IMAGES ──┐
                   ├─> Prétraitement (Python) ──> Vecteur X ──┐
LABELS (genres) ───┘                             Vecteur Y ──┤
                                                              │
                                                              ▼
                                                    ┌──────────────────┐
                                                    │  Fonction C      │
                                                    │  train_model()   │
                                                    └────────┬─────────┘
                                                             │
                                                             ▼
                                                    Fichier POIDS.bin
```

### Phase 2 : Prédiction (Interface)

```
USER ──> Upload Image ──> Frontend ──> API Backend ──> Python (Resize/Numpy)
                                                              │
                                                              ▼
                                                       Vecteur X ──┐
                                                                   │
                                            POIDS.bin ────────────┤
                                                                   │
                                                                   ▼
                                                         ┌──────────────────┐
                                                         │  Fonction C      │
                                                         │  predict()       │
                                                         └────────┬─────────┘
                                                                  │
                                                                  ▼
USER <── Affichage Résultat <── Frontend <── JSON Response <── Genre + Score
                                                            (ex: "Cubisme" 87%)
```

---

## Utilisation

### 1. Training d'un Modèle

Ouvrir et exécuter le notebook Jupyter :

```sh
jupyter notebook notebooks/main.ipynb
```

Le notebook permet de :
- Charger et prétraiter le dataset
- Entraîner le modèle avec les fonctions C
- Sauvegarder les poids dans `models/`
- Évaluer les performances

### 2. Lancer l'Interface

#### Backend :
```sh
cd interface/backend
python manage.py runserver
```

#### Frontend :
```sh
cd interface/frontend
npm install
npm run dev
```

Accéder à l'interface : **http://localhost:3000**

### 3. Faire une Prédiction

1. Uploader une image via l'interface
2. Le système prétraite l'image
3. Le modèle C prédit le genre artistique
4. Résultat affiché avec le score de confiance

---

## Structure du Projet

```
├── engine/               # Moteur de ML Python
│   ├── bindings/         # Interfaces Python-C
│   └── core/             # Logique de classification
├── libc/                 # Bibliothèques C optimisées
│   ├── src/              # Code source C
│   └── include/          # Headers
├── interface/
│   ├── backend/          # API Django/FastAPI
│   └── frontend/         # Application Vue.js
├── models/               # Modèles entraînés (.bin)
├── notebooks/            # Jupyter notebooks (training)
├── dataset/              # Données d'entraînement
└── Makefile              # Compilation des lib C
```

---

## Déploiement Docker

```sh
# Développement
docker-compose up

# Production
docker-compose -f docker-compose.prod.yml up -d
```

---

## Documentation Additionnelle

- [Configuration Windows/MSYS2](docs/setup_windows_msys2.md)
- [Spécifications des fonctions C](libc/specs/)
- [Documentation backend](interface/backend/README.md)
- [Documentation frontend](interface/frontend/README.md)
