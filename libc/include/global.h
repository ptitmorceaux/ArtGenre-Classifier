#ifndef __GLOBAL_H__
#define __GLOBAL_H__


#include <stdint.h>


#ifdef _WIN32
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT
#endif


// Error codes
// -> unsigned char -> entre 0 et 255 erreurs possibles pour le moment
typedef enum {
    EXIT_SUCCESS,
    ERR_INVALID_PTR,
    ERR_MATH_DIV_BY_ZERO,
} ErrorCode;

const char* get_status_message(unsigned char code);


#endif