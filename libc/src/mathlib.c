#include "../include/global.h"

// Error codes

#define EXIT_SUCCESS 0
#define ERR_INVALID_PTR 1
#define ERR_MATH_DIV_BY_ZERO 2

// Error string function

EXPORT char* strerror(int32_t err) {
    switch (err) {
        case EXIT_SUCCESS:          return "OK";
        case ERR_INVALID_PTR:       return "Invalid Pointer";
        case ERR_MATH_DIV_BY_ZERO:  return "Division by Zero";
        default:                    return "Unknown Error";
    }
}

// Mathematical operations

EXPORT int32_t add(double a, double b, double* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a + b;
    return EXIT_SUCCESS;
}

EXPORT int32_t sub(double a, double b, double* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a - b;
    return EXIT_SUCCESS;
}

EXPORT int32_t mult(double a, double b, double* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = a * b;
    return EXIT_SUCCESS;
}

EXPORT int32_t div(double a, double b, double* result) {
    if (!result) return ERR_INVALID_PTR;
    if (b == 0.0) return ERR_MATH_DIV_BY_ZERO;
    *result = a / b;
    return EXIT_SUCCESS;
}

EXPORT int32_t power(double base, int32_t exponent, double* result) {
    if (!result) return ERR_INVALID_PTR;
    *result = 1.0;
    for (int32_t i = 0; i < exponent; i++)
        *result *= base;
    return EXIT_SUCCESS;
}