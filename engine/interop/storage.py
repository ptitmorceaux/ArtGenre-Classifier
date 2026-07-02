
import ctypes
from engine.interop.loader import Loader
from engine.interop.linearModel import LinearModel, _CLinearModel
from engine.interop.mlp import MLP, _CMLP
from engine.interop.normalization import StandardScaler, StandardPerColumnScaler

def load_model_and_normalization_from_binary_file(filepath: str) -> None | \
                                                                    tuple[LinearModel | MLP, StandardScaler | StandardPerColumnScaler]:
    """Load a LinearModel from a binary file."""
    model_type = ctypes.c_int()
    model_ptr = ctypes.c_void_p()

    normalization_type = ctypes.c_int()
    normalization_ptr = ctypes.c_void_p()

    Loader.call(
        "load_binary_file",
        filepath.encode('utf-8'),
        ctypes.byref(model_type),
        ctypes.byref(model_ptr),
        ctypes.byref(normalization_type),
        ctypes.byref(normalization_ptr),
        prefix_errmsg="LinearModel.init_from_binary_file()"
    )

    model_type = Loader.call(
        "get_model_type_string",
        model_type,
        prefix_errmsg="load_model_from_binary_file.get_model_type_string()"
    )

    if model_type.lower() == "linearModel":
        
        model_struct = ctypes.cast(
            model_ptr,
            ctypes.POINTER(_CLinearModel)
        ).contents

        model = LinearModel(model_struct.length.value)
        model.ptr = model_ptr
        
        return model
    
    elif model_type.lower() == "mlp":

        return MLP._init_from_model_ptr(model_ptr)

    return None


def get_model_type(model: LinearModel | MLP) -> str:
        """
        Renvoie le ModelType du modèle C.
        """
        if model.ptr is None or model.ptr.value is None:
            raise ValueError("LinearModel.get_model_type(): model is not initialized.")
        
        if isinstance(model, LinearModel):
            struct_model = ctypes.POINTER(_CLinearModel)
        
        elif isinstance(model, MLP):
            struct_model = ctypes.POINTER(_CMLP)

        model = ctypes.cast(
            model.ptr,
            struct_model
        ).contents

        return model.model_type

Storage = {
     "load": load_model_and_normalization_from_binary_file,
     "get_model_type": get_model_type
}