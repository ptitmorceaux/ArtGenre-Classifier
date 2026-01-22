#include "../include/global.h"


/// ALLOCATION ///

DLLEXPORT unsigned char ALLOCATE_float32_array_of_incrementing_numbers(uint32_t array_length, float** res_array) {
    if (!res_array) return ERR_INVALID_PTR;
    *res_array = NULL; // init
    if (array_length == 0) return ERR_LENGTH_ZERO;

    float* array = (float*) malloc(array_length * sizeof(float));
    for (uint32_t i = 0; i < array_length; i++) {
        array[i] = (float) i;
    }
    *res_array = array;
    return RES_EXIT_SUCCESS;
}


// ARRAY OPERATIONS ///

DLLEXPORT unsigned char sum_float32_array(const float* array, uint32_t array_length, float* result) {
    if (!array || !result) return ERR_INVALID_PTR;
    float sum = 0.0;
    for (uint32_t i = 0; i < array_length; i++) {
        sum += array[i];
    }
    *result = sum;
    return RES_EXIT_SUCCESS;
}