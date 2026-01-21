#include "../include/global.h"

// Struct

typedef struct {
    float a;
    float b;
} LinearModel;

// Linear Model functions

DLLEXPORT unsigned char create_linear_model(float a, float b, LinearModel** res_model) {
    if (!res_model) return ERR_INVALID_PTR;
    LinearModel* model = (LinearModel*) malloc(sizeof(LinearModel));
    model->a = a;
    model->b = b;
    *res_model = model;
    return EXIT_SUCCESS;
}

DLLEXPORT unsigned char predict_linear_model(LinearModel* model, float* result) {
    if (!model || !result) return ERR_INVALID_PTR;
    *result = model->a + model->b;
    return EXIT_SUCCESS;
}

DLLEXPORT unsigned char release_linear_model(LinearModel* model) {
    if (!model) return ERR_INVALID_PTR;
    free(model);
    return EXIT_SUCCESS;
}