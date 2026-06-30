#include "../include/utils.h"


// status code to string
const char* get_status_message(unsigned char code) {
    switch (code) {
        case RES_EXIT_SUCCESS:              return "OK";
        case ERR_INVALID_PTR:               return "Invalid Pointer";
        case ERR_MATH_DIV_BY_ZERO:          return "Division by Zero";
        case ERR_LENGTH_ZERO:               return "Length is Zero";
        case ERR_MEMORY_ALLOCATION:         return "Memory Allocation Failed";
        case ERR_OUT_OF_BOUNDS:             return "Index Out of Bounds";
        case ERR_INVALID_MATRIX_DIMENSIONS: return "Invalid Matrix Dimensions";
        case ERR_INVALID_MATRIX_SQUARE:     return "Matrices must be square and have the same dimensions";
        case ERR_INVALID_MATRIX_INVERSION_SINGULAR: return "Matrix is singular and cannot be inverted";
        case ERR_INVALID_MATRIX_INVERSION:          return "Matrix inversion failed";
        default:                            return "Unknown Error";
    }
}


// basic free in c
unsigned char _c_free(void* ptr) {
    if (!ptr) return ERR_INVALID_PTR;
    free(ptr);
    return RES_EXIT_SUCCESS;
}