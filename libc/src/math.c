#include "../include/global.h"


DLLEXPORT int32_t add(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a + b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT int32_t sub(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a - b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT int32_t mult(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a * b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT int32_t div(float a, float b, float* result) {
    if (!result) return ERR_INVALID_PTR;
    if (b == 0.0) return ERR_MATH_DIV_BY_ZERO;
    *result = a / b;
    return RES_EXIT_SUCCESS;
}

DLLEXPORT int32_t pow(float base, int32_t exponent, float* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = 1.0;
    for (int32_t i = 0; i < exponent; i++)
        *result *= base;
    return RES_EXIT_SUCCESS;
}