#include "../include/rbf.h"

/** ==========================================
 * Structure for a Radial Basis Function (RBF) Network
 * ========================================== **/
/*
    # Architecture d'un réseau de neurones à fonctions de base radiale (RBF) : 
        - input_dim : Dimension de chaque vecteur d'entrée.
        - num_centers : Nombre de centres.
        - gamma : Variance de la fonction gaussienne.
        - centers : Tableau des centres [num_centers * input_dim].

    # Implémentation en C :
        
*/

unsigned char euclidean_distance(float* a, float* b, uint32_t dim, float* result) {
    float sum = 0.0f;
    for (uint32_t i = 0; i < dim; i++) {
        float diff = a[i] - b[i];
        sum += diff * diff;
    }

    *result = sqrtf(sum);
    return RES_EXIT_SUCCESS;
}

// Alogorithme de K-Means
unsigned char rbf_kmeans(float* points, uint32_t num_points, uint32_t input_dim, uint32_t k, float* out_centers, uint32_t max_iters) {
    uint32_t* assignments = (uint32_t*)malloc(num_points * sizeof(uint32_t));
    uint32_t* cluster_sizes = (uint32_t*)malloc(k * sizeof(uint32_t));

    if (!assignments || !cluster_sizes) {
        free(assignments);
        free(cluster_sizes);
        return ERR_ALLOCATION_FAILED;
    }

    for (uint32_t i = 0; i < k; i++) {
        for (uint32_t d = 0; d < input_dim; d++) {
            out_centers[i * input_dim + d] = points[i * input_dim + d];
        }
    }

    unsigned char converged = 0;
    uint32_t iter = 0;

    while (!converged && iter < max_iters) {
        converged = 1;
        for (uint32_t i = 0; i < num_points; i++) {
            float min_dist = MAX_FLOAT;
            uint32_t closest_center = 0;

            /** ==========================================================
             * Etape 1 : Assigner chaque point à son centre le plus proche
             * =========================================================== 
            **/

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

            if (assignments[i] != closest_center) {
                converged = 0;
                assignments[i] = closest_center;
            }
        }

        if (converged) break;

            /** ==============================================
             *  Etape 2 : Recalculer les centres des clusters
             * ===============================================
            **/
        for (uint32_t i = 0; i < k * input_dim; i++) {
            out_centers[i] = 0.0f;
        }

        for (uint32_t i = 0; i < k; i++) {
            cluster_sizes[i] = 0;
        }

        // Somme des points
        for (uint32_t i = 0; i < num_points; i++) {
            uint32_t cluster_id = assignments[i];
            cluster_sizes[cluster_id]++;
            for (uint32_t d = 0; d < input_dim; d++) {
                out_centers[cluster_id * input_dim + d] += points[i * input_dim + d];
            }
        }

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
 *  Creation d'un réseau RBF
 *  ===============================================
**/

unsigned char create_rbf(uint32_t input_dim, uint32_t num_centers, float gamma, RBF** res_model) {
    if (!res_model) return ERR_INVALID_PTR;

    RBF* model = (RBF*) malloc(sizeof(RBF));
    if (!model) return ERR_ALLOCATION_FAILED;

    model->input_dim = input_dim;
    model->num_centers = num_centers;
    model->gamma = gamma;

    // Allocation des centres
    model->centers = (float*) calloc(num_centers * input_dim, sizeof(float));
    if (!model->centers) {
        free(model);
        return ERR_ALLOCATION_FAILED;
    }

    // Création de la couche de sortie (modèle linéaire)
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
 *  Libération de la mémoire d'un réseau RBF
 *  ===============================================
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
 *  Prédiction avec un réseau RBF et entrainement
 *  ===============================================
*/

unsigned char predict_rbf(RBF* model, float* input, int32_t* outputs) {
    if (!model || !outputs) return ERR_INVALID_PTR;

    float* hidden_activations = (float*) malloc(model->num_centers * sizeof(float));
    if (!hidden_activations) return ERR_ALLOCATION_FAILED;

    for (uint32_t i = 0; i < model->num_centers; i++) {
        float dist = 0.0f;
        unsigned char status = euclidean_distance(&input[0], &model->centers[i * model->input_dim], model->input_dim, &dist);
        if (status != RES_EXIT_SUCCESS) {
            free(hidden_activations);
            return status;
        }
        hidden_activations[i] = expf(-model->gamma * dist * dist);
    }

    unsigned char status = predict_linear_classification(model->output_layer, hidden_activations, outputs);
    
    free(hidden_activations);
    return status;
}

unsigned char train_rbf(RBF* model, float* dataset_inputs, float* dataset_expected_outputs,
        uint32_t dataset_size, float alpha, uint32_t epochs) {
    if (!model || !dataset_inputs || !dataset_expected_outputs) return ERR_INVALID_PTR;

    // PHASE 1 : Entraînement non supervisé (Placer les centres avec K-means)
    rbf_kmeans(dataset_inputs, dataset_size, model->input_dim, model->num_centers, model->centers, 100);

    // Calcul automatique du gamma : on utilise l'heuristique classique 
    // gamma = 1 / (2 * sigma^2) où sigma est basée sur la distance max entre 2 centres
    float dmax = 0.0f;
    for (uint32_t i = 0; i < model->num_centers; i++) {
        for (uint32_t j = i + 1 ; j < model->num_centers; j++) {
            float dist = 0.0f;
            unsigned char status = euclidean_distance(&model->centers[i * model->input_dim], &model->centers[j * model->input_dim], model->input_dim, &dist);
            if (status != RES_EXIT_SUCCESS) return status;
            if (dist > dmax) dmax = dist;
        }
    }

    float sigma = (dmax == 0.0f) ? 1.0f : (dmax / sqrtf(2.0f * (float)model->num_centers));
    model->gamma = 1.0f / (2.0f * sigma * sigma);

    // PHASE 2: Entrainement supervisé
    float* transformed_inputs = (float*) malloc(dataset_size * model->num_centers * sizeof(float));
    if (!transformed_inputs) return ERR_ALLOCATION_FAILED;

    for (uint32_t i = 0; i < dataset_size; i++) {
        for (uint32_t j = 0; j < model->num_centers; j++) {
            float dist = 0.0f;
            unsigned char status = euclidean_distance(&dataset_inputs[i * model->input_dim], &model->centers[j * model->input_dim], model->input_dim, &dist);
            if (status != RES_EXIT_SUCCESS) {
                free(transformed_inputs);
                return status;
            }
            transformed_inputs[i * model->num_centers + j] = expf(-model->gamma * dist * dist);
        }
    }

    // PHASE 3: Entraintement supervisé
    unsigned char status = train_linear_classification(
        model->output_layer,
        transformed_inputs,
        dataset_expected_outputs,
        dataset_size,
        alpha,
        epochs
    );

    free(transformed_inputs);
    return RES_EXIT_SUCCESS;
}