
#include "../include/normalization.h"

const char* get_normalization_method_string(NormalizationMethod normalization_method) {
    switch (normalization_method) {
        case STANDARD:              return "STANDARD";
        case STANDARD_PER_COLUMN:   return "STANDARD_PER_COLUMN";
        default:                    return "UNKNOWN_NORMALIZATION_METHOD";
    }
}