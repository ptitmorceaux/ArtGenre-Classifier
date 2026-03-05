import ctypes
from engine.interop.loader import Loader

class Matrix:
    
    def __init__(self, data: list[list[float | int]], rows: int, cols: int, ):
        self.
        self._rows = rows
        self._cols = cols


    #====== Constructeurs alternatifs ======#

    @classmethod
    def init_random(cls, rows: int, cols: int, max_value: float, min_value: float):
        Loader.check_ctype(rows, ctypes.c_uint32, "Matrix.init_random()")
        Loader.check_ctype(cols, ctypes.c_uint32, "Matrix.init_random()")
        Loader.check_ctype(max_value, ctypes.c_float, "Matrix.init_random()")
        Loader.check_ctype(min_value, ctypes.c_float, "Matrix.init_random()")
        
        Loader.call(
            "allocate_random_2d_matrix_float32",
            ctypes.c_uint32(rows),
            ctypes.c_uint32(cols),
            ctypes.c_float(max_value),
            ctypes.c_float(min_value)
        )
        pass

    #====== Properties ======#

    @property
    def rows(self):
        return self._rows
    @property
    def columns(self):
        return self._columns

    #====== Intern methods ======#

    def _set_matrix(self, data: list[list[float | int]]):
        
        self._rows = len(data)
        self._columns = len(data[0])
        
        Loader.call(
            "allocate_2d_matrix_float32",
            ctypes.c_uint32(self._rows),
            ctypes.c_uint32(self._columns),
            prefix_errmsg="Matrix._set_matrix()"
        )

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                Loader.call(
                    "set_2d_matrix_float32_value",
                    ctypes.c_uint32(i),
                    ctypes.c_uint32(j),
                    ctypes.c_float(value),
                    prefix_errmsg="Matrix._set_matrix()"
                )
    



    #====== Operations Matrix ======#

    def transpose(self):
        pass

    def multiply(self, other: "Matrix"):
        pass

    def add(self, other: "Matrix"):
        pass