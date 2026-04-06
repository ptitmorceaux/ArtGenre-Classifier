#include "../include/mlp.h"

/** ==========================================
 * Structure for a Multi-Layer Perceptron (MLP)
 * ========================================== **/
/*
    # Architecture d'un réseau de neurones multicouches (MLP) : 
        - d      : Tableau contenant le nombre de neurones par couche (ex: [2, 2, 1] -> 2 entrées, 2 cachés, 1 sortie).
        - L      : L'index de la dernière couche (si on a 3 couches, L = 2). Cela correspond au nombre de "sauts" de poids.
        - W      : Poids du modèle. Relie les neurones de la couche l-1 à la couche l.
        - X      : Activations. L'état (la valeur) de chaque neurone dans chaque couche.
        - deltas : Les gradients (erreurs) de chaque neurone, utilisés uniquement pour l'entraînement.

    # Implémentation en C :
        - La dimension 1 (l) indique la couche.
        - La dimension 2 contiendra un tableau en une dimension (genre 1D, applatit quoi).
        
        Le Biais est à la case 0 de chaque couche d'activation, (X[l][0]) est le neurone de Biais. 
        Sa valeur est toujours initialisée à 1.0.
*/


