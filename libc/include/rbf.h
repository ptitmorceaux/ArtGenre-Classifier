#ifndef __RBF_H__
#define __RBF_H__


#include "global.h"
#include "array.h"
#include "random.h"
#include "linearModel.h"

typedef struct {
    uint32_t input_dim; // dimension de chaque vecteur d'entrée
    uint32_t num_centers; // nombre de centres
    float gamma; // variance de la gaussienne
    float* centers; // tableau des centres [num_centers * input_dim]
} RBF;

#endif 
