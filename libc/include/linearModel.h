#ifndef __LINEAR_MODEL_H__
#define __LINEAR_MODEL_H__


#include "global.h"

// Allocation et libération
EXPORT double* create_linear_model(int input_dim);
EXPORT void free_linear_model(double* model);

// Prédiction
EXPORT double predict_classification(double* model, double* input, int input_dim);
EXPORT double predict_regression(double* model, double* input, int input_dim);

// Entraînements
EXPORT void train_classification();
EXPORT void train_regression();

#endif
