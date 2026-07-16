import os
from pathlib import Path
from PIL import Image
import concurrent.futures

# Si le script est dans ArtGenre-Classifier/dataset/script/
# SCRIPT_DIR pointe vers le dossier "script"
SCRIPT_DIR = Path(__file__).resolve().parent

# DATASET_DIR pointe vers le dossier parent "dataset"
DATASET_DIR = SCRIPT_DIR.parent 

INPUT_DIR = os.path.join(DATASET_DIR, "images", "64x64")
OUTPUT_DIR = os.path.join(DATASET_DIR, "images", "32x32_gray")

GENRES = ["impressionism", "realism", "romanticism"]
TARGET_SIZE = (32, 32)

def process_single_image(input_path, output_path):
    """Ouvre une image, la convertit en niveaux de gris (L), la redimensionne et la sauvegarde."""
    try:
        with Image.open(input_path) as img:
            # 1. 'L' pour Luminance (1 seul canal)
            # 2. resize avec LANCZOS pour éviter la perte de qualité lors de la réduction
            processed_img = img.convert('L').resize(TARGET_SIZE, getattr(Image, "Resampling", Image).LANCZOS)
            processed_img.save(output_path)
        return True
    except Exception as e:
        return f"Erreur sur {input_path.name} : {e}"

def main():
    print(f"[*] Dossier source : {INPUT_DIR}")
    print(f"[*] Dossier cible  : {OUTPUT_DIR}\n")

    # Création de l'arborescence de sortie si elle n'existe pas
    for genre in GENRES:
        os.makedirs(os.path.join(OUTPUT_DIR, genre), exist_ok=True)

    tasks = []
    # Parallélisation pour traiter les ~43 000 images très rapidement
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for genre in GENRES:
            genre_dir = os.path.join(INPUT_DIR, genre)
            if not os.path.exists(genre_dir):
                print(f"[!] Dossier introuvable : {genre_dir}")
                continue

            image_files = list(Path(genre_dir).glob("*.*"))
            print(f"[*] Lancement de la conversion pour '{genre}' ({len(image_files)} images)...")

            for img_path in image_files:
                out_path = os.path.join(OUTPUT_DIR, genre, img_path.name)
                tasks.append(executor.submit(process_single_image, img_path, out_path))

        # Suivi de la progression
        total_tasks = len(tasks)
        completed = 0
        for future in concurrent.futures.as_completed(tasks):
            result = future.result()
            if result is not True:
                print(result) # Affiche les erreurs s'il y en a
            
            completed += 1
            if completed % 1000 == 0 or completed == total_tasks:
                print(f"\r[>] Progression : {completed} / {total_tasks} ({(completed/total_tasks)*100:.1f}%)", end="")
                
    print("\n\n[*] Conversion terminée avec succès ! Le nouveau dataset 32x32_gray est prêt.")

if __name__ == "__main__":
    main()