#include "../include/array.h"

unsigned char fill_randomly_float_array(float min, float max, float** array, uint32_t size_array) {
    if (!array || !(*array)) return ERR_INVALID_PTR;
    float* data = *array;

    for (uint32_t i = 0; i < size_array; i++) {
        
        unsigned char status = random_float(min, max, &(data[i]));
        if (status != RES_EXIT_SUCCESS) {
            free(data);
            return status;
        }
    }
    return RES_EXIT_SUCCESS;
}