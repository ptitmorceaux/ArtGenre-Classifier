#ifndef __MODEL_H__
#define __MODEL_H__

#include "global.h"

// Les enum ne doivent pas dépasser 255, sinon il faudra changer le type de retour des fonctions save/load_binary_file
typedef enum {
    ModelType_LINEAR,
    ModelType_MLP,
} ModelType;

DLLEXPORT const char* get_model_type_string(ModelType model_type);

#endif