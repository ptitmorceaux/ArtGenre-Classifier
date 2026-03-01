#ifndef __MATRIX_H__
#define __MATRIX_H__


#include "global.h"
#include "random.h"


// 2D matrix of float32 values (stored in row-major order) 
typedef struct {
    float* data;
    uint32_t rows;
    uint32_t columns;
    uint32_t row_stride;
    uint32_t col_stride; 
} Matrix;


DLLEXPORT unsigned char free_matrix(Matrix* matrix);
DLLEXPORT unsigned char allocate_2d_matrix_float32(uint32_t rows, uint32_t columns, Matrix** res_matrix);
DLLEXPORT unsigned char get_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float* res);
DLLEXPORT unsigned char set_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float value);
DLLEXPORT unsigned char fill_randomly_2d_matrix(float min, float max, Matrix** matrix); 
 
#endif 
