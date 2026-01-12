#ifndef __GLOBAL_H__
#define __GLOBAL_H__

    #include <stdint.h>

    #ifdef _WIN32
        #define EXPORT __declspec(dllexport)
    #else
        #define EXPORT
    #endif

#endif