#include "../include/normalization.h"


const char* get_normalization_method_string(NormalizationMethod normalization_method) {
    switch (normalization_method) {
        case STANDARD:              return "STANDARD";
        case STANDARD_PER_COLUMN:   return "STANDARD_PER_COLUMN";
        default:                    return "UNKNOWN_NORMALIZATION_METHOD";
    }
}

///////////////////////////////////////////////

unsigned char create_StandardNormalizationData(float mean, float std, StandardNormalizationData** data) {
    if (data == NULL) return ERR_INVALID_PTR;
    
    *data = (StandardNormalizationData*) malloc(sizeof(StandardNormalizationData));
    if (*data == NULL) return ERR_MEMORY_ALLOCATION;
    
    (*data)->method = STANDARD;
    (*data)->mean = mean;
    (*data)->std = std;
    
    return RES_EXIT_SUCCESS;
}

unsigned char free_StandardNormalizationData(StandardNormalizationData** data) {
    if (data == NULL || *data == NULL) return RES_EXIT_SUCCESS;
    free(*data);
    *data = NULL;
    return RES_EXIT_SUCCESS;
}

///////////////////////////////////////////////

unsigned char create_StandardPerColumnNormalizationData(float* mean, float* std, uint32_t* length, StandardPerColumnNormalizationData** data) {
    if (data == NULL) return ERR_INVALID_PTR;
    
    *data = (StandardPerColumnNormalizationData*) malloc(sizeof(StandardPerColumnNormalizationData));
    if (*data == NULL) return ERR_MEMORY_ALLOCATION;

    // TODO: demander a claude si mean et std changent quand on change sur python (pcque le tableau est alloue sur python)
     
    (*data)->method = STANDARD_PER_COLUMN;
    (*data)->mean = mean;
    (*data)->std = std;
    (*data)->length = length;
    
    return RES_EXIT_SUCCESS;
}

unsigned char free_StandardPerColumnNormalizationData(StandardPerColumnNormalizationData** data) {
    if (data == NULL || *data == NULL) return RES_EXIT_SUCCESS;
    if ((*data)->mean != NULL) free((*data)->mean);
    if ((*data)->std != NULL) free((*data)->std);
    free(*data);
    *data = NULL;
    return RES_EXIT_SUCCESS;
}