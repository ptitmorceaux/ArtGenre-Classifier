#ifndef __RBF_H__
#define __RBF_H__


#include "global.h"
#include "array.h"
#include "random.h"
#include "linearModel.h"

/* Maximum float value */
#define MAX_FLOAT 3.402823466e+38F

typedef struct {
    uint32_t input_dim;         // dimension de chaque vecteur d'entrée
    uint32_t num_centers;       // nombre de centres
    float gamma;                // variance de la gaussienne
    float* centers;             // tableau des centres [num_centers * input_dim]
    LinearModel* output_layer;  // modèle linéaire pour la sortie
} RBF;


DLLEXPORT unsigned char euclidean_distance(float* a, float* b, uint32_t dim, float* result);
DLLEXPORT unsigned char rbf_kmeans(float* points, uint32_t num_points, uint32_t input_dim, uint32_t k, float* out_centers, uint32_t max_iters);
DLLEXPORT unsigned char create_rbf(uint32_t input_dim, uint32_t num_centers, float gamma, RBF** res_model);
DLLEXPORT unsigned char free_rbf(RBF** model_ptr);
DLLEXPORT unsigned char predict_rbf(RBF* model, float* input, int32_t* outputs);
DLLEXPORT unsigned char train_rbf(RBF* model, float* dataset_inputs, float* dataset_expected_outputs, uint32_t dataset_size, float alpha, uint32_t epochs, float* loss_history, float* accuracy_history);
DLLEXPORT unsigned char predict_rbf_regression(RBF* model, float* input, float* output);
DLLEXPORT unsigned char train_rbf_regression(RBF* model, float* dataset_inputs, float* dataset_expected_outputs, uint32_t dataset_size, float alpha, uint32_t epochs);

#endif 
