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

/////////

--> rangement: Makefile dans ./libc/ mtn

Ok dcp mtn on a tt les types de base qui fonctionnent bien.
Mtn faut voir la gestion de tableau entre le C et le python (moins trivial).

Je vais tenter de manipuler le script LinearModel du prof (en c et non en cpp dcp).

- Deja pour la structure LinearModel on va dire qu'on passe en paramettre un ptr void (voir loader.py: def _get_ctype(self, type: str) -> structs_ptr)

Pour la gestion des tableaux je vais tout centraliser dans un file array.c / array.json / array.py

J'ai divisé le .c en 2 parties : la gestion mémoire (alloc et free) et les operations (aucun alloc/free)

OK ALORS:
Pour le moment je suis parti du principe que on fait les allocations en python -> AUCUNE ALLOC NI FREE EN C: gestion de ptr de tab venant de Python (qui gere les siens).

Bon j'en ai marre d'appeler tt le temps Loader.check_status(status_code, prefix_errmsg) avant chaque appel de fct de la lib c donc je vais juste faire un bon vieux wrapper -> Loader.call(self, func_name: str, *args, prefix_errmsg: str = "")

reglage de qq pbl + mise en place de c_uint32 pour les length des array.

////////

Jusqu'a mtn je faisais tout plein de test pour voir si l'implémentation fonctionnait bien sur des ipynb mais ca devient bcp trop long a voir, donc je vais passer a pytest.