#include "../include/model.h"

const char* get_model_type_string(unsigned char code) {
    switch (code) {
        case ModelType_LINEAR:      return "linearModel";
        case ModelType_MLP:         return "mlp";
        case ModelType_RBF:         return "rbfModel";
        default:                    return "UNKNOWN_MODEL_TYPE";
    }
}