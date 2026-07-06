#ifndef __LINEAR_MODEL_H__
#define __LINEAR_MODEL_H__


#include "global.h"
#include "model.h"
#include "matrix.h"
#include "array.h"

typedef struct {
    ModelType model_type; // ModelType_LINEAR
    float* weights;     // weights[0] = poids du bias, weights[1] = w1, weights[2] = w2, ...
    uint32_t length;    // length = input_dim + 1 (nombre de poids + biais)
} LinearModel;

// =============================
// Allocation et libération
// =============================
DLLEXPORT unsigned char create_linear_model(uint32_t input_dim, LinearModel** res_model);
DLLEXPORT unsigned char create_linear_model_randomly(uint32_t input_dim, LinearModel** res_model);
DLLEXPORT unsigned char create_linear_model_from_init_weights(float* weights, uint32_t input_dim, float bias, LinearModel** res_model);
DLLEXPORT unsigned char free_linear_model(LinearModel** model_ptr);

// =============================
// Prédiction
// =============================
DLLEXPORT unsigned char predict_linear_classification(LinearModel* model, float* input, int32_t* results);
DLLEXPORT unsigned char predict_linear_regression(LinearModel* model, float* input, float* results);

// =============================
// Entraînements
// =============================
DLLEXPORT unsigned char train_linear_classification(LinearModel* model, float* dataset_inputs, float* dataset_expected_outputs, uint32_t dataset_size, float alpha, uint32_t epochs);
DLLEXPORT unsigned char train_linear_regression(LinearModel* model, float* dataset_inputs, float* dataset_expected_outputs, uint32_t dataset_size, float alpha, uint32_t epochs);

// =============================
// Calcul des poids via la pseudo-inverse
// =============================
DLLEXPORT unsigned char pseudo_inverse_2d_matrix(Matrix* X, Matrix** res);
DLLEXPORT unsigned char get_linear_regression_weights(Matrix* dataset_inputs, Matrix* dataset_expected_outputs, LinearModel** res_model);
DLLEXPORT unsigned char get_linear_regression_weights_from_list(float* dataset_inputs_without_bias, float* dataset_expected_outputs, uint32_t row, uint32_t col, LinearModel** res_model);


#endif