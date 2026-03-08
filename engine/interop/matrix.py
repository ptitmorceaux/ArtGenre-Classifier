# ruff:noqa
import ctypes
import numpy as np
from engine.interop.loader import Loader
import engine.interop.array as C_Array


class Matrix2dFloat32:

    def __init__(self, rows: int, cols: int) -> "Matrix2dFloat32":
        """Constructeur de la classe Matrix2dFloat32: intialise une matrice None"""
        self._matrix = None
        self._rows = rows
        self._cols = cols
        self._length = rows * cols

    #====== Constructeurs alternatifs ======#

    @classmethod
    def init_random(cls, rows: int, cols: int, max_value: float, min_value: float) -> "Matrix2dFloat32":
        """Initialise une matrice avec des valeurs aléatoires entre min_value et max_value"""
        prefix_err = "Matrix2dFloat32.init_random()"
        obj = cls(rows, cols)

        obj._allocate_matrix_2d(rows=rows, cols=cols, prefix_errmsg=prefix_err)
        obj.fill_randomly(max_value=max_value, min_value=min_value, prefix_errmsg=prefix_err)

        return obj


    @classmethod
    def init_from_list(cls, rows: int, cols: int, data: list[float]) -> "Matrix2dFloat32":
        """Initialise une matrice à partir d'une liste de données"""
        prefix_err = "Matrix2dFloat32.init_from_list()"
        obj = cls(rows, cols)

        obj._length = len(data)  # On met à jour la longueur des données pour les vérifications internes

        obj._allocate_matrix_2d(rows=rows, cols=cols, prefix_errmsg=prefix_err)
        obj.fill_from_list(data=data, prefix_errmsg=prefix_err)

        return obj
    
    @classmethod
    def _init_from_C_matrix(cls, rows: int, cols: int, c_matrix_ptr: ctypes.c_void_p) -> "Matrix2dFloat32":
        """Initialise une matrice à partir d'un pointeur vers une matrice C déjà allouée"""
        obj = cls(rows, cols)
        obj._matrix = c_matrix_ptr
        obj.check_dimensions(rows, cols, obj.length, "Matrix2dFloat32._init_from_C_matrix()")
        return obj

    #====== Properties ======#

    # NOTE: Pas besoin de setter dcp la on peut juste utiliser @property puis return

    # TODO: GETTER matrix (ptr vers la matrice C)

    # TODO: GETTER rows
    
    # TODO: GETTER cols

    # TODO: GETTER length

    #====== Intern methods ======#

    def _allocate_matrix_2d(self, rows: int, cols: int, prefix_errmsg: str = "") -> None:
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32._allocate_matrix_2d()" if prefix_errmsg else "Matrix2dFloat32._allocate_matrix_2d()"
        self.check_dimensions(rows, cols, self.length, prefix_err)
        
        # TODO: Checker la range des arguments avec Loader.check_primitive_values_range()
        
        # TODO: Appeler la fonction C `allocate_2d_matrix_float32()` via Loader.call()
        
        raise NotImplementedError(f"{prefix_err}: Not implemented yet.")


    def _free_matrix(self):
        if self.matrix is not None:
            # TODO: appeler la fonction C `free_matrix()` via Loader.call() pour
            #       libérer la mémoire de la matrice (self.matrix)
            raise ValueError("Matrix2dFloat32._free_matrix(): Not implemented yet.")
        
        self._matrix = None
        self._rows = 0
        self._cols = 0
        self._length = 0
    

    def __del__(self):
        self._free_matrix()

    #====== Extern methods ======#

    @staticmethod
    def check_dimensions(rows: int, cols: int, length: int, prefix_errmsg: str = "") -> None:
        """Vérifie que les dimensions de la matrice sont cohérentes avec la longueur des données fournies."""
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32.check_dimensions()" if prefix_errmsg else "Matrix2dFloat32.check_dimensions()"
        # TODO: raise une ValueError si les dimensions ne sont pas cohérentes avec la longueur des données fournies


    def fill_from_list(self, data: list[float], prefix_errmsg: str = "") -> None:
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32.fill_from_list()" if prefix_errmsg else "Matrix2dFloat32.fill_from_list()"
        self.check_dimensions(self.rows, self.cols, len(data), prefix_err)

        float32Array = C_Array.get_float32_array_from_py_list(data, prefix_err)

        # TODO: Appeler la fonction C `fill_from_list_2d_matrix` via Loader.call()
        #       pour remplir la matrice avec les données fournies dans la liste
        
        raise NotImplementedError(f"{prefix_err}: Not implemented yet.")

    
    def fill_randomly(self, max_value: float, min_value: float, prefix_errmsg: str = "") -> None:
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32.fill_randomly()" if prefix_errmsg else "Matrix2dFloat32.fill_randomly()"
        self.check_dimensions(self.rows, self.cols, self.length, prefix_err)

        # TODO: Checker la range des arguments avec Loader.check_primitive_values_range()
        
        # TODO: Appeler la fonction C `fill_randomly_2d_matrix` via Loader.call()
        #       pour remplir la matrice avec des valeurs aléatoires entre min_value et max_value
        
        raise NotImplementedError(f"{prefix_err}: Not implemented yet.")

    #====== Operations Matrix ======#

    @staticmethod
    def _operation_between_2_matrices(a: "Matrix2dFloat32", b: "Matrix2dFloat32", func_name: str, is_self_update: bool = False, prefix_errmsg: str = "") -> "Matrix2dFloat32":
        """Effectue une opération entre 2 matrices (ex: multiplication, addition) en appelant la fonction C correspondante via Loader.call()"""
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32._operation_between_2_matrices()" if prefix_errmsg else "Matrix2dFloat32._operation_between_2_matrices()"
        
        # TODO: Checker les instances de `a` et `b` pour s'assurer qu'elles sont bien
        #       des instances de Matrix2dFloat32 (sinon -> raise ValueError)
        
        # TODO: Checker si `a` et `b` ne sont pas None (sinon -> raise ValueError)
        
        if is_self_update and a.cols == b.cols:
            res_matrix = a.matrix
        
        else:
            # TODO: Initialiser la matrice résultat à `ctypes.c_void_p()`
            #       NOTE: equivalent à un ptr -> `void* matrix` ou `Matrix* matrix`
            raise NotImplementedError(f"{prefix_err}: Not implemented yet.")

        # TODO: Appeler la fonction C `func_name` via Loader.call() en passant les pointeurs vers les
        #       matrices `a` et `b` et le pointeur vers la matrice résultat -> ctypes.byref(VARIABLE_MATRICE_RES)

        rows_res = a.rows
        cols_res = b.cols

        raise NotImplementedError(f"{prefix_err}: Not implemented yet.")
        
        # TODO: Remplacer `VARIABLE_MATRICE_RES` par le nom de la variable correspondante
        return Matrix2dFloat32._init_from_C_matrix(rows_res, cols_res, VARIABLE_MATRICE_RES)
    

    @staticmethod
    def _scalar_operation(matrix: "Matrix2dFloat32", value: float, is_addition: bool, is_self_update: bool = True, prefix_errmsg: str = "") -> "Matrix2dFloat32":
        """Effectue une opération entre une matrice et un scalaire (ex: multiplication, addition) en appelant la fonction C correspondante via Loader.call()"""
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32._scalar_operation()" if prefix_errmsg else "Matrix2dFloat32._scalar_operation()"

        # TODO: Checker l'instance de `matrix` pour s'assurer qu'elle est bien une
        #       instance de Matrix2dFloat32 (sinon -> raise ValueError)

        # TODO: Checker si `matrix.matrix` n'est pas None (sinon -> raise ValueError)

        # TODO: Checker la range de l'argument `value` avec Loader.check_primitive_values_range()

        if is_self_update:
            res_matrix = matrix.matrix
        
        else:
            # TODO: Initialiser la matrice résultat à `ctypes.c_void_p()`
            #       NOTE: equivalent à un ptr -> `void* matrix` ou `Matrix* matrix`
            raise NotImplementedError(f"{prefix_err}: Not implemented yet.")

        # TODO: Appeler la fonction C `scalar_operation_2d_matrix` via Loader.call() en passant le pointeur
        #       vers la matrice, la valeur scalaire et le ptr vers la matrice res

        raise NotImplementedError(f"{prefix_err}: Not implemented yet.")

        # TODO: Remplacer `VARIABLE_MATRICE_RES` par le nom de la variable correspondante
        return Matrix2dFloat32._init_from_C_matrix(matrix.rows, matrix.cols, VARIABLE_MATRICE_RES)
    
    
    @staticmethod
    def mult(a: "Matrix2dFloat32" | float, b: "Matrix2dFloat32" | float, is_self_update: bool = True, prefix_errmsg: str = "") -> "Matrix2dFloat32":
        """Effectue une multiplication entre une matrice et une autre matrice ou un scalaire"""
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32.mult()" if prefix_errmsg else "Matrix2dFloat32.mult()"

        if isinstance(b, Matrix2dFloat32) and isinstance(a, (float, int, bool)):
            a, b = b, a

        if isinstance(a, Matrix2dFloat32) and isinstance(b, Matrix2dFloat32):
            return Matrix2dFloat32._operation_between_2_matrices(
                a = a,
                b = b,
                func_name = "multiply_2d_matrix",
                is_self_update = is_self_update,
                prefix_errmsg = prefix_err
            )
        
        elif isinstance(b, (float, int, bool)):
            return Matrix2dFloat32._scalar_operation(
                matrix = a,
                value = b,
                is_addition = False,
                is_self_update = is_self_update,
                prefix_errmsg = prefix_err
            )
        
        raise ValueError(f"{prefix_err}: Unsupported combinaison of type for operation: {type(a)} and {type(b)}. Expected (Matrix2dFloat32, float) or (Matrix2dFloat32, Matrix2dFloat32).")


    @staticmethod
    def add(a: "Matrix2dFloat32" | float, b: "Matrix2dFloat32" | float, is_self_update: bool = True, prefix_errmsg: str = "") -> "Matrix2dFloat32":
        """Effectue une addition entre une matrice et une autre matrice ou un scalaire"""
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32.add()" if prefix_errmsg else "Matrix2dFloat32.add()"

        if isinstance(b, Matrix2dFloat32) and isinstance(a, (float, int, bool)):
            a, b = b, a

        if isinstance(a, Matrix2dFloat32) and isinstance(b, Matrix2dFloat32):
            return Matrix2dFloat32._operation_between_2_matrices(
                a = a,
                b = b,
                func_name = "add_2d_matrix",
                is_self_update = is_self_update,
                prefix_errmsg = prefix_err
            )
        
        elif isinstance(a, Matrix2dFloat32) and isinstance(b, (float, int, bool)):
            return Matrix2dFloat32._scalar_operation(
                matrix = a,
                value = b,
                is_addition = True,
                is_self_update = is_self_update,
                prefix_errmsg = prefix_err
            )
        
        raise ValueError(f"{prefix_err}: Unsupported combinaison of type for operation: {type(a)} and {type(b)}. Expected (Matrix2dFloat32, float) or (Matrix2dFloat32, Matrix2dFloat32).")


    @staticmethod
    def negative(matrix: "Matrix2dFloat32") -> "Matrix2dFloat32":
        """Change le contenu de la matrice par son opposé (* -1)"""
        return Matrix2dFloat32.mult(matrix, -1)
    

    @staticmethod
    def sub(a: "Matrix2dFloat32" | float, b: "Matrix2dFloat32" | float, is_self_update: bool = True, prefix_errmsg: str = "") -> "Matrix2dFloat32":
        """Effectue une soustraction entre une matrice et une autre matrice ou un scalaire"""
        prefix_err = f"{prefix_errmsg}: Matrix2dFloat32.sub()" if prefix_errmsg else "Matrix2dFloat32.sub()"

        if isinstance(b, Matrix2dFloat32):
            Matrix2dFloat32.negative(b)
        
        if isinstance(a, Matrix2dFloat32) and isinstance(b, Matrix2dFloat32):
            try:
                return Matrix2dFloat32.add(
                    a = a,
                    b = b,
                    is_self_update = is_self_update,
                    prefix_errmsg = prefix_err
                )
            finally:
                Matrix2dFloat32.negative(b)
        
        if isinstance(b, (float, int, bool)) and isinstance(a, Matrix2dFloat32):
            return Matrix2dFloat32._scalar_operation(
                matrix = a,
                value = b * -1,
                is_addition = True,
                is_self_update = is_self_update,
                prefix_errmsg = prefix_err
            )
        
        if isinstance(a, (float, int, bool)) and isinstance(b, Matrix2dFloat32):
            try:
                return Matrix2dFloat32._scalar_operation(
                    matrix = b,
                    value = a,
                    is_addition = True,
                    is_self_update = is_self_update,
                    prefix_errmsg = prefix_err
                )
            finally:
                if not is_self_update:
                    Matrix2dFloat32.negative(b)
        
        raise ValueError(f"{prefix_err}: Unsupported combinaison of type for operation: {type(a)} and {type(b)}. Expected (Matrix2dFloat32, float) or (Matrix2dFloat32, Matrix2dFloat32).")


    # Usage: new_matrix = matrix_self * other
    def __mul__(self, other: "Matrix2dFloat32" ) -> "Matrix2dFloat32":
        return Matrix2dFloat32.mult(
            a = self,
            b = other,
            is_self_update = False,
            prefix_errmsg = "Matrix2dFloat32.__mul__()"
        )
    
    # Usage: new_matrix = other * matrix_self
    def __rmul__(self, other: "Matrix2dFloat32") -> "Matrix2dFloat32":
        return Matrix2dFloat32.mult(
            a = other,
            b = self,
            is_self_update = False,
            prefix_errmsg = "Matrix2dFloat32.__rmul__()"
        )
    
    # Usage: matrix_self *= other
    def __imul__(self, other: "Matrix2dFloat32" | float) -> "Matrix2dFloat32":
        return Matrix2dFloat32.mult(
            a = self,
            b = other,
            is_self_update = True,
            prefix_errmsg = "Matrix2dFloat32.__imul__()"
        )
    

    # Usage: new_matrix = matrix_self @ another_matrix
    # Equivalent: matrix_self * another_matrix
    def __matmul__(self, another_matrix: "Matrix2dFloat32") -> "Matrix2dFloat32":
        return Matrix2dFloat32._operation_between_2_matrices(
            a = self,
            b = another_matrix,
            func_name = "multiply_2d_matrix",
            is_self_update = False,
            prefix_errmsg = "Matrix2dFloat32.__matmul__()"
        )
    
    # Usage: new_matrix = another_matrix @ matrix_self
    def __rmatmul__(self, another_matrix: "Matrix2dFloat32") -> "Matrix2dFloat32":
        return Matrix2dFloat32._operation_between_2_matrices(
            a = another_matrix,
            b = self,
            func_name = "multiply_2d_matrix",
            is_self_update = False,
            prefix_errmsg = "Matrix2dFloat32.__rmatmul__()"
        )
    
    # Usage: matrix_self @= another_matrix
    def __imatmul__(self, another_matrix: "Matrix2dFloat32") -> "Matrix2dFloat32":
        return Matrix2dFloat32._operation_between_2_matrices(
            a = self,
            b = another_matrix,
            func_name = "multiply_2d_matrix",
            is_self_update = True,
            prefix_errmsg = "Matrix2dFloat32.__imatmul__()"
        )


    # Usage: new_matrix = matrice + other
    def __add__(self, other: "Matrix2dFloat32") -> "Matrix2dFloat32":
        return Matrix2dFloat32.add(
            a = self,
            b = other,
            is_self_update = False,
            prefix_errmsg = "Matrix2dFloat32.__add__()"
        )

    # Usage: new_matrix = other + matrice
    def __radd__(self, other: "Matrix2dFloat32") -> "Matrix2dFloat32":
        return self.__add__(other)
    
    # Usage: matrix += other
    def __iadd__(self, other: "Matrix2dFloat32" | float) -> "Matrix2dFloat32":
        return Matrix2dFloat32.add(
            a = self,
            b = other,
            is_self_update = True,
            prefix_errmsg = "Matrix2dFloat32.__iadd__()"
        )


    # Usage: new_matrix = matrice - other
    def __sub__(self, other: "Matrix2dFloat32") -> "Matrix2dFloat32":
        if not isinstance(other, Matrix2dFloat32):
            raise ValueError("Matrix2dFloat32.__sub__(): The `-` operator only accepts Matrix2dFloat32 operands. For scalar subtraction, use `-=` (e.g. `matrix -= scalar`) or Matrix2dFloat32.sub(matrix, scalar) directly.")
        return Matrix2dFloat32.sub(
            a = self,
            b = other,
            is_self_update = False,
            prefix_errmsg = "Matrix2dFloat32.__sub__()"
        )
    
    # Usage: new_matrix = other - matrice
    def __rsub__(self, other: "Matrix2dFloat32") -> "Matrix2dFloat32":
        return Matrix2dFloat32.sub(
            a = other,
            b = self,
            is_self_update = False,
            prefix_errmsg = "Matrix2dFloat32.__rsub__()"
        )
    
    # Usage: matrix -= other
    def __isub__(self, other: "Matrix2dFloat32" | float) -> "Matrix2dFloat32":
        return Matrix2dFloat32.sub(
            a = self,
            b = other,
            is_self_update = True,
            prefix_errmsg = "Matrix2dFloat32.__isub__()"
        )
