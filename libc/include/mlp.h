#ifndef __MLP_H__
#define __MLP_H__


#include "global.h"
#include "model.h"
#include "array.h"
#include "random.h"

typedef struct {
    ModelType model_type;   // ModelType_MLP

    uint32_t* d;            // Tableau de dimensions (nombre de neuronnes par couche) + 1 pour le biais
    uint32_t L;             // Nombre de "sauts" entre les couches (len(dimension) - 1)

    float*** W;             // Poids (W[l] est la matrice de poids vers la couche l+1) --> ne pas oublier le biais 
    float** X;              // Activations (X[l] aura les valeurs des neuronnes de la couche l)
    float** deltas;         // Deltas (Deltas[l] aura les erreurs de la couche l)
} MLP;


DLLEXPORT unsigned char create_mlp(uint32_t* npl, uint32_t npl_size, MLP** res_model);
DLLEXPORT unsigned char free_mlp(MLP** model_ptr);
DLLEXPORT unsigned char propagate_forward_mlp(MLP* model, float* input, char is_classification);
DLLEXPORT unsigned char predict_mlp(MLP* model, float* input, char is_classification, float* outputs);
DLLEXPORT unsigned char train_mlp(MLP* model, float* dataset_inputs, float* dataset_expected_outputs, uint32_t dataset_size, float alpha, uint32_t epochs, char is_classification);

#endif 
