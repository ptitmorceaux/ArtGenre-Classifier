#include "../include/model.h"

const char* get_model_type_string(ModelType model_type) {
    switch (model_type) {
        case ModelType_LINEAR:      return "linearModel";
        case ModelType_MLP:         return "mlp";
        default:                    return "UNKNOWN_MODEL_TYPE";
    }
}