#ifndef __MATH_H__
#define __MATH_H__


#include "global.h"

DLLEXPORT unsigned char my_add(float a, float b, float* result);
DLLEXPORT unsigned char my_sub(float a, float b, float* result);
DLLEXPORT unsigned char my_mult(float a, float b, float* result);
DLLEXPORT unsigned char my_div(float a, float b, float* result);
DLLEXPORT unsigned char my_pow(float base, uint32_t exponent, float* result);


#endif
