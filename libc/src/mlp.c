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
    model->W = (float***) malloc((model->L) * sizeof(float**));
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

    // Allouer et initialiser activations et deltas pour chaque couche
    for (uint32_t l = 0; l <= model->L + 1; l++) {
        // Allocations X et deltas
        model->X[l] = (float*) malloc((model->d[l] + 1) * sizeof(float));
        model->deltas[l] = (float*) malloc((model->d[l] + 1) * sizeof(float));

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

    for (uint32_t l = 0; l < model->L; l++) {
        // Allocation de W pour la couche l > 0
        uint32_t rows = model->d[l] + 1;
        uint32_t cols = model->d[l + 1];
        
        model->W[l] = (float**) malloc(rows * sizeof(float*));
        if (!model->W[l]) {
            free_mlp(&model);
            return ERR_ALLOCATION_FAILED;
        }
        for (uint32_t i = 0; i < rows; i++) {
            model->W[l][i] = (float*) malloc(cols * sizeof(float));
            
            if (!model->W[l][i]) {
                free_mlp(&model);
                return ERR_ALLOCATION_FAILED;
            }

            // On remplit les lignes des poids aléatoirements entre -1.0 et 1.0
            unsigned char status = fill_randomly_float_array(-1.0f, 1.0f, &model->W[l], cols);
            if (status != RES_EXIT_SUCCESS) {
                free_mlp(&model);
                return status;
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
    if (!model_ptr) return ERR_INVALID_PTR;    
    if (!(*model_ptr)) return RES_EXIT_SUCCESS; 

    MLP* model = *model_ptr;

    if (model->W) {
        for (uint32_t l = 0; l < model->L; l++) {
            if (!model->W[l]) continue;
            for (uint32_t i = 0; i < model->d[l] + 1; i++) {
                if (!model->W[l][i]) continue;
                free(model->W[l][i]);
                model->W[l][i] = NULL;
            }
            free(model->W[l]);
            model->W[l] = NULL;
        }
        free(model->W);
        model->W = NULL;
    }
    if (model->X) {
        for (uint32_t l = 0; l <= model->L; l++) {
            if (!model->X[l]) continue;
            free(model->X[l]);
            model->X[l] = NULL;
        }
        free(model->X);
        model->X = NULL;
    }
    if (model->deltas) {
        for (uint32_t l = 0; l <= model->L; l++) {
            if (!model->deltas[l]) continue;
            free(model->deltas[l]);
            model->deltas[l] = NULL;
        }
        free(model->deltas);
        model->deltas = NULL;
    }
    if (model->d) {
        free(model->d);
        model->d = NULL;
    }

    free(model);
    *model_ptr = NULL;

    return RES_EXIT_SUCCESS;
}

/** =========================================
 * Fonction de prédiction (Forward pass)
 * ==========================================
 */
    // FEUR

unsigned char propagate_forward_mlp(MLP* model, float* input, char is_classification) {
    if (!model || !model->W || !model->X || !input) return ERR_INVALID_PTR;

    // Remplir la couche d'entrée (Couche 0) (en laissant la case 0 pour le biais)
    for (uint32_t j = 1; j < model->d[0] + 1; j++) {
        model->X[0][j] = input[j - 1];
    }

    // Propagation couche par couche
    for (uint32_t l = 1; l < model->L + 1; l++) {
        for (uint32_t i = 1; i < model->d[l] + 1; i++) {
            float sum = 0.0f;
            for (uint32_t j = 0; j < model->d[l - 1] + 1; j++) {
                sum += model->W[l - 1][j][i - 1] * model->X[l - 1][j];
            }

            if (l < model->L || is_classification) {
                sum = tanh(sum);
            }

            model->X[l][i] = sum;
        }
    }
    return RES_EXIT_SUCCESS;
}

unsigned char predict_mlp(MLP* model, float* input, char is_classification, float* outputs) {
    if (!model || !outputs) return ERR_INVALID_PTR;

    unsigned char status = propagate_forward_mlp(model, input, is_classification);
    if (status != RES_EXIT_SUCCESS) return status;

    // Copier les activations de la couche de sortie dans output
    for (uint32_t i = 1; i <= model->d[model->L]; i++) {
        outputs[i - 1] = model->X[model->L][i];
    }

    return RES_EXIT_SUCCESS;
}


/** =========================================
 * Entraintement (Backward pass + mise à jour des poids)
 * ==========================================
 */

    // FEUR

unsigned char train_mlp(MLP* model, float* dataset_inputs, float* dataset_expected_outputs,
        uint32_t dataset_size, float alpha, uint32_t epochs, char is_classification) {
    if (!model || !dataset_inputs || !dataset_expected_outputs) return ERR_INVALID_PTR;

    uint32_t input_dim = model->d[0]; // Nombre de neurones d'entrée (sans le biais)
    uint32_t outputs_dim = model->d[model->L]; // Nombre de neurones de sortie

    // Boucle d'entraînement stochastique
    for (uint32_t i = 0; i < epochs; i++) {
        uint32_t k = random_float(0, dataset_size - 1, &k);
        float* inputs_k = &dataset_inputs[k * input_dim];
        float* y_k = &dataset_expected_outputs[k * outputs_dim];

        unsigned char status = propagate_forward_mlp(model, inputs_k, is_classification);
        if (status != RES_EXIT_SUCCESS) return status;

        // Calcul des deltas pour la couche de sortie
        for (uint32_t j = 1; j <= outputs_dim; j++) {
            model->deltas[model->L][j] = model->X[model->L][j] - y_k[j - 1];

            // Si classification, on applique la dérivée de tanh (1 - x^2)
            if (is_classification) {
                model->deltas[model->L][j] *= (1.0f - model->X[model->L][j] * model->X[model->L][j]);
            }
        }
    }

    // Backpropagation des deltas et mise à jour des poids
    for (int32_t l = model->L - 1; l >= 1; l--) {
        for (uint32_t i = 1; i <= model->d[l] + 1; i++) {
            float total_errors = 0.0f;

            // On somme (poids * deltas) pour la couche suivante (l + 1)
            for (uint32_t j = 1; j <= model->d[l + 1]; j++) {
                // W[l] connecte la couche l à l+1
                total_errors += model->W[l][i][j - 1] * model->deltas[l + 1][j];
            }

            // On multiplie par la dérivée de l'activation (tanh) pour obtenir les deltas des couches cachées
            total_errors *= (1.0f - model->X[l][i] * model->X[l][i]);

            model->deltas[l][i] = total_errors;
        }   
    }


    for (uint32_t l = 0; l < model->L; l++) {
        for (uint32_t i = 0; i <= model->d[l]; i++) {
            for (uint32_t j = 1; j <= model->d[l + 1]; j++) {
               model->W[l][i][j - 1] -= alpha * model->X[l + 1][j] * model->deltas[l][i];
            }
        }
    }

    return RES_EXIT_SUCCESS;
}