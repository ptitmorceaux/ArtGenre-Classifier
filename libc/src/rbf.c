#include "../include/rbf.h"

/** ==========================================
 * Structure for a Radial Basis Function (RBF) Network
 * ========================================== **/
/*
    # Architecture d'un réseau de neurones à fonctions de base radiale (RBF) : 
        - input_dim : Dimension de chaque vecteur d'entrée (ex: nombre de pixels).
        - num_centers : Nombre de centres (neurones cachés).
        - gamma : Paramètre de variance (rayon d'action) de la fonction gaussienne.
        - centers : Tableau aplati des coordonnées des centres [num_centers * input_dim].
        - output_layer : Un modèle linéaire classique (Perceptron) utilisé comme couche de sortie.

    # Principe mathématique :
        Au lieu de séparer l'espace avec des droites, le RBF mesure la distance 
        entre une donnée d'entrée X et des "points de repère" (les centres C).
        La sortie est une somme pondérée des activations gaussiennes :
        Sortie = Somme( Poids_i * exp(-gamma * distance(X, C_i)^2) ) + Biais
*/

// Calcule la distance euclidienne entre deux points de dimension `dim`
unsigned char euclidean_distance(float* a, float* b, uint32_t dim, float* result) {
    float sum = 0.0f;
    for (uint32_t i = 0; i < dim; i++) {
        float diff = a[i] - b[i];
        sum += diff * diff;
    }

    *result = sqrtf(sum);
    return RES_EXIT_SUCCESS;
}

/** ==============================================
 * Algorithme de K-Means (Apprentissage Non Supervisé)
 * ===============================================
**/
/*
    # Objectif : 
        Trouver `k` centres représentatifs de la distribution des données d'entrée.
    
    # Algorithme de Lloyd :
        1. Initialisation : Prendre les `k` premiers points du dataset comme centres initiaux.
        2. Répéter jusqu'à convergence (ou max_iters) :
            - Étape 1 (Assignation) : Pour chaque point, trouver le centre le plus proche.
            - Étape 2 (Mise à jour) : Recalculer la position de chaque centre en 
                                      prenant la moyenne des points qui lui sont assignés.
*/

unsigned char rbf_kmeans(float* points, uint32_t num_points, uint32_t input_dim, uint32_t k, float* out_centers, uint32_t max_iters) {
    // Tableaux pour stocker l'index du cluster de chaque point et la taille de chaque cluster
    uint32_t* assignments = (uint32_t*)malloc(num_points * sizeof(uint32_t));
    uint32_t* cluster_sizes = (uint32_t*)malloc(k * sizeof(uint32_t));

    if (!assignments || !cluster_sizes) {
        free(assignments);
        free(cluster_sizes);
        return ERR_MEMORY_ALLOCATION;
    }

    // Initialisation naïve : on place les centres sur les k premiers points
    for (uint32_t i = 0; i < k; i++) {
        for (uint32_t d = 0; d < input_dim; d++) {
            out_centers[i * input_dim + d] = points[i * input_dim + d];
        }
    }

    unsigned char converged = 0;
    uint32_t iter = 0;

    while (!converged && iter < max_iters) {
        converged = 1;
        
        /** ==========================================================
         * Etape 1 : Assigner chaque point à son centre le plus proche
         * =========================================================== 
        **/
        for (uint32_t i = 0; i < num_points; i++) {
            float min_dist = MAX_FLOAT;
            uint32_t closest_center = 0;

            for (uint32_t j = 0; j < k; j++) {
                float dist = 0.0f;
                unsigned char status = euclidean_distance(&points[i * input_dim], &out_centers[j * input_dim], input_dim, &dist);

                if (status != RES_EXIT_SUCCESS) {
                    free(assignments);
                    free(cluster_sizes);
                    return status;
                }

                if (status == RES_EXIT_SUCCESS && dist < min_dist) {
                    min_dist = dist;
                    closest_center = j;
                }
            }

            // Si un point change de cluster, on n'a pas encore convergé
            if (assignments[i] != closest_center) {
                converged = 0;
                assignments[i] = closest_center;
            }
        }

        if (converged) break;

        /** ==============================================
         * Etape 2 : Recalculer les centres des clusters (Moyennes)
         * ===============================================
        **/
        
        // Remise à zéro avant de faire les sommes
        for (uint32_t i = 0; i < k * input_dim; i++) {
            out_centers[i] = 0.0f;
        }

        for (uint32_t i = 0; i < k; i++) {
            cluster_sizes[i] = 0;
        }

        // Somme des coordonnées de tous les points pour chaque cluster
        for (uint32_t i = 0; i < num_points; i++) {
            uint32_t cluster_id = assignments[i];
            cluster_sizes[cluster_id]++;
            for (uint32_t d = 0; d < input_dim; d++) {
                out_centers[cluster_id * input_dim + d] += points[i * input_dim + d];
            }
        }

        // Division par la taille du cluster pour obtenir la vraie moyenne géométrique
        for (uint32_t j = 0; j < k; j++) {
            if (cluster_sizes[j] > 0) {
                for (uint32_t d = 0; d < input_dim; d++) {
                    out_centers[j * input_dim + d] /= (float)cluster_sizes[j];
                }
            }
        }
        iter++;            
    }

    free(assignments);
    free(cluster_sizes);

    return RES_EXIT_SUCCESS;
}

/** ==============================================
 * Creation d'un réseau RBF
 * ===============================================
**/

unsigned char create_rbf(uint32_t input_dim, uint32_t num_centers, float gamma, RBF** res_model) {
    if (!res_model) return ERR_INVALID_PTR;

    RBF* model = (RBF*) malloc(sizeof(RBF));
    if (!model) return ERR_MEMORY_ALLOCATION;

    model->input_dim = input_dim;
    model->num_centers = num_centers;
    model->gamma = gamma;

    // Allocation du tableau plat pour les centres
    model->centers = (float*) calloc(num_centers * input_dim, sizeof(float));
    if (!model->centers) {
        free(model);
        return ERR_MEMORY_ALLOCATION;
    }

    // Création de la couche de sortie : un modèle linéaire dont l'entrée est de taille `num_centers`
    model->output_layer = NULL;
    unsigned char status = create_linear_model_randomly(num_centers, &(model->output_layer));
    if (status != RES_EXIT_SUCCESS) {
        free(model->centers);
        free(model);
        return status;
    }

    *res_model = model;
    return RES_EXIT_SUCCESS;
}


/** ==============================================
 * Libération de la mémoire d'un réseau RBF
 * ===============================================
*/

unsigned char free_rbf(RBF** model_ptr) {
    if (!model_ptr) return ERR_INVALID_PTR;
    if (!(*model_ptr)) return RES_EXIT_SUCCESS;

    RBF* model = *model_ptr;

    if (model->centers) {
        free(model->centers);
        model->centers = NULL;
    }

    if (model->output_layer) {
        free_linear_model(&(model->output_layer));
        model->output_layer = NULL;
    }

    free(model);
    *model_ptr = NULL;

    return RES_EXIT_SUCCESS;
}


/** ==============================================
 * Calcul des activations de la couche cachée (Fonction interne)
 * ===============================================
**/
/*
    # Formule pour chaque centre i : activation_i = exp(-gamma * distance(input, centre_i)^2)
    # Identique en classification et en régression -> factorisé ici pour ne pas dupliquer
    # ce calcul dans predict_rbf() et predict_rbf_regression().
*/
static unsigned char _rbf_compute_hidden_activations(RBF* model, float* input, float* out_activations) {
    if (!model || !input || !out_activations) return ERR_INVALID_PTR;

    for (uint32_t i = 0; i < model->num_centers; i++) {
        float dist = 0.0f;
        unsigned char status = euclidean_distance(&input[0], &model->centers[i * model->input_dim], model->input_dim, &dist);
        if (status != RES_EXIT_SUCCESS) return status;

        out_activations[i] = expf(-model->gamma * dist * dist);
    }
    return RES_EXIT_SUCCESS;
}


/** ==============================================
 * Fonction de Prédiction (Forward Pass)
 * ===============================================
*/
/*
    # Comment le RBF prédit-il un résultat ?
        1. Transformer l'entrée : On calcule l'activation de chaque neurone caché (centre)
           avec la fonction gaussienne : activation = exp(-gamma * distance^2).
        2. Modèle linéaire : On donne ces activations au modèle de régression/classification 
           linéaire qui fera une somme pondérée (W * activations + biais).
*/
unsigned char predict_rbf(RBF* model, float* input, int32_t* outputs) {
    if (!model || !outputs) return ERR_INVALID_PTR;

    // Tableau pour stocker l'activation de chaque centre (de taille `num_centers`)
    float* hidden_activations = (float*) malloc(model->num_centers * sizeof(float));
    if (!hidden_activations) return ERR_MEMORY_ALLOCATION;

        // Étape 1 : Calcul des activations gaussiennes (espace transformé)
    unsigned char status = _rbf_compute_hidden_activations(model, input, hidden_activations);
    if (status != RES_EXIT_SUCCESS) {
        free(hidden_activations);
        return status;
    }

    // Étape 2 : On passe le relais à la couche de classification linéaire (-1 ou 1)
    status = predict_linear_classification(model->output_layer, hidden_activations, outputs);
    
    free(hidden_activations);
    return status;
}


/** ==============================================
 * Fonction de Prédiction en Régression (Forward Pass)
 * ===============================================
*/
/*
    # Différence avec predict_rbf() : le calcul des activations cachées (Étape 1) est
    # identique. Seule la couche de sortie change : on renvoie la valeur continue via
    # predict_linear_regression au lieu de la classe (-1/1).
*/
unsigned char predict_rbf_regression(RBF* model, float* input, float* output) {
    if (!model || !output) return ERR_INVALID_PTR;

    float* hidden_activations = (float*) malloc(model->num_centers * sizeof(float));
    if (!hidden_activations) return ERR_MEMORY_ALLOCATION;

    // Étape 1 : Calcul des activations gaussiennes (identique à la classification)
    unsigned char status = _rbf_compute_hidden_activations(model, input, hidden_activations);
    if (status != RES_EXIT_SUCCESS) {
        free(hidden_activations);
        return status;
    }

    // Étape 2 : On passe le relais à la couche de régression linéaire (valeur continue)
    status = predict_linear_regression(model->output_layer, hidden_activations, output);

    free(hidden_activations);
    return status;
}


/** ==============================================
 * Fonction d'entraînement global
 * ===============================================
*/
/*
    # Algorithme d'apprentissage hybride en 3 phases :
        - Phase 1 (Non Supervisé) : Utilisation des K-Means pour placer judicieusement 
          les centres (balises) là où les données sont denses.
        
        - Phase 2 (Heuristique) : Calcul dynamique de Gamma (rayon d'action). 
          On cherche la distance maximale entre deux centres pour ajuster la variance 
          des gaussiennes afin qu'elles se chevauchent de manière optimale.
          Puis, transformation de tout le dataset d'entrée dans le nouvel espace des distances.

        - Phase 3 (Supervisé) : Apprentissage des poids de la couche de sortie. 
          Les données transformées sont envoyées à l'algorithme de Rosenblatt du modèle linéaire.
*/
unsigned char train_rbf(RBF* model, float* dataset_inputs, float* dataset_expected_outputs,
        uint32_t dataset_size, float alpha, uint32_t epochs) {
    
    if (!model || !dataset_inputs || !dataset_expected_outputs) return ERR_INVALID_PTR;

    // ==============================================================================
    // PHASE 1 : Entraînement non supervisé (Trouver la position des centres)
    // ==============================================================================
    unsigned char status = rbf_kmeans(dataset_inputs, dataset_size, model->input_dim, model->num_centers, model->centers, 100);
    if (status != RES_EXIT_SUCCESS) return status;

    // ==============================================================================
    // PHASE 2 : Ajustement de Gamma et Transformation du dataset
    // ==============================================================================
    
    // a. Calcul heuristique du Gamma : gamma = 1 / (2 * sigma^2)
    //    où sigma est calculé à partir de la distance maximale (dmax) entre deux centres.
    float dmax = 0.0f;
    for (uint32_t i = 0; i < model->num_centers; i++) {
        for (uint32_t j = i + 1 ; j < model->num_centers; j++) {
            float dist = 0.0f;
            status = euclidean_distance(&model->centers[i * model->input_dim], &model->centers[j * model->input_dim], model->input_dim, &dist);
            if (dist > dmax) dmax = dist;
        }
    }

    // Si un seul centre (dmax == 0), on retombe sur une valeur par défaut pour éviter une division par zéro
    float sigma = (dmax == 0.0f) ? 1.0f : (dmax / sqrtf(2.0f * (float)model->num_centers));
    model->gamma = 1.0f / (2.0f * sigma * sigma);

    // b. Transformation de l'espace (Matrice Phi)
    //    On transforme la matrice [dataset_size * input_dim] en [dataset_size * num_centers]
    float* transformed_inputs = (float*) malloc(dataset_size * model->num_centers * sizeof(float));
    if (!transformed_inputs) return ERR_MEMORY_ALLOCATION;

    for (uint32_t i = 0; i < dataset_size; i++) {
        for (uint32_t j = 0; j < model->num_centers; j++) {
            float dist = 0.0f;
            status = euclidean_distance(&dataset_inputs[i * model->input_dim], &model->centers[j * model->input_dim], model->input_dim, &dist);
            if (status != RES_EXIT_SUCCESS) {
                free(transformed_inputs);
                return status;
            }
            // Application de la fonction d'activation de base radiale
            transformed_inputs[i * model->num_centers + j] = expf(-model->gamma * dist * dist);
        }
    }

    // ==============================================================================
    // PHASE 3 : Entraînement supervisé (Règle de Rosenblatt sur la couche de sortie)
    // ==============================================================================
    status = train_linear_classification(
        model->output_layer,
        transformed_inputs,
        dataset_expected_outputs,
        dataset_size,
        alpha,
        epochs,
        NULL, // loss_history : pas de suivi de l'historique pour l'instant
        NULL // accuracy_history : idem
    );

    free(transformed_inputs);
    return status;
}

/** ==============================================
 * Fonction d'entraînement globale - Régression
 * ===============================================
*/
/*
    # Mêmes 3 phases que train_rbf(), seule la Phase 3 change :
        - Phase 1 (Non Supervisé) : K-Means pour placer les centres.
        - Phase 2 (Heuristique) : Calcul de Gamma + transformation en matrice Phi.
        - Phase 3 (Supervisé) : Descente de gradient stochastique (régression) au lieu
          de la règle de Rosenblatt, pour apprendre à prédire une valeur continue.
*/
unsigned char train_rbf_regression(RBF* model, float* dataset_inputs, float* dataset_expected_outputs,
        uint32_t dataset_size, float alpha, uint32_t epochs) {

    if (!model || !dataset_inputs || !dataset_expected_outputs) return ERR_INVALID_PTR;

    // ==============================================================================
    // PHASE 1 : Entraînement non supervisé (Trouver la position des centres)
    // ==============================================================================
    unsigned char status = rbf_kmeans(dataset_inputs, dataset_size, model->input_dim, model->num_centers, model->centers, 100);
    if (status != RES_EXIT_SUCCESS) return status;

    // ==============================================================================
    // PHASE 2 : Ajustement de Gamma et Transformation du dataset
    // ==============================================================================

    // a. Calcul heuristique du Gamma : gamma = 1 / (2 * sigma^2)
    //    où sigma est calculé à partir de la distance maximale (dmax) entre deux centres.
    float dmax = 0.0f;
    for (uint32_t i = 0; i < model->num_centers; i++) {
        for (uint32_t j = i + 1; j < model->num_centers; j++) {
            float dist = 0.0f;
            status = euclidean_distance(&model->centers[i * model->input_dim], &model->centers[j * model->input_dim], model->input_dim, &dist);
            if (status != RES_EXIT_SUCCESS) return status;
            if (dist > dmax) dmax = dist;
        }
    }

    float sigma = (dmax == 0.0f) ? 1.0f : (dmax / sqrtf(2.0f * (float)model->num_centers));
    model->gamma = 1.0f / (2.0f * sigma * sigma);

    // b. Transformation de l'espace (Matrice Phi)
    //    On transforme la matrice [dataset_size * input_dim] en [dataset_size * num_centers]
    float* transformed_inputs = (float*) malloc(dataset_size * model->num_centers * sizeof(float));
    if (!transformed_inputs) return ERR_MEMORY_ALLOCATION;

    for (uint32_t i = 0; i < dataset_size; i++) {
        for (uint32_t j = 0; j < model->num_centers; j++) {
            float dist = 0.0f;
            status = euclidean_distance(&dataset_inputs[i * model->input_dim], &model->centers[j * model->input_dim], model->input_dim, &dist);
            if (status != RES_EXIT_SUCCESS) {
                free(transformed_inputs);
                return status;
            }
            transformed_inputs[i * model->num_centers + j] = expf(-model->gamma * dist * dist);
        }
    }

    // ==============================================================================
    // PHASE 3 : Entraînement supervisé (Descente de gradient sur la couche de sortie)
    // ==============================================================================
    status = train_linear_regression(
        model->output_layer,
        transformed_inputs,
        dataset_expected_outputs,
        dataset_size,
        alpha,
        epochs
    );

    free(transformed_inputs);
    return status;
}