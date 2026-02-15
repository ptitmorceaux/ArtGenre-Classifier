
import ctypes
import os

def main():

    """ Etape 1: import lib """
    dll_path = os.path.join(os.path.dirname(__file__), "library.dll")
    lib = ctypes.cdll.LoadLibrary(dll_path)


    """
    Etape 2: set up function signatures
        - argtypes: liste des types des arguments (empty list if no arg)
        - restype:  return type (None si pas de return)
    """

    lib.my_add.argtypes = [                 # 2 args:
        ctypes.c_int32,                     #   int32_t
        ctypes.c_int32                      #   int32_t
    ]
    lib.my_add.restype = ctypes.c_int32     # return: int32_t

    lib.my_add_with_ptr_res.argtypes = [    # 3 args:
        ctypes.c_float,                     #   float
        ctypes.c_int32,                     #   int32_t
        ctypes.POINTER(ctypes.c_float)      #   float* (pointer to float)
    ]
    lib.my_add_with_ptr_res.restype = None  # return: void

    lib.return_allocate_int32t.argtypes = []             # 0 args
    lib.return_allocate_int32t.restype = ctypes.POINTER(ctypes.c_int32) # return: int32_t*
        
    lib.free_ptr.argtypes = [       # 1 arg:
        ctypes.c_void_p             #   void* (= ptr de n'importe quel type)
    ]
    lib.free_ptr.restype = None     # return: void


    """ Etape 3: call functions """

    # CALL: int32_t my_add(int32_t a, int32_t b)
    a = 5
    b = 7
    # conversion en types C
    arg_a = ctypes.c_int32(a)
    arg_b = ctypes.c_int32(b)
    # call de la fonction C
    result_add = lib.my_add(arg_a, arg_b)
    # retourne directement un int Python car
    # ctypes convertit automatiquement le résultat de type C en type Python
    print(f"my_add({a}, {b}) = {result_add}")


    # CALL: void my_add_with_ptr_res(float a, int32_t b, float* res)
    a = 3.5
    b = 4
    # conversion en types C
    arg_a = ctypes.c_float(a)
    arg_b = ctypes.c_int32(b)
    #
    # variable de type float pour stocker le résultat
    res = ctypes.c_float()
    #
    # NOTE: ctypes.byref(res) -> passe un pointeur vers res à la fonction C
    #
    # call de la fonction C, qui va stocker le résultat dans res via le pointeur
    lib.my_add_with_ptr_res(arg_a, arg_b, ctypes.byref(res))
    print(f"my_add_with_ptr_res({a}, {b}) = {res.value}")
    #
    # NOTE: Ici on utilise .value pour accéder à la valeur stockée dans res,
    #       car res a été créée par ctypes et non nativement par Python ou C


    # CALL: int32_t* return_allocate_int32t()
    # CALL: void free_ptr(void* ptr)
    #
    # NOTE: Python ne gère pas la mémoire allouée par C,
    #       il faut donc free manuellement
    #
    # call de la fonction C qui retourne un pointeur vers un int32_t
    # alloué dynamiquement par la fonction C
    int32t_ptr = lib.return_allocate_int32t()
    #
    # NOTE: Il faut vérifier que le pointeur n'est pas NULL avant de l'utiliser
    #
    if int32t_ptr:
        #
        # On accede à la valeur pointée par int32t_ptr en
        # utilisant l'opérateur de déréférencement [] de ctypes :
        #
        #   int32t_ptr[0] est équivalent à *int32t_ptr en C,
        #   int32t_ptr[1] serait équivalent à *(int32t_ptr + 1) en C, etc.
        #
        int32t_value = int32t_ptr[0]
        print(f"return_allocate_int32t() = {int32t_value}")
        #
        # NOTE: il ne faut PAS oublier de free le ptr
        #
        lib.free_ptr(int32t_ptr)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")