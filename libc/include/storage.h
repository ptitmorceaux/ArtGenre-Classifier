#ifndef __STORAGE_H__
#define __STORAGE_H__


#include "global.h"
#include "utils.h"
#include "model.h"
#include "normalization.h"
#include "linearModel.h"
#include "mlp.h"
#include "rbf.h"

/*  Structure du fichier binaire :

    +-----------------------------------------------------------------------+
    | HEADER                                                                |
    | - NormalizationMethod (1 octet)                                       |
    | - ModelType (1 octet)                                                 |
    +-----------------------------------------------------------------------+
    | BLOC NORMALISATION (Taille variable selon la methode)                 |
    | - Si STANDARD : 1 float (Moyenne), 1 float (Écart-type)               |
    | - Si PER_COLUMN : N floats (Moyennes), N floats (Écarts)              |
    +-----------------------------------------------------------------------+
    | BLOC MODÈLE (Taille variable selon le ModelType)                      |
    | - Si ModelType_LINEAR : uint32_t (length) + [length * float32]        |
    | - Si ModelType_MLP    : (Nb layers, architecture, etc.) + [poids...]  |
    | - Si ModelType_RBF    : (Input dimension, number of centers, gamma) + [centers...] + [output_layer...] |
    +-----------------------------------------------------------------------+
*/

// const char* get_current_datetime_string();
unsigned char init_filename(ModelType model_type, NormalizationMethod normalization_method, char** res_filename);
unsigned char get_format_filepath(const char* output_folder_path, const char* _filename, ModelType model_type, NormalizationMethod normalization_method, char** filepath);

unsigned char save_header(FILE* file, ModelType model_type, NormalizationMethod normalization_method);
unsigned char save_standard_normalization(FILE* file, StandardNormalizationData* normalization_data);
unsigned char save_standard_per_column_normalization(FILE* file, StandardPerColumnNormalizationData* normalization_data);
unsigned char save_linear_model(FILE* file, LinearModel* model);
unsigned char save_mlp_model(FILE* file, MLP* model);
unsigned char save_rbf_model(FILE* file, RBF* model);
unsigned char save_normalization_data(FILE* file, NormalizationMethod normalization_method, void* normalization_data);
unsigned char save_model_data(FILE* file, ModelType model_type, void* model);

unsigned char load_header(FILE* file, NormalizationMethod* normalization_method, ModelType* model_type);
unsigned char load_standard_normalization(FILE* file, StandardNormalizationData** normalization_data);
unsigned char load_standard_per_column_normalization(FILE* file, StandardPerColumnNormalizationData** normalization_data);
unsigned char load_linear_model(FILE* file, LinearModel** model);
unsigned char load_mlp_model(FILE* file, MLP** model);
unsigned char load_rbf_model(FILE* file, RBF** model);
unsigned char load_normalization_data(FILE* file, NormalizationMethod normalization_method, void** normalization_data);
unsigned char load_model_data(FILE* file, ModelType model_type, void** model);

DLLEXPORT unsigned char save_binary_file(char* output_folder_path, char* filename, ModelType model_type, void* model, NormalizationMethod normalization_method, void* normalization_data);
DLLEXPORT unsigned char load_binary_file(char* filepath, ModelType* model_type, void** model, NormalizationMethod* normalization_method, void** normalization_data);


#endif