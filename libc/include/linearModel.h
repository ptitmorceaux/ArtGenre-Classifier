#ifndef __LINEAR_MODEL_H__
#define __LINEAR_MODEL_H__


#include "global.h"
#include "matrix.h"
#include "array.h"

typedef struct {
    float* weights;
    uint32_t input_dim;
} LinearModel;

// Allocation et libération
DLLEXPORT unsigned char create_linear_model(uint32_t input_dim, LinearModel** res_model);
DLLEXPORT unsigned char free_linear_model(LinearModel** model_ptr);

// Prédiction
DLLEXPORT unsigned char predict_classification(LinearModel* model, double* input, uint32_t input_dim);
DLLEXPORT unsigned char predict_regression(LinearModel* model, double* input, uint32_t input_dim);

// Entraînements
DLLEXPORT unsigned char train_classification(LinearModel* model, double* dataset_inputs, double* dataset_expected_outputs, uint32_t dataset_size, uint32_t alpha, uint32_t epochs);
DLLEXPORT unsigned char train_regression(LinearModel* model, double* dataset_inputs, double* dataset_expected_outputs, uint32_t dataset_size, uint32_t alpha, uint32_t epochs);

#endif
    