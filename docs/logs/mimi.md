## Logs

J'ai commencé par recopier le code d'exemple de MONSIEUR ML pour comprendre comment fonctionne le C ABI.

J'ai fini par faire une classe par dll/dylib/so (repartition des taches -> model.dll / ...)

Ensuite j'ai chercher à optimiser / simplifier ce traitement pour ne plus avoir besoin d'écrire tout les types à la main et de centraliser le load des dll/dylib/so dans une seule classe : Loader
- Creation d'une classe mere -> Loader qui permet de gérer le load d'un dll, dylib ou so.
- Ajout de fichiers json qui lisent les types des arguments et le type de retour des fonctions

J'ai mis au moins 2h a tenter de tout renommer / ranger dans des folders pour avoir une bonne base pour la suite du PA.

Ajout de la compilation de la `libc` au début des notebooks (permet d'être sur d'avoir les bons dll/dylib/so)
