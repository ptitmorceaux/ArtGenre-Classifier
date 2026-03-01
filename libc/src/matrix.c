#include "../include/matrix.h"


/*===============================================================*/

// ALLOCATION

unsigned char allocate_2d_matrix_float32(uint32_t rows, uint32_t columns, Matrix** res_matrix) {
    if (!res_matrix) return ERR_INVALID_PTR;
    *res_matrix = NULL;
    if (rows == 0 || columns == 0) return ERR_LENGTH_ZERO;

    Matrix* matrix = (Matrix*) malloc(sizeof(Matrix));
    if (!matrix) return ERR_ALLOCATION_FAILED;
    
    matrix->data = (float*) malloc(rows * columns * sizeof(float));
    if (!matrix->data) {
        free(matrix);
        return ERR_ALLOCATION_FAILED;
    }

    matrix->rows = rows;
    matrix->columns = columns;
    matrix->row_stride = rows * sizeof(float);
    matrix->col_stride = sizeof(float);

    *res_matrix = matrix;
    return RES_EXIT_SUCCESS; 
}

/*===============================================================*/

// INIT

unsigned char fill_randomly_2d_matrix(float min, float max, Matrix** matrix) {
    if (!matrix || !(*matrix) || !(*matrix)->data) return ERR_INVALID_PTR;
    Matrix* m = *matrix;

    for (uint32_t i = 0; i < m->rows * m->columns; i++) {
        
        unsigned char status = random_float(min, max, &m->data[i]);
        if (status != RES_EXIT_SUCCESS) {
            free_matrix(m);
            *matrix = NULL;
            return status;
        }
    }
    return RES_EXIT_SUCCESS;
}


/*===============================================================*/

// OPERATIONS

uint32_t get_index_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col) {
    return row * matrix->columns + col;
}

unsigned char get_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float* res) {
    if (!matrix || !matrix->data || !res) return ERR_INVALID_PTR;
    if (row >= matrix->rows || col >= matrix->columns) return ERR_OUT_OF_BOUNDS;
    
    uint32_t index = get_index_2d_matrix(matrix, row, col);
    *res = matrix->data[index]; 
    return RES_EXIT_SUCCESS;
}

unsigned char set_element_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col, float value) {
    if (!matrix || !matrix->data) return ERR_INVALID_PTR;
    if (row >= matrix->rows || col >= matrix->columns) return ERR_OUT_OF_BOUNDS;
    
    uint32_t index = get_index_2d_matrix(matrix, row, col);
    matrix->data[index] = value; 
    return RES_EXIT_SUCCESS;
}


// TODO: implement matrix operations (multiplication, "addition", transposé) and corresponding tests (in pytest)
// INFO: https://www.geeksforgeeks.org/maths/matrix-operations/

unsigned char multiplication_2d_matrix(Matrix* a, Matrix* b, Matrix** res) {
    if (!a || !b || !res) return ERR_INVALID_PTR;
    if (a->columns != b->rows) return ERR_INVALID_MATRIX_DIMENSIONS;

    unsigned char status = allocate_2d_matrix_float32(a->rows, b->columns, res);
    if (status != RES_EXIT_SUCCESS) return status;

    Matrix* result = *res;
    for (uint32_t i = 0; i < a->rows; i++) {
        for (uint32_t j = 0; j < b->columns; j++) {
            float sum = 0;
            for (uint32_t k = 0; k < a->columns; k++) {
                float a_ik, b_kj;
                get_element_2d_matrix(a, i, k, &a_ik);
                get_element_2d_matrix(b, k, j, &b_kj);
                sum += a_ik * b_kj;
            }
            set_element_2d_matrix(result, i, j, sum);
        }
    }
    return RES_EXIT_SUCCESS;
}

unsigned char substraction_2d_matrix(Matrix* a, Matrix* b, Matrix** res) {
    if (!a || !b || !res) return ERR_INVALID_PTR;
    if (a->rows != b->rows || a->columns != b->columns) return ERR_INVALID_MATRIX_DIMENSIONS;

    unsigned char status = allocate_2d_matrix_float32(a->rows, a->columns, res);
    if (status != RES_EXIT_SUCCESS) return status;

    Matrix* result = *res;
    for (uint32_t i = 0; i < a->rows; i++) {
        for (uint32_t j = 0; j < a->columns; j++) {
            float a_ij, b_ij;
            get_element_2d_matrix(a, i, j, &a_ij);
            get_element_2d_matrix(b, i, j, &b_ij);
            set_element_2d_matrix(result, i, j, a_ij - b_ij);
        }
    }
    return RES_EXIT_SUCCESS;
}
/*===============================================================*/


// FREE //

unsigned char free_matrix(Matrix* matrix) {
    if (!matrix) return ERR_INVALID_PTR;
    if (matrix->data) free(matrix->data);
    free(matrix);
    return RES_EXIT_SUCCESS;
}
