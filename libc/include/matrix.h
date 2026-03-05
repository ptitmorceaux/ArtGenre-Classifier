#ifndef __MATRIX_H__
#define __MATRIX_H__


#include "global.h"
#include "random.h"


// 2D matrix of float32 values (stored in row-major order) 
typedef struct {
    float* data;
    char owns_data;
    uint32_t rows;
    uint32_t columns;
    uint32_t row_stride;
    uint32_t col_stride;
} Matrix;


// FREE
DLLEXPORT unsigned char free_matrix(Matrix** m);
// ALLOCATION
DLLEXPORT unsigned char allocate_2d_matrix_float32_without_data(uint32_t rows, uint32_t columns, Matrix** res_matrix);
DLLEXPORT unsigned char allocate_2d_matrix_float32(uint32_t rows, uint32_t columns, Matrix** res_matrix);
// INIT / GETTER / SETTER
DLLEXPORT unsigned char init_values_2d_matrix(float* values, Matrix** matrix);
DLLEXPORT unsigned char fill_randomly_2d_matrix(float min, float max, Matrix** matrix);
DLLEXPORT unsigned char get_transpose_2d_matrix(Matrix* matrix, Matrix** res);
DLLEXPORT unsigned char get_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float* res);
DLLEXPORT unsigned char set_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float value);
// OPERATIONS
DLLEXPORT unsigned char multiply_2d_matrix(Matrix* a, Matrix* b, Matrix** res);
DLLEXPORT unsigned char add_2d_matrix(Matrix* a, Matrix* b, Matrix** res);
DLLEXPORT unsigned char scalar_operation_2d_matrix(Matrix** m, float scalar, char is_addition);


#endif 
