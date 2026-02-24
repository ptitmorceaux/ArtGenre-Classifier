#ifndef __ARRAY_H__
#define __ARRAY_H__


#include "global.h"

DLLEXPORT unsigned char ALLOCATE_float32_array_of_incrementing_numbers(uint32_t array_length, float** res_array);
DLLEXPORT unsigned char sum_float32_array(const float* array, uint32_t array_length, float* result);


#endif
