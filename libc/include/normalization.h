#ifndef __NORMALIZATION_H__
#define __NORMALIZATION_H__

#include "global.h"
 
// Les enum ne doivent pas dépasser 255, sinon il faudra changer le type de retour des fonctions save/load_binary_file
typedef enum {
    STANDARD,
    STANDARD_PER_COLUMN,
} NormalizationMethod;


typedef struct {
    NormalizationMethod method;
    float mean; // moyenne globale
    float std;  // ecart-type global
} StandardNormalizationData;


typedef struct {
    NormalizationMethod method;
    float* mean; // tableau de moyennes pour chaque colonne
    float* std;  // tableau d'ecart-types pour chaque colonne
    uint32_t length; // nombre de colonnes
} StandardPerColumnNormalizationData;


DLLEXPORT const char* get_normalization_method_string(NormalizationMethod normalization_method);
DLLEXPORT unsigned char free_StandardNormalizationData(StandardNormalizationData** data);
DLLEXPORT unsigned char free_StandardPerColumnNormalizationData(StandardPerColumnNormalizationData** data);


#endif