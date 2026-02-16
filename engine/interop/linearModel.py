# import ctypes
# from engine.interop.loader import Loader
# from engine.interop.array import ArrayFloat32Ptr

# class LinearModel:
    
#     def __init__(self, coef_list: list[float | int], feature_list: list[float | int], intercept = 0.0):
#         self._set_linear_model(coef_list, feature_list, intercept)    

#     def __str__(self):
#         return f"LinearModel(coef={self.coef_list}, constant={self.feature_list})"
    

#     #====== Properties ======#

#     def _get_coef_list(self):
#         return self._coef_list.array
    
#     def _set_coef_list(self, data: list[float | int]):
#         self._coef_list = ArrayFloat32Ptr(data)
    
#     def _get_constant_list(self):
#         return self._constant_list.array

#     def _set_constant_list(self, data: list[float | int]):
#         self._constant_list = ArrayFloat32Ptr(data)

#     def _get_linear_model(self):
#         return (self.coef_list, self.feature_list)

#     def _set_linear_model(self, coef_list: list[float | int], feature_list: list[float | int]):
#         if len(coef_list) != len(feature_list):
#             raise ValueError("LinearModel.__init__(): `coef_list` and `feature_list` must have the same length")
#         self._set_coef_list(coef_list)
#         self._set_constant_list(feature_list)

#     coef_list = property(_get_coef_list, _set_coef_list)
#     feature_list = property(_get_constant_list, _set_constant_list)
#     linear_model = property(_get_linear_model, _set_linear_model)
#     intercept = property(_get_constant_list, _set_constant_list)

#     #====== Pulbic ======#
#     def predict(self, input_vector: list[float | int]) -> float:
#         if len(input_vector) != len(self.coef_list):
#             raise ValueError("LinearModel.predict(): `input_vector` length must match number of coefficients")
        
#         result = 0.0
#         for coef, feature, input_val in zip(self.coef_list, self.feature_list, input_vector):
#             result += coef * input_val
#         return result