#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// Error codes
#define EXIT_SUCCESS 0
#define ERR_MATH_INVALID_ARG 1
#define ERR_MATH_DIV_BY_ZERO 2

EXPORT const char* strerror(__INT32_TYPE__ err) {
    switch (err) {
        case ERR_MATH_INVALID_ARG:
            return "Invalid Argument";
        case ERR_MATH_DIV_BY_ZERO:
            return "Division by Zero";
        case EXIT_SUCCESS:
            return "OK";
        default:
            return "Unknown Error";
    }
}

// Mathematical operations

EXPORT __INT32_TYPE__ addition(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    *result = a + b;
    return EXIT_SUCCESS;
}

EXPORT __INT32_TYPE__ soustraction(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    *result = a - b;
    return EXIT_SUCCESS;
}

EXPORT __INT32_TYPE__ multiplication(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    *result = a * b;
    return EXIT_SUCCESS;
}

EXPORT __INT32_TYPE__ division(double a, double b, double *result) {
    if (!result) return ERR_MATH_INVALID_ARG;
    if (b == 0.0) return ERR_MATH_DIV_BY_ZERO;
    *result = a / b;
    return EXIT_SUCCESS;
}
