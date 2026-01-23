import ctypes
from engine.interop.loader import Loader


class ArrayFloat32Ptr:
    # On charge le loader une seule fois pour la classe
    _loader = Loader()

    def __init__(self, data: list[float, int]):
        self._set_array(data)
    

    #====== Constructeurs alternatifs ======#

    @classmethod
    def init_from_incrementing_numbers(cls, length: int):
        cls._loader.check_ctype(length, ctypes.c_uint32, "ArrayFloat32Ptr.init_from_incrementing_numbers()")
        
        ptr_result = ctypes.POINTER(ctypes.c_float)()
        
        cls._loader.call(
            "ALLOCATE_float32_array_of_incrementing_numbers",
            ctypes.c_uint32(length),
            ctypes.byref(ptr_result),
            prefix_errmsg="ArrayFloat32Ptr.init_from_incrementing_numbers()"
        )

        data = [ptr_result[i] for i in range(length)]
        cls._loader.call(
            "_c_free",
            ctypes.cast(ptr_result, ctypes.c_void_p),
            prefix_errmsg="ArrayFloat32Ptr.init_from_incrementing_numbers()"
        )
        return cls(data)


    #====== Properties ======#

    def _get_array(self):
        return self._py_list
    
    def _set_array(self, data: list[float, int]):
        if not data or not isinstance(data, list):
            raise TypeError("ArrayFloat32Ptr.__init__(): `data` must be a non-empty list of floats")
        if not all(isinstance(x, (float, int)) for x in data):
            raise TypeError("ArrayFloat32Ptr.__init__(): all elements of the list must be floats")
        
        length = len(data)
        self._loader.check_ctype(length, ctypes.c_uint32, "ArrayFloat32Ptr.__init__()")
        
        self._length = length
        self._py_list = data
        
        # On crée un tableau ctypes
        ArrayType = ctypes.c_float * self._length
        self._c_array = ArrayType(*[ctypes.c_float(x) for x in data])
        self._c_length = ctypes.c_uint32(self._length)

    array = property(_get_array, _set_array)


    #====== Public ======#

    def sum(self) -> float:
        """Calcule la somme en utilisant la lib C"""
        c_res = ctypes.c_float()
        self._loader.call(
            "sum_float32_array",
            self._c_array,
            self._c_length,
            ctypes.byref(c_res),
            prefix_errmsg="ArrayFloat32Ptr.sum()"
        )
        return c_res.value