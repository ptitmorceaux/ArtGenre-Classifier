## Installation en local

### Installer les dépendances Python

```sh
pip install -r requirements.txt
```

### Compiler sur win x86_64

```sh
make
```

---

## Tests & Training

Il ne reste plus qu'à effectuer vos tests et entraînements dans [`notebooks/`](./notebooks/main.ipynb)

---

## Info

### Flow du projet :

```
TRAINING :
IMAGE -> Python (Resize/Numpy) -> Vecteur X ──┐
                                              ├─> [Fonction C : Train] ─> Fichier de POIDS (.bin)
LABELS -> Python (0, 1, 2...)  -> Vecteur Y ──┘

PRÉDICTION (API) :
NOUVELLE IMAGE -> Python (Numpy) -> Vecteur X ──┐
                                                ├─> [Fonction C : Predict] ─> Genre (ex: "Cubisme")
FICHIER DE POIDS (.bin) ────────────────────────┘
```
