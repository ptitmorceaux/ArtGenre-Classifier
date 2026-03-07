#include "../include/matrix.h"


/*===============================================================*/

// ALLOCATION

unsigned char allocate_2d_matrix_float32_without_data(uint32_t rows, uint32_t columns, Matrix** res_matrix) {
    if (!res_matrix) return ERR_INVALID_PTR;
    *res_matrix = NULL;
    if (rows == 0 || columns == 0) return ERR_LENGTH_ZERO;

    Matrix* matrix = (Matrix*) malloc(sizeof(Matrix));
    if (!matrix) return ERR_ALLOCATION_FAILED;
    
    matrix->data = NULL;
    matrix->owns_data = false;
    matrix->rows = rows;
    matrix->columns = columns;
    matrix->row_stride = columns;
    matrix->col_stride = 1;

    *res_matrix = matrix;
    return RES_EXIT_SUCCESS; 
}

unsigned char allocate_2d_matrix_float32(uint32_t rows, uint32_t columns, Matrix** res_matrix) {
    
    unsigned char status = allocate_2d_matrix_float32_without_data(rows, columns, res_matrix);
    if (status != RES_EXIT_SUCCESS) return status;
    
    Matrix* matrix = *res_matrix;
    
    matrix->data = (float*) malloc(rows * columns * sizeof(float));
    if (!matrix->data) {
        free_matrix(res_matrix);
        return ERR_ALLOCATION_FAILED;
    }
    matrix->owns_data = true;
    
    return RES_EXIT_SUCCESS; 
}

/*===============================================================*/

// INIT

unsigned char fill_from_list_2d_matrix(float* values, Matrix** matrix) {
    if (!matrix || !(*matrix) || !(*matrix)->data) return ERR_INVALID_PTR;
    if (!values) {
        free_matrix(matrix);
        return ERR_INVALID_PTR;
    }
    
    Matrix* m = *matrix;
    
    for (uint32_t i = 0; i < m->rows * m->columns; i++) {
        m->data[i] = values[i];
    }
    
    return RES_EXIT_SUCCESS;
}

unsigned char fill_randomly_2d_matrix(float min, float max, Matrix** matrix) {
    if (!matrix || !(*matrix) || !(*matrix)->data) return ERR_INVALID_PTR;
    Matrix* m = *matrix;

    for (uint32_t i = 0; i < m->rows * m->columns; i++) {
        
        unsigned char status = random_float(min, max, &m->data[i]);
        if (status != RES_EXIT_SUCCESS) {
            free_matrix(matrix);
            return status;
        }
    }
    return RES_EXIT_SUCCESS;
}

unsigned char get_transpose_2d_matrix(Matrix* matrix, Matrix** res) {
    if (!matrix || !matrix->data || !res) return ERR_INVALID_PTR;
    
    unsigned char status = allocate_2d_matrix_float32_without_data(matrix->columns, matrix->rows, res);
    if (status != RES_EXIT_SUCCESS) return status;
    
    Matrix *transposed = *res;
    
    transposed->data = matrix->data;
    transposed->owns_data = false;
    transposed->row_stride = matrix->col_stride;
    transposed->col_stride = matrix->row_stride;
    
    return RES_EXIT_SUCCESS;
}


/*===============================================================*/

// OPERATIONS

uint32_t get_index_2d_matrix(Matrix* matrix, uint32_t row, uint32_t col) {
    return row * matrix->row_stride + col * matrix->col_stride;
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

// Matrix Operations

unsigned char multiply_2d_matrix(Matrix* a, Matrix* b, Matrix** res) {
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

                // TODO: fix later as it is not optimal to check status at each iteration

                status = get_element_2d_matrix(a, i, k, &a_ik);
                if (status != RES_EXIT_SUCCESS) {
                    free_matrix(res);
                    return status;
                }

                status = get_element_2d_matrix(b, k, j, &b_kj);
                if (status != RES_EXIT_SUCCESS) {
                    free_matrix(res);
                    return status;
                }

                sum += a_ik * b_kj;
            }

            status = set_element_2d_matrix(result, i, j, sum);
            if (status != RES_EXIT_SUCCESS) {
                free_matrix(res);
                return status;
            }
        }
    }
    return RES_EXIT_SUCCESS;
}

unsigned char add_2d_matrix(Matrix* a, Matrix* b, Matrix** res) {
    if (!a || !b || !res) return ERR_INVALID_PTR;
    if (a->rows != b->rows || a->columns != b->columns) return ERR_INVALID_MATRIX_DIMENSIONS;

    unsigned char status = allocate_2d_matrix_float32(a->rows, a->columns, res);
    if (status != RES_EXIT_SUCCESS) return status;

    Matrix* result = *res;
    for (uint32_t i = 0; i < a->rows; i++) {
        for (uint32_t j = 0; j < a->columns; j++) {
            float a_ij, b_ij;

            status = get_element_2d_matrix(a, i, j, &a_ij);
            if (status != RES_EXIT_SUCCESS) {
                free_matrix(res);
                return status;
            }

            status = get_element_2d_matrix(b, i, j, &b_ij);
            if (status != RES_EXIT_SUCCESS) {
                free_matrix(res);
                return status;
            }

            status = set_element_2d_matrix(result, i, j, a_ij + b_ij);
            if (status != RES_EXIT_SUCCESS) {
                free_matrix(res);
                return status;
            }
        }
    }
    return RES_EXIT_SUCCESS;
}

unsigned char scalar_operation_2d_matrix(Matrix** m, float scalar, char is_addition) {
    if (!m || !*m) return ERR_INVALID_PTR;

    Matrix* matrix = *m;
    Matrix* tmp = NULL;
    unsigned char status = allocate_2d_matrix_float32(matrix->rows, matrix->columns, &tmp);
    if (status != RES_EXIT_SUCCESS) return status;

    for (uint32_t i = 0; i < matrix->rows; i++) {
        for (uint32_t j = 0; j < matrix->columns; j++) {
            float value;
            status = get_element_2d_matrix(matrix, i, j, &value);
            if (status != RES_EXIT_SUCCESS) {
                free_matrix(&tmp);
                return status;
            }
            status = set_element_2d_matrix(tmp, i, j, is_addition ? value + scalar : value * scalar);
            if (status != RES_EXIT_SUCCESS) {
                free_matrix(&tmp);
                return status;
            }
        }
    }
    free_matrix(m);
    *m = tmp;
    return RES_EXIT_SUCCESS;
}

/*===============================================================*/


// FREE //

unsigned char free_matrix(Matrix** m) {
    Matrix *matrix = *m;
    if (!matrix) return ERR_INVALID_PTR;
    if (matrix->data && matrix->owns_data) free(matrix->data);
    free(matrix);
    *m = NULL;
    return RES_EXIT_SUCCESS;
}
