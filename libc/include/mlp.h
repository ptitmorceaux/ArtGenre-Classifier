#ifndef __MLP_H__
#define __MLP_H__


#include "global.h"
#include "random.h"
 
typedef struct {
    uint32_t* dimension;     // Tableau de dimensions (nombre de neuronnes par couche)
    uint32_t L;              // Nombre de "sauts" entre les couches (len(dimension) - 1)

    float** W;              // Poids (W[l] est la matrice de poids vers la couche l+1) --> ne pas oublier le biais 
    float** X;              // Activations (X[l] aura les valeurs des neuronnes de la couche l)
    float** Deltas;              // Deltas (Deltas[l] aura les erreurs de la couche l)
} MLP;



#endif 
