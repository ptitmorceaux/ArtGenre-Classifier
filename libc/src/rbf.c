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
unsigned char rbf_kmeans() {
    return RES_EXIT_SUCCESS;
}