#ifndef __GLOBAL_H__
#define __GLOBAL_H__


#include <stdlib.h>
#include <stdint.h>


#ifdef _WIN32
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT
#endif


// Status codes
// -> unsigned char -> entre 0 et 255 status possibles pour le moment
typedef enum {
    RES_EXIT_SUCCESS,
    ERR_INVALID_PTR,
    ERR_MATH_DIV_BY_ZERO,
    ERR_LENGTH_ZERO,
    ERR_ALLOCATION_FAILED
} StatusCode;


#endif