
import ctypes
import os
from engine.interop.loader import Loader
from engine.interop.linearModel import LinearModel, _CLinearModel
from engine.interop.mlp import MLP, _CMLP
from engine.interop.normalization import StandardScaler, _CStandardScaler, StandardPerColumnScaler, _CStandardPerColumnScaler


def _init_normalization_from_ptr(normalization_ptr: ctypes.c_void_p, normalization_type: str) -> StandardScaler | StandardPerColumnScaler:
    """Initialize a normalization object from a pointer."""
    match normalization_type.upper():
        
        case "STANDARD":
            return StandardScaler._init_from_normalization_ptr(normalization_ptr)
        
        case "STANDARD_PER_COLUMN":
            return StandardPerColumnScaler._init_from_normalization_ptr(normalization_ptr)
        
        case _:
            raise ValueError(f"init_normalization_from_ptr(): unknown normalization type '{normalization_type}'.")


def _init_model_from_ptr(model_ptr: ctypes.c_void_p, model_type: str) -> LinearModel | MLP:
    """Initialize a model object from a pointer."""
    match model_type.upper():
        
        case "LINEARMODEL":
            return LinearModel._init_from_model_ptr(model_ptr)
        
        case "MLP":
            return MLP._init_from_model_ptr(model_ptr)
        
        case _:
            raise ValueError(f"init_model_from_ptr(): unknown model type '{model_type}'.")


def load_model_and_normalization_from_binary_file(filepath: str) -> None | tuple[LinearModel | MLP, StandardScaler | StandardPerColumnScaler]:
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

    normalization_type = Loader.call(
        "get_normalization_type_string",
        normalization_type,
        prefix_errmsg="load_model_from_binary_file.get_normalization_type_string()"
    )

    model = _init_model_from_ptr(model_ptr, model_type)
    normalization = _init_normalization_from_ptr(normalization_ptr, normalization_type)

    return model, normalization


def _get_normalization_type(normalization: StandardScaler | StandardPerColumnScaler) -> str:
    """
    Renvoie le NormalizationMethod de la normalisation C.
    """
    if normalization.ptr is None or normalization.ptr.value is None:
        raise ValueError("StandardScaler.get_normalization_type(): normalization is not initialized.")
    
    if isinstance(normalization, StandardScaler):
        struct_normalization = ctypes.POINTER(_CStandardScaler)
    
    elif isinstance(normalization, StandardPerColumnScaler):
        struct_normalization = ctypes.POINTER(_CStandardPerColumnScaler)

    normalization = ctypes.cast(
        normalization.ptr,
        struct_normalization
    ).contents

    return normalization.method

def _get_model_type(model: LinearModel | MLP) -> ctypes.c_int:
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


def save_model_and_normalization_to_binary_file(
        model: LinearModel | MLP,
        normalization: StandardScaler | StandardPerColumnScaler,
        output_folder: str, filename: str | None
    ) -> None:
    """
    Save a LinearModel and its normalization to a binary file.
    """
    if model.ptr is None or model.ptr.value is None:
        raise ValueError("LinearModel.save_to_binary_file(): model is not initialized.")
    
    if normalization.ptr is None or normalization.ptr.value is None:
        raise ValueError("StandardScaler.save_to_binary_file(): normalization is not initialized.")
    
    os.makedirs(output_folder, exist_ok=True)
    
    if filename is not None:
        filepath = os.path.join(output_folder, filename)
        if os.path.isfile(filepath):
            raise ValueError(f"LinearModel.save_to_binary_file(): file '{filepath}' already exists.")

    normalization_type = _get_normalization_type(normalization)
    model_type = _get_model_type(model)

    Loader.call(
        "save_binary_file",
        output_folder.encode('utf-8'),
        filename.encode('utf-8') if filename is not None else None,
        normalization_type,
        normalization.ptr,
        model_type,
        model.ptr,
        prefix_errmsg="LinearModel.save_to_binary_file()"
    )


Storage = {
    "load": load_model_and_normalization_from_binary_file,
    "save": save_model_and_normalization_to_binary_file
}