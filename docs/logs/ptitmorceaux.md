## Logs

J'ai commencé par recopier le code d'exemple de MONSIEUR ML pour comprendre comment fonctionne le C ABI.

J'ai fini par faire une classe par dll/dylib/so (repartition des taches -> model.dll / ...)

Ensuite j'ai chercher à optimiser / simplifier ce traitement pour ne plus avoir besoin d'écrire tout les types à la main et de centraliser le load des dll/dylib/so dans une seule classe : Loader
- Creation d'une classe mere -> Loader qui permet de gérer le load d'un dll, dylib ou so.
- Ajout de fichiers json qui lisent les types des arguments et le type de retour des fonctions

J'ai mis au moins 2h a tenter de tout renommer / ranger dans des folders pour avoir une bonne base pour la suite du PA.

Ajout de la compilation de la `libc` au début des notebooks (permet d'être sur d'avoir les bons dll/dylib/so)

///////

Réorganisation de la libc : les erreurs sont traités dans un fichier distinc et mtn on ne génére plus qu'une seule lib (avant 1 par file c)

Python : création d'une fonction pour verifier de l'integrité un type (de ses limites)
-> J'ai cherché un moyen de ne pas dupliquer mon loader dans à chaque nouveau fichier de mon interop et:
il y a un pattern objet (Singleton pattern) qui permet de n'instencier qu'une seule fois le loader dans tout le projet (les autres classes n'herite plus de loader mais on un self.loader = Loader() ).

Je viens de comprendre que ça ne sert à rien la POO pour des fonctions qui n'ont rien à instancier (par exemple une class Math sert a rien, c'est juste des fonctions ou la prog fonctionnelle suffit). En revanche pour toutes les fonctions / variables / struct avec gestions de ptr comme LinearModel là ce serait peut etre intéressant.

GROS PBL ALED : mtn on dirait que le cargs ne s'est plus mis dcp 10 + 5 ça fait pas 15 o-o :
```py
print(math.addition(10, 5)) = 2.1019476964872256e-44
```
Ok je suis fou c'est pcque je suis passé de double à float en C.... dcp ba les float en py sont des float64.... Il faut les cast en float32 sinon ca fonctionne pas (ca fait 1 je bug sur ca ptn)...