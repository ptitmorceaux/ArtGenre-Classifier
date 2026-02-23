#include "../include/random.h"


#if defined(_WIN32) || defined(_WIN64)
#include <windows.h>

uint32_t get_millisecond_time() {
    FILETIME ft;
    GetSystemTimeAsFileTime(&ft);
    ULARGE_INTEGER uli;
    uli.LowPart  = ft.dwLowDateTime;
    uli.HighPart = ft.dwHighDateTime;
    // Convert in ms (FILETIME en 100-ns)
    return (uint32_t)(uli.QuadPart / 10000);
}
#else
#include <sys/time.h>

uint32_t get_millisecond_time() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (uint32_t)(tv.tv_sec * 1000 + tv.tv_usec / 1000);
}
#endif


// Return millisecond time + address of a local variable
uint32_t getRandomSeed() {
    int stack_var;
    uint32_t time_seed = get_millisecond_time();
    uint32_t addr_seed = (uint32_t)(uintptr_t)&stack_var;
    return (time_seed ^ addr_seed);
}


DLLEXPORT unsigned char set_randomly_seed() {
    uint32_t seed = getRandomSeed();
    srand(seed);
    return RES_EXIT_SUCCESS;
}

DLLEXPORT unsigned char set_seed(uint32_t seed) {
    srand(seed);
    return RES_EXIT_SUCCESS;
}


unsigned char random_float(float min, float max, float* res) {
    if (!res) return ERR_INVALID_PTR;
    
    if (min == max) {
        *res = min;
        return RES_EXIT_SUCCESS;
    }

    if (min > max) {
        float tmp = max;
        max = min;
        min = tmp;
    }

    *res = (float)rand() / (float)RAND_MAX * (max - min) + min;
    return RES_EXIT_SUCCESS;
}