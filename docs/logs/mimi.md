## Logs

J'ai commencé par recopier le code d'exemple de MONSIEUR ML pour comprendre comment fonctionne le C ABI.
J'ai fini par faire une classe par dll (repartition des taches -> model.dll / ...)
Ensuite j'ai cherher à optimiser / simplifier se traitement pour ne plus avoir besoin d'ecrire tout les types a la main et de centraliser le load des dll dans une seule classe :
- Creation d'une classe mere -> Loader qui permet de gérer le load d'un dll, dylib ou so.
- Ajout de fichiers json qui lisent les types des arguments et le type de retour des fonctions


## Flow du projet :

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
