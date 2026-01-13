#include "../include/global.h"

// Error codes

#define EXIT_SUCCESS 0
#define ERR_INVALID_PTR 1
#define ERR_INVALID_NUMBER 2

// Error string function

EXPORT char* strerror(int32_t err) {
    switch (err) {
        case EXIT_SUCCESS:  return "OK";
        case ERR_INVALID_PTR:  return "Invalid Pointer";
        case ERR_INVALID_NUMBER:  return "Invalid Number";
        default:            return "Unknown Error";
    }
}

// functions

EXPORT int32_t factorial(uint32_t nb, uint32_t* result) {
    if (!result) return ERR_INVALID_PTR;
    if (nb == 0) *result = 0;
    for (uint32_t i = 1; i <= nb; i++)
        *result *= i;
    return EXIT_SUCCESS;
}