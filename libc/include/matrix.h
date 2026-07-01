#ifndef __MATRIX_H__
#define __MATRIX_H__


#include "global.h"
#include "array.h"

// For matrix inversion, we will use the LAPACK library
#if defined(_WIN32) || defined(_WIN64) || defined(__APPLE__)
    #include <openblas/cblas.h>   // get CblasRowMajor
    #include <openblas/lapacke.h> // header for inversion functions
#else
    #include <cblas.h>            // get CblasRowMajor
    #include <lapacke.h>          // header for inversion functions
#endif

// 2D matrix of float32 values (stored in row-major order) 
typedef struct {
    float* data;
    char owns_data; // boolean: 1 / 0
    uint32_t rows;
    uint32_t columns;
    uint32_t row_stride;
    uint32_t col_stride;
} Matrix;


// FREE
DLLEXPORT unsigned char free_matrix(Matrix** matrix);
// ALLOCATION
DLLEXPORT unsigned char allocate_2d_matrix_float32_without_data(uint32_t rows, uint32_t columns, Matrix** res_matrix);
DLLEXPORT unsigned char allocate_2d_matrix_float32(uint32_t rows, uint32_t columns, Matrix** res_matrix);
// INIT / GETTER / SETTER
DLLEXPORT unsigned char fill_from_list_2d_matrix(float* values, char add_the_bias_in_first_column, Matrix** matrix);
DLLEXPORT unsigned char fill_randomly_2d_matrix(float min, float max, char first_column_is_bias, Matrix** matrix);
DLLEXPORT unsigned char get_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float* res);
DLLEXPORT unsigned char set_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float value);
DLLEXPORT unsigned char get_transpose(Matrix* matrix, Matrix** transpose);
// OPERATIONS
DLLEXPORT unsigned char multiply_2d_matrix(Matrix* a, Matrix* b, Matrix** result);
DLLEXPORT unsigned char add_2d_matrix(Matrix* a, Matrix* b, Matrix** result);
DLLEXPORT unsigned char scalar_operation_2d_matrix(Matrix* matrix, float scalar, char is_addition, Matrix** result);
DLLEXPORT unsigned char inverse_2d_matrix(Matrix* A);

#endif 
