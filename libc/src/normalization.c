#include "../include/normalization.h"

const char* get_normalization_method_string(NormalizationMethod normalization_method) {
    switch (normalization_method) {
        case STANDARD:              return "STANDARD";
        case STANDARD_PER_COLUMN:   return "STANDARD_PER_COLUMN";
        default:                    return "UNKNOWN_NORMALIZATION_METHOD";
    }
}

unsigned char free_StandardNormalizationData(StandardNormalizationData** data) {
    if (data == NULL || *data == NULL) return RES_EXIT_SUCCESS;
    free(*data);
    *data = NULL;
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