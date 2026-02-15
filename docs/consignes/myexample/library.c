#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT
#endif

// 2 args: int32_t, int32_t
// return: int32_t
DLLEXPORT int32_t my_add(int32_t a, int32_t b) {
    return a + b;
}

// 3 args: float, int32_t, float* (ptr to float)
// return: void
DLLEXPORT void my_add_with_ptr_res(const float a, int32_t b, float* result) {
    *result = a + b;
}

// 0 args
// return: int32_t* (ptr to int32_t)
DLLEXPORT int32_t* return_allocate_int32t() {
    int32_t* int32t_ptr = (int32_t*)malloc(1 * sizeof(int32_t));
    if (int32t_ptr == NULL) return NULL;
    *int32t_ptr = 67;  // initialise la valeur à 67
    return int32t_ptr;
}

// 1 arg: void* (ptr de n'importe quel type)
// return: void (rien)
DLLEXPORT void free_ptr(void* ptr) {
    free(ptr);
}



