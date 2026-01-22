#include "../include/global.h"


DLLEXPORT unsigned char sum_float32_array(const float* array, int32_t array_length, float* result) {
    if (!array || !result) return ERR_INVALID_PTR;
    float sum = 0.0;
    for (int32_t i = 0; i < array_length; i++) {
        sum += array[i];
    }
    *result = sum;
    return RES_EXIT_SUCCESS;
}


/// ALLOCATION && FREE PTR ///

DLLEXPORT unsigned char get_float32_array_of_incrementing_numbers(int32_t num_elements, float** res_array) {
    if (!res_array) return ERR_INVALID_PTR;
    float* array = (float*) malloc(num_elements * sizeof(float));
    for (int32_t i = 0; i < num_elements; i++) {
        array[i] = (float) i;
    }
    *res_array = array;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT unsigned char delete_array(void* array) {
    if (!array) return ERR_INVALID_PTR;
    free(array);
    return RES_EXIT_SUCCESS;
}