#ifndef __GLOBAL_H__
#define __GLOBAL_H__


#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
#include <time.h>


#ifdef _WIN32
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT
#endif


#define true 1
#define false 0


// Status codes
// -> unsigned char -> entre 0 et 255 status possibles pour le moment
typedef enum {
    RES_EXIT_SUCCESS,
    ERR_NOT_IMPLEMENTED,
    ERR_INVALID_PTR,
    ERR_MATH_DIV_BY_ZERO,
    ERR_LENGTH_ZERO,
    ERR_MEMORY_ALLOCATION,
    ERR_OUT_OF_BOUNDS,
    ERR_INVALID_MATRIX_DIMENSIONS,
    ERR_INVALID_MATRIX_SQUARE,
    ERR_INVALID_MATRIX_INVERSION_SINGULAR,
    ERR_INVALID_MATRIX_INVERSION,
    ERROR_SAVE_INVALID_NORMALIZATION_METHOD,
    ERROR_LOAD_INVALID_NORMALIZATION_METHOD,
    ERROR_INVALID_MODEL_TYPE,
    ERR_FILE_OPEN_TMP,
    ERR_FILE_RENAME_TMP,
    ERR_FILE_OPEN_RB,
} StatusCode;


#endif