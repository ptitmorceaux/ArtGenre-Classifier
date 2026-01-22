#include "../include/global.h"


// status code to string
DLLEXPORT const char* get_status_message(unsigned char code) {
    switch (code) {
        case RES_EXIT_SUCCESS:      return "OK";
        case ERR_INVALID_PTR:       return "Invalid Pointer";
        case ERR_MATH_DIV_BY_ZERO:  return "Division by Zero";
        case ERR_LENGTH_ZERO:       return "Length is Zero";
        default:                    return "Unknown Error";
    }
}


// basic free in c
DLLEXPORT unsigned char _c_free(void* ptr) {
    if (!ptr) return ERR_INVALID_PTR;
    free(ptr);
    return RES_EXIT_SUCCESS;
}