#include <stdint.h>

#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// Error codes

#define EXIT_SUCCESS 0
#define ERR_MATH_INVALID_ARG 1
#define ERR_MATH_DIV_BY_ZERO 2

EXPORT const char *strerror(int32_t err) {
    switch (err) {
        case EXIT_SUCCESS:          return "OK";
        case ERR_MATH_INVALID_ARG:  return "Invalid Argument";
        case ERR_MATH_DIV_BY_ZERO:  return "Division by Zero";
        default:                    return "Unknown Error";
    }
}

// Mathematical operations

EXPORT int32_t addition(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    *result = a + b;
    return EXIT_SUCCESS;
}

EXPORT int32_t soustraction(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    *result = a - b;
    return EXIT_SUCCESS;
}

EXPORT int32_t multiplication(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    *result = a * b;
    return EXIT_SUCCESS;
}

EXPORT int32_t division(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    if (b == 0.0) return ERR_MATH_DIV_BY_ZERO;
    *result = a / b;
    return EXIT_SUCCESS;
}

EXPORT int32_t power(double base, int32_t exponent, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    *result = 1.0;
    for (int32_t i = 0; i < exponent; i++)
        *result *= base;
    return EXIT_SUCCESS;
}