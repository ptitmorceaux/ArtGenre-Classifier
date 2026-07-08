import engine.core.config as cf
from engine.interop.normalization import (
    StandardScaler,
    StandardPerColumnScaler,
    fit_and_normalize_by_columns,
)


def standard_scaler(df_X: dict) -> tuple[dict, StandardScaler]:
    """
    Standardisation GLOBALE : (X - moyenne) / ecart_type, une seule paire mean/std
    pour tout le dataset. FIT sur le train uniquement, TRANSFORM sur train + test.
    """
    scaler = StandardScaler.from_data(df_X["train"])

    df_X["train"] = scaler.transform(df_X["train"])

    for i, X_test in enumerate(df_X["test"]):
        # Pas de `[X_test]` ici : ça emballerait l'image dans une liste supplémentaire
        # et casserait predict() (mauvaise longueur détectée).
        df_X["test"][i] = scaler.transform(X_test)

    return df_X, scaler


def standard_column_scaler(df_X: dict) -> tuple[dict, StandardPerColumnScaler]:
    """
    Standardisation PAR CANAL (r, g, b) : chaque canal a sa propre moyenne/écart-type.
    FIT sur le train uniquement (jamais sur le test, pour éviter la fuite de données),
    puis TRANSFORM sur train + test avec ces mêmes stats.
    """
    # FIT + TRANSFORM du train en une passe : mean/std calculés PAR CANAL,
    # puis appliqués immédiatement au train (reshape (-1, 3) -> normalise -> reflatten).
    train_normalized, means, stds = fit_and_normalize_by_columns(df_X["train"], n_columns=3)

    scaler = StandardPerColumnScaler(mean=means, std=stds)
    df_X["train"] = train_normalized

    # TRANSFORM du test avec les stats du train (jamais recalculées sur le test).
    for i, X_test in enumerate(df_X["test"]):
        df_X["test"][i] = scaler.transform(X_test)

    return df_X, scaler


def standardize_data(df_X: dict) -> tuple[dict, StandardScaler | StandardPerColumnScaler]:
    """Dispatch vers la méthode de normalisation choisie dans cf.CONFIG."""
    method = cf.CONFIG["dataset"]["normalization_method"]

    if method == "standard":
        return standard_scaler(df_X)
    elif method == "per_column":
        return standard_column_scaler(df_X)
    else:
        raise ValueError(f"standardize_data(): unknown normalization_method '{method}'.")