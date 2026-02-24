#ifndef _RANDOM_H
#define _RANDOM_H


#include "global.h"

DLLEXPORT unsigned char set_randomly_seed();
DLLEXPORT unsigned char set_seed(uint32_t seed);
DLLEXPORT unsigned char random_float(float min, float max, float* res);


#endif