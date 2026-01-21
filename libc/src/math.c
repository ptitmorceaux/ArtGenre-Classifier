#include "../include/global.h"


DLLEXPORT unsigned char my_add(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a + b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT unsigned char my_sub(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a - b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT unsigned char my_mult(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a * b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT unsigned char my_div(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    if (b == 0.0) return ERR_MATH_DIV_BY_ZERO;
    *result = a / b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT unsigned char my_pow(float base, int32_t exponent, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = 1.0;
    for (int32_t i = 0; i < exponent; i++)
        *result *= base;
    return RES_EXIT_SUCCESS;
}