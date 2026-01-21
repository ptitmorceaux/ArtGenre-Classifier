#include "../include/global.h"

// error code to string
DLLEXPORT const char* get_status_message(unsigned char code) {
    switch (code) {
        case EXIT_SUCCESS:          return "OK";
        case ERR_INVALID_PTR:       return "Invalid Pointer";
        case ERR_MATH_DIV_BY_ZERO:  return "Division by Zero";
        default:                    return "Unknown Error";
    }
}