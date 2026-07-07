#include "../include/storage.h"

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  UTILS   */

const char* get_current_datetime_string() {
    static char buffer[20]; // "YYYY-MM-DD_HH-MM-SS" (19 + '\0' = 20)
    time_t now = time(NULL);
    struct tm tm;

#if defined(_WIN32)
    localtime_s(&tm, &now);
#else
    localtime_r(&now, &tm);
#endif

    if (strftime(buffer, sizeof(buffer), "%Y-%m-%d_%H-%M-%S", &tm) == 0)
        return NULL;

    return buffer;
}

unsigned char init_filename(ModelType model_type, NormalizationMethod normalization_method, char** res_filename) {
    if (res_filename == NULL || *res_filename != NULL) return ERR_INVALID_PTR;
    
    const char* model_str = get_model_type_string(model_type);
    const char* norm_str = get_normalization_method_string(normalization_method);
    const char* date_str = get_current_datetime_string();

    // + 2 '_' + 4 '.bin' + 1 '\0' = 7
    size_t needed = strlen(model_str) + strlen(norm_str) + strlen(date_str) + 7;
    
    char* filename = (char*) calloc(needed, sizeof(char));
    if (!filename) return ERR_MEMORY_ALLOCATION;

    snprintf(filename, needed, "%s_%s.%s.bin", model_str, norm_str, date_str);

    *res_filename = filename;
    return RES_EXIT_SUCCESS;
}

// Si _filename est NULL, la fonction va générer un nom de fichier basé sur le model_type et normalization_method
unsigned char get_format_filepath(const char* output_folder_path, const char* _filename, ModelType model_type, NormalizationMethod normalization_method, char** filepath) {
    if (!output_folder_path || !filepath || *filepath != NULL) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;
    char* filename = NULL;

    if (_filename != NULL) {
        filename = (char*) _filename;
    } else {
        status = init_filename(model_type, normalization_method, &filename);
        if (status != RES_EXIT_SUCCESS) return status;
    }

    // + 1 '/' + 1 '\0' = 2
    size_t needed = strlen(output_folder_path) + strlen(filename) + 2;
    
    *filepath = (char*) calloc(needed, sizeof(char));
    if (!(*filepath)) {
        if (_filename == NULL) free(filename);
        return ERR_MEMORY_ALLOCATION;
    }

    // Construction sécurisée du chemin
    snprintf(*filepath, needed, "%s/%s", output_folder_path, filename);
    
    if (_filename == NULL) free(filename);
    return status;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  SAVE - HEADER  */

unsigned char save_header(FILE* file, ModelType model_type, NormalizationMethod normalization_method) {
    if (!file) return ERR_INVALID_PTR;

    // NormalizationMethod (1 octet)
    fwrite(&normalization_method, sizeof(unsigned char), 1, file);

    // ModelType (1 octet)
    fwrite(&model_type, sizeof(unsigned char), 1, file);

    return RES_EXIT_SUCCESS;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  SAVE - NORMALIZATION  */

/*
typedef struct {
    NormalizationMethod method;
    float mean; // moyenne globale
    float std;  // ecart-type global
} StandardNormalizationData;
*/
unsigned char save_standard_normalization(FILE* file, StandardNormalizationData* normalization_data) {
    if (!file || !normalization_data) return ERR_INVALID_PTR;

    // method (1 octet)
    fwrite(&(normalization_data->method), sizeof(unsigned char), 1, file);

    // mean (float32)
    fwrite(&(normalization_data->mean), sizeof(float), 1, file);

    // std (float32)
    fwrite(&(normalization_data->std), sizeof(float), 1, file);

    return RES_EXIT_SUCCESS;
}

/*
typedef struct {
    NormalizationMethod method;
    float* mean; // tableau de moyennes pour chaque colonne
    float* std;  // tableau d'ecart-types pour chaque colonne
    uint32_t length; // nombre de colonnes
} StandardPerColumnNormalizationData;
*/
unsigned char save_standard_per_column_normalization(FILE* file, StandardPerColumnNormalizationData* normalization_data) {
    if (!file || !normalization_data || !normalization_data->mean || !normalization_data->std) return ERR_INVALID_PTR;

    // method (1 octet)
    fwrite(&(normalization_data->method), sizeof(unsigned char), 1, file);

    // length (uint32_t)
    fwrite(&(normalization_data->length), sizeof(uint32_t), 1, file);

    // mean (float32 array)
    for (uint32_t i = 0; i < normalization_data->length; i++) {
        fwrite(&(normalization_data->mean[i]), sizeof(float), 1, file);
    }

    // std (float32 array)
    for (uint32_t i = 0; i < normalization_data->length; i++) {
        fwrite(&(normalization_data->std[i]), sizeof(float), 1, file);
    }

    return RES_EXIT_SUCCESS;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  SAVE - MODEL  */

/*
typedef struct {
    float* weights;     // weights[0] = poids du bias, weights[1] = w1, weights[2] = w2, ...
    uint32_t length;    // length = input_dim + 1 (nombre de poids + biais)
} LinearModel;
 */
unsigned char save_linear_model(FILE* file, LinearModel* model) {
    if (!file || !model || !model->weights) return ERR_INVALID_PTR;

    // length (uint32_t)
    fwrite(&(model->length), sizeof(uint32_t), 1, file);

    // weights (float32 array)
    fwrite(model->weights, sizeof(float), model->length, file);

    return RES_EXIT_SUCCESS;
}

/*
NOTE: Pas besoin de save/load X et deltas

typedef struct {
    uint32_t* d;            // Tableau de dimensions (nombre de neuronnes par couche)
    uint32_t L;             // Nombre de "sauts" entre les couches (len(dimension) - 1)

    float*** W;             // Poids (W[l] est la matrice de poids vers la couche l+1) --> ne pas oublier le biais 
    float** X;              // Activations (X[l] aura les valeurs des neuronnes de la couche l)
    float** deltas;         // Deltas (Deltas[l] aura les erreurs de la couche l)
} MLP;
*/
unsigned char save_mlp_model(FILE* file, MLP* model) {
    if (!file || !model || !model->d || !model->W) return ERR_INVALID_PTR;
    
    // L (uint32_t)
    fwrite(&(model->L), sizeof(uint32_t), 1, file);

    // d (uint32_t array)
    fwrite(model->d, sizeof(uint32_t), model->L + 1, file);

    // W (float32 array)
    // len(model->W) = model->L
    for (uint32_t l = 0; l < model->L; l++) {
        
        uint32_t rows = model->d[l] + 1; // +1 car la couche de départ DE CHAQUE TRANSITION a un biais
        uint32_t cols = model->d[l + 1]; // Pas de +1, la couche d'arrivée n'a pas de biais

        for (uint32_t i = 0; i < rows; i++) {
            for (uint32_t j = 0; j < cols; j++) {
                fwrite(&(model->W[l][i][j]), sizeof(float), 1, file);
            }
        }
    }

    return RES_EXIT_SUCCESS;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  SAVE - GLOBAL  */

unsigned char save_normalization_data(FILE* file, NormalizationMethod normalization_method, void* normalization_data) {
    if (!file || !normalization_data) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;

    switch (normalization_method) {
        
        case STANDARD:
            status = save_standard_normalization(file, (StandardNormalizationData*) normalization_data);
            break;

        case STANDARD_PER_COLUMN:
            status = save_standard_per_column_normalization(file, (StandardPerColumnNormalizationData*) normalization_data);
            break;
        
        default:
            return ERROR_SAVE_INVALID_NORMALIZATION_METHOD;
    }

    return status;
}

unsigned char save_model_data(FILE* file, ModelType model_type, void* model) {
    if (!file || !model) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;

    switch (model_type) {
        
        case ModelType_LINEAR:
            status = save_linear_model(file, (LinearModel*) model);
            break;

        case ModelType_MLP:
            status = save_mlp_model(file, (MLP*) model);
            break;
        
        default:
            return ERROR_INVALID_MODEL_TYPE;
    }

    return status;
}

unsigned char save_binary_file(char* output_folder_path, char* filename, ModelType model_type, void* model, NormalizationMethod normalization_method, void* normalization_data) {
    if (!output_folder_path || !model || !normalization_data) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;
    
    char* filepath = NULL;
    status = get_format_filepath(output_folder_path, filename, model_type, normalization_method, &filepath);
    if (status != RES_EXIT_SUCCESS) return status;

    // +5 => 4 '.tmp' + 1 '\0'
    char* tmp_filepath = (char*) calloc(strlen(filepath) + 5, sizeof(char));
    if (!tmp_filepath) {
        free(filepath);
        return ERR_MEMORY_ALLOCATION;
    }

    // on ajoute l'extension .tmp pour le fichier temporaire
    snprintf(tmp_filepath, strlen(filepath) + 5, "%s.tmp", filepath);

    FILE* file = fopen(tmp_filepath, "wb");
    if (!file) {
        remove(tmp_filepath);
        free(tmp_filepath);
        free(filepath);
        return ERR_FILE_OPEN_TMP;
    }
    
    status = save_header(file, model_type, normalization_method);
    if (status != RES_EXIT_SUCCESS) {
        fclose(file);
        remove(tmp_filepath);
        free(tmp_filepath);
        free(filepath);
        return status;
    }
    
    status = save_normalization_data(file, normalization_method, normalization_data);
    if (status != RES_EXIT_SUCCESS) {
        fclose(file);
        remove(tmp_filepath);
        free(tmp_filepath);
        free(filepath);
        return status;
    }

    status = save_model_data(file, model_type, model);
    if (status != RES_EXIT_SUCCESS) {
        fclose(file);
        remove(tmp_filepath);
        free(tmp_filepath);
        free(filepath);
        return status;
    }

    fclose(file);

    // Renommer le fichier temporaire en fichier final
    if (rename(tmp_filepath, filepath) != 0) {
        free(tmp_filepath);
        free(filepath);
        return ERR_FILE_RENAME_TMP;
    }

    free(tmp_filepath);
    free(filepath);
    return RES_EXIT_SUCCESS;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  LOAD - HEADER   */

unsigned char load_header(FILE* file, NormalizationMethod* normalization_method, ModelType* model_type) {
    if (!file || !normalization_method || !model_type) return ERR_INVALID_PTR;

    // NormalizationMethod (1 octet)
    if (fread(normalization_method, sizeof(unsigned char), 1, file) != 1) 
        return ERR_FILE_READ;

    // ModelType (1 octet)
    if (fread(model_type, sizeof(unsigned char), 1, file) != 1) 
        return ERR_FILE_READ;

    return RES_EXIT_SUCCESS;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  LOAD - NORMALIZATION   */

/*
typedef struct {
    NormalizationMethod method;
    float mean; // moyenne globale
    float std;  // ecart-type global
} StandardNormalizationData;
*/
unsigned char load_standard_normalization(FILE* file, StandardNormalizationData** normalization_data) {
    if (!file || !normalization_data || *normalization_data != NULL) return ERR_INVALID_PTR;

    StandardNormalizationData* data = (StandardNormalizationData*) malloc(sizeof(StandardNormalizationData));
    if (!data) return ERR_MEMORY_ALLOCATION;

    // method (1 octet)
    if (fread(&(data->method), sizeof(unsigned char), 1, file) != 1) 
        return ERR_FILE_READ;

    // mean (float32)
    if (fread(&(data->mean), sizeof(float), 1, file) != 1) 
        return ERR_FILE_READ;

    // std (float32)
    if (fread(&(data->std), sizeof(float), 1, file) != 1) 
        return ERR_FILE_READ;

    *normalization_data = data;
    return RES_EXIT_SUCCESS;
}

/*
typedef struct {
    NormalizationMethod method;
    float* mean; // tableau de moyennes pour chaque colonne
    float* std;  // tableau d'ecart-types pour chaque colonne
    uint32_t length; // nombre de colonnes
} StandardPerColumnNormalizationData;
*/
unsigned char load_standard_per_column_normalization(FILE* file, StandardPerColumnNormalizationData** normalization_data) {
    if (!file || !normalization_data || *normalization_data != NULL) return ERR_INVALID_PTR;

    StandardPerColumnNormalizationData* data = (StandardPerColumnNormalizationData*) malloc(sizeof(StandardPerColumnNormalizationData));
    if (!data) return ERR_MEMORY_ALLOCATION;

    // method (1 octet)
    if (fread(&(data->method), sizeof(unsigned char), 1, file) != 1) 
        return ERR_FILE_READ;

    // length (uint32_t)
    if (fread(&(data->length), sizeof(uint32_t), 1, file) != 1) 
        return ERR_FILE_READ;

    // mean (float32 array)
    data->mean = (float*) malloc(data->length * sizeof(float));
    if (!data->mean) {
        free(data);
        return ERR_MEMORY_ALLOCATION;
    }
    if (fread(data->mean, sizeof(float), data->length, file) != data->length) {
        free(data->mean);
        free(data);
        return ERR_FILE_READ;
    }

    // std (float32 array)
    data->std = (float*) malloc(data->length * sizeof(float));
    if (!data->std) {
        free(data->mean);
        free(data);
        return ERR_MEMORY_ALLOCATION;
    }
    if (fread(data->std, sizeof(float), data->length, file) != data->length) {
        free(data->std);
        free(data->mean);
        free(data);
        return ERR_FILE_READ;
    }

    *normalization_data = data;
    return RES_EXIT_SUCCESS;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  LOAD - MODEL  */

/*
typedef struct {
    float* weights;     // weights[0] = poids du bias, weights[1] = w1, weights[2] = w2, ...
    uint32_t length;    // length = input_dim + 1 (nombre de poids + biais)
} LinearModel;
 */
unsigned char load_linear_model(FILE* file, LinearModel** model) {
    if (!file || !model || *model != NULL) return ERR_INVALID_PTR;

    LinearModel* data = (LinearModel*) malloc(sizeof(LinearModel));
    if (!data) return ERR_MEMORY_ALLOCATION;

    // length (uint32_t)
    if (fread(&(data->length), sizeof(uint32_t), 1, file) != 1) {
        free(data);
        return ERR_FILE_READ;
    }

    // weights (float32 array)
    data->weights = (float*) malloc(data->length * sizeof(float));
    if (!data->weights) {
        free(data);
        return ERR_MEMORY_ALLOCATION;
    }
    if (fread(data->weights, sizeof(float), data->length, file) != data->length) {
        free(data->weights);
        free(data);
        return ERR_FILE_READ;
    }

    *model = data;
    return RES_EXIT_SUCCESS;
}

/*
NOTE: Pas besoin de save/load X et deltas

typedef struct {
    uint32_t* d;            // Tableau de dimensions (nombre de neuronnes par couche)
    uint32_t L;             // Nombre de "sauts" entre les couches (len(dimension) - 1)

    float*** W;             // Poids (W[l] est la matrice de poids vers la couche l+1) --> ne pas oublier le biais 
    float** X;              // Activations (X[l] aura les valeurs des neuronnes de la couche l)
    float** deltas;         // Deltas (Deltas[l] aura les erreurs de la couche l)
} MLP;
*/
unsigned char load_mlp_model(FILE* file, MLP** res_model) {
    if (!file || !res_model) return ERR_INVALID_PTR;

    uint32_t L;
    // L (uint32_t) -> len(W)
    if (fread(&L, sizeof(uint32_t), 1, file) != 1) return ERR_FILE_READ;

    // d (uint32_t array) -> len(d) = L + 1
    uint32_t* d = (uint32_t*) malloc((L + 1) * sizeof(uint32_t));
    if (!d) return ERR_MEMORY_ALLOCATION;
    
    if (fread(d, sizeof(uint32_t), L + 1, file) != L + 1) {
        free(d);
        return ERR_FILE_READ;
    }

    // Allocation mlp model
    MLP* model = NULL;
    unsigned char status = create_mlp(d, L + 1, &model);
    free(d); // On peut libérer d car create_mlp en fait une copie profonde
    if (status != RES_EXIT_SUCCESS) return status;

    // W (float32 array)
    for (uint32_t l = 0; l < model->L; l++) {
        uint32_t rows = model->d[l] + 1;
        uint32_t cols = model->d[l + 1];

        for (uint32_t i = 0; i < rows; i++) {
            for (uint32_t j = 0; j < cols; j++) {
                if (fread(&(model->W[l][i][j]), sizeof(float), 1, file) != 1) {
                    free_mlp(&model);
                    return ERR_FILE_READ;
                }
            }
        }
    }

    *res_model = model;
    return RES_EXIT_SUCCESS;
}
    

//////////////////////////////////////////////////////////////////////////////////////////////////////
/*  LOAD - GLOBAL   */

unsigned char load_normalization_data(FILE* file, NormalizationMethod normalization_method, void** normalization_data) {
    if (!file || !normalization_data || *normalization_data != NULL) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;

    switch (normalization_method) {
        
        case STANDARD:
            status = load_standard_normalization(file, (StandardNormalizationData**) normalization_data);
            break;

        case STANDARD_PER_COLUMN:
            status = load_standard_per_column_normalization(file, (StandardPerColumnNormalizationData**) normalization_data);
            break;
        
        default:
            return ERROR_LOAD_INVALID_NORMALIZATION_METHOD;
    }

    return status;
}

unsigned char load_model_data(FILE* file, ModelType model_type, void** model) {
    if (!file || !model || *model != NULL) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;

    switch (model_type) {
        
        case ModelType_LINEAR:
            status = load_linear_model(file, (LinearModel**) model);
            break;

        case ModelType_MLP:
            status = load_mlp_model(file, (MLP**) model);
            break;
        
        default:
            return ERROR_INVALID_MODEL_TYPE;
    }

    return status;
}

/*
    RETURN:
    - NormalizationMethod
    - ModelType
    - void* model
    - void* normalization_data
*/
unsigned char load_binary_file(char* filepath, ModelType* model_type, void** model, NormalizationMethod* normalization_method, void** normalization_data) {
    if (!filepath || !model_type || !model || !normalization_method || !normalization_data) return ERR_INVALID_PTR;
    if (*model != NULL || *normalization_data != NULL) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;

    FILE* file = fopen(filepath, "rb");
    if (!file) return ERR_FILE_OPEN_RB;

    status = load_header(file, normalization_method, model_type);
    if (status != RES_EXIT_SUCCESS) {
        fclose(file);
        return status;
    }

    status = load_normalization_data(file, *normalization_method, normalization_data);
    if (status != RES_EXIT_SUCCESS) {
        fclose(file);
        return status;
    }

    status = load_model_data(file, *model_type, model);
    if (status != RES_EXIT_SUCCESS) {
        fclose(file);
        return status;
    }

    fclose(file);
    return RES_EXIT_SUCCESS;
}