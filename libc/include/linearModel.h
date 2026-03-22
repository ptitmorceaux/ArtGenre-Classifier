#ifndef __LINEAR_MODEL_H__
#define __LINEAR_MODEL_H__


#include "global.h"

// Allocation et libération
EXPORT double* create_linear_model(int input_dim);
EXPORT void free_linear_model(double* model);



#endif
