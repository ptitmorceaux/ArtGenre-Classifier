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


/** ==========================================
 * Allocation et initialisation
 * ========================================== **/

unsigned char create_mlp(uint32_t* npl, uint32_t npl_size, MLP** res_model) {
    if (!res_model || !npl || npl_size < 2) return ERR_INVALID_PTR;
    
    MLP* model = (MLP*) malloc(sizeof(MLP));
    if (!model) return ERR_ALLOCATION_FAILED;

    // Configuration de d et L
    model->L = npl_size - 1;
    model->d = (uint32_t*) malloc(npl_size * sizeof(uint32_t));
    if (model->d) {
        free_mlp(model);
        return ERR_ALLOCATION_FAILED;
    }

    for (uint32_t i = 0; i < npl_size; i++) {
        model->d[i] = npl[i];
    }

    // Allocation des tableaux de poids, activations et deltas
    model->W = (float**) malloc((model->L + 1) * sizeof(float*));
    model->X = (float**) malloc((model->L + 1) * sizeof(float*));
    model->deltas = (float**) malloc((model->L + 1) * sizeof(float*));

    if (!model->W || !model->X || !model->deltas) {
        free_mlp(&model);
        return ERR_ALLOCATION_FAILED;
    }

    // Initialiser les pointeurs à NULL
    for (uint32_t i = 0; i <= model->L; i++) {
        model->W[i] = NULL;
        model->X[i] = NULL;
        model->deltas[i] = NULL;
    }

    // Allouer et initialiser les poids, activations et deltas pour chaque couche
    for (uint32_t l = 0; l <= model->L; l++) {
        // Allocations X et deltas
        model->X[l] = (float*) malloc(model->d[l] * sizeof(float));
        model->deltas[l] = (float*) malloc(model->d[l] * sizeof(float));

        if (!model->X[l] || !model->deltas[l]) {
            free_mlp(&model);
            return ERR_ALLOCATION_FAILED;
        }

        for (uint32_t j = 0; j < model->d[l] + 1; j++) {
            model->deltas[l][j] = 0.0f;
            if (j == 0) {
                model->X[l][j] = 1.0f; // Biais
            } else {
                model->X[l][j] = 0.0f;
            }
        }

    }
    
    *res_model = model;

    return RES_EXIT_SUCCESS;
}

unsigned char free_mlp(MLP** model_ptr) {
    /*
    Libérer la mémoire allouée pour le MLP
    */
    if (!model_ptr || !(*model_ptr)) return ERR_INVALID_PTR;

    return RES_EXIT_SUCCESS;
}