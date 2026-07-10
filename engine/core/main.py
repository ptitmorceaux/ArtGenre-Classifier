# ruff: noqa
import os
import sys
import argparse
import tensorflow as tf

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import engine.core.config as cf
import engine.core.tb_logger as tb
from engine.core.build import compile_c_library, load_c_library
from engine.core.dataset import load_and_prepare_csv, load_images_from_filepaths
from engine.core.preprocessing import standardize_train_data, standardize_test_data_from_scaler
from engine.core.training import train_models
from engine.core.persistence import save_trained_models, save_config_json
from engine.core.evaluation import evaluate_models, plot_confusion_matrix


def parse_args() -> argparse.Namespace:
    default_json_path = os.path.join("engine", "core", "conf", "config.json")
    parser = argparse.ArgumentParser(description="Entraînement d'un classifieur de genre artistique.")
    parser.add_argument(
        "-j", "--json",
        dest="json_path",
        type=str,
        default=default_json_path,
        help=f"Chemin vers le fichier de configuration JSON (défaut: '{default_json_path}')",
    )
    return parser.parse_args()



def main():
    args = parse_args()

    # Chargement de la configuration depuis un fichier JSON si disponible
    cf.CONFIG = cf.load_config_from_json(args.json_path)

    # INFO
    print(f"\n# INFO :")
    print(f"[*] Start TensorBoard with: tensorboard --logdir={cf.CONFIG['output']['folder']} --port=6007")

    # 1. Gestion de l'aléa
    print(f"\n# Etape 1 : Seed sélectionnée : {cf.CONFIG['lib']['seed']}")

    # 2. Compilation et chargement de l'interopérabilité
    print("\n# Etape 2 : Compilation et chargement de l'interopérabilité...")
    compile_c_library()
    load_c_library()

    # 3. Préparation des données
    print("\n# Etape 3 : Préparation des données (chargement des images train uniquement)...")
    df_X_filepaths, df_Y = load_and_prepare_csv()
    df_X = { "train": load_images_from_filepaths(df_X_filepaths["train"], is_train=True) }
    cf.CONFIG = cf.finalize_mlp_config(cf.CONFIG)
    df_X, scaler = standardize_train_data(df_X)

    ### TENSORBOARD SUMMARY WRITER ###
    summary_writer = tf.summary.create_file_writer(cf.CONFIG["output"]["logs"])

    # 4. Entraînement
    print("\n# Etape 4 : Entraînement des modèles et enregistrement des logs pour tensorboard...")
    models_per_category = train_models(summary_writer, df_X, df_Y)

    # 5. Sauvegarde des modèles entraînés + du scaler utilisé (un fichier par catégorie).
    #    Les modèles restent en mémoire ensuite pour l'évaluation ci-dessous.
    print("\n# Etape 5 : Sauvegarde des modèles entraînés...")
    save_trained_models(models_per_category, scaler, cf.CONFIG["output"]["models"], cf.CONFIG["model"]["type"])

    # 6. Chargement des images de test et normalisation avec le scaler du train (on libère la mémoire des images du train).
    print("\n# Etape 6 : Chargement des images de test et normalisation...")
    del df_X  # Libère la mémoire des images du train
    df_X = { "test": load_images_from_filepaths(df_X_filepaths["test"], is_train=False) }
    df_X["test"] = standardize_test_data_from_scaler(df_X["test"], scaler)

    # 7. Évaluation et Visualisation
    print("\n# Etape 7 : Évaluation et Visualisation...")
    df_predictions_expected, df_predictions_test = evaluate_models(models_per_category, df_X, df_Y)
    
    # 8. Sauvegarde de la matrice de confusion test
    print("\n# Etape 8 : Sauvegarde de la matrice de confusion...")
    plot_confusion_matrix(df_predictions_expected, df_predictions_test, df_X, show=False)

    # 9. Sauvegarde de la configuration en json
    print("\n# Etape 9 : Sauvegarde de la configuration...")
    save_config_json(cf.CONFIG["output"]["logs"], cf.CONFIG)

    # 10. Écriture des résultats finaux dans TensorBoard
    print("\n# Etape 10 : Écriture des résultats finaux dans TensorBoard...\n")
    summary_writer = tf.summary.create_file_writer(cf.CONFIG["output"]["logs"])
    tb.write_markdown_from_dict(
        summary_writer,
        tb.get_summary_md_dict()
    )
    tb.write_images(summary_writer)

    ### TENSORBOARD SUMMARY WRITER CLOSE ###
    summary_writer.close()


if __name__ == "__main__":
    main()