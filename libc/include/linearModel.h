#ifndef __LINEAR_MODEL_H__
#define __LINEAR_MODEL_H__


#include "global.h"
#include "matrix.h"
#include "array.h"

typedef struct {
    float* weights;
    uint32_t input_dim;
} LinearModel;

// =============================
// Allocation et libération
// =============================
DLLEXPORT unsigned char create_linear_model(uint32_t input_dim, LinearModel** res_model);
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

#endif
    
