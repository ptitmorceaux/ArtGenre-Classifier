import os
import time
import requests
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

TARGET_IMAGES = 2500

ART_MOVEMENTS = {
    "surrealism": "https://www.wikiart.org/fr/paintings-by-style/surrealism-0#!#filterName:all-works,viewType:masonry",
    "cubism": "https://www.wikiart.org/fr/paintings-by-style/cubism#!#filterName:all-works,viewType:masonry",
    "late-renaissance": "https://www.wikiart.org/fr/paintings-by-style/mannerism-late-renaissance?select=featured#!#filterName:featured,viewType:masonry"
}

DATASET_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'dataset')

def setup_driver():
    """Configure et retourne un driver Selenium pour Chrome."""
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)

def download_image(url, folder_path, filename):
    """Télécharge une image depuis une URL et la sauvegarde dans le dossier spécifié."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            with open(os.path.join(folder_path, filename), 'wb') as f:
                f.write(response.content)
            return True
    except Exception:
        pass
    return False

def close_popup(driver):
    """Ferme le pop-up des cookies s'il y en a un."""
    try:
        wait = WebDriverWait(driver, 5)
        bouton_accept = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'agree') or contains(@class, 'close')]")))
        bouton_accept.click()
        time.sleep(1)
    except Exception:
        pass

def run_scraper():
    """Fonction principale qui orchestre le scraping pour tous les mouvements artistiques."""
    driver = setup_driver()
    
    for movement, url in ART_MOVEMENTS.items():
        print("\n" + "="*50)
        print(f"Démarrage pour: {movement.upper()}")
        print("="*50)

        movement_dir = os.path.join(DATASET_DIRECTORY, movement)
        os.makedirs(movement_dir, exist_ok=True)
        csv_file = os.path.join(movement_dir, "metadata.csv")
        
        driver.get(url)
        time.sleep(3)
        close_popup(driver)
        
        # ---------------------------------------------------------
        # PHASE 1 : SCROLL ET RÉCOLTE DES LIENS
        # ---------------------------------------------------------
        
        print(f"\nPHASE 1: Récolte des liens (Objectif : {TARGET_IMAGES} images)")
        liens_recoltes = {}
        
        # Check si on a terminer la page 
        scrolls_sans_nouvelle_image = 0
        MAX_SCROLLS_VIDES = 15 
        
        while len(liens_recoltes) < TARGET_IMAGES:
            nb_avant = len(liens_recoltes)
            
            # On lit les images affichées à cet instant précis
            images = driver.find_elements(By.TAG_NAME, "img")
            for img_tag in images:
                if len(liens_recoltes) >= TARGET_IMAGES:
                    break # On stoppe l'extraction si on atteint 2500 pendant la boucle
                    
                try:
                    raw_img_url = img_tag.get_attribute("src")
                    if not raw_img_url or "data:image" in raw_img_url:
                        raw_img_url = img_tag.get_attribute("lazy-src") or img_tag.get_attribute("data-src")
                  
                    if not raw_img_url:
                        continue
                        
                    image_url = raw_img_url.split('!')[0]
                
                    if image_url in liens_recoltes:
                        continue
                        
                    full_title = img_tag.get_attribute("title") or img_tag.get_attribute("alt")
                    
                    if not full_title or "-" not in full_title:
                        continue

                    parts = full_title.split("-", 1)
                    liens_recoltes[image_url] = {
                        "titre": parts[0].strip(),
                        "artiste": parts[1].strip()
                    }
                except Exception:
                    continue
            
            # Affichage de la progression sur la même ligne (le \r permet de remplacer la ligne précédente)
            print(f"\rProgression : {len(liens_recoltes)} / {TARGET_IMAGES} liens trouvés...", end="")
            
            # Scroll pour charger plus d'images (on continue d'avancer petit à petit)
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(1)
            
            # Verifier si il faut "Charger plus"
            try:
                load_button = driver.find_element(
                    By.XPATH,
                    "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'charger plus') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'load more')]"
                )
                if load_button.is_displayed():
                    driver.execute_script("arguments[0].click();", load_button)
                    time.sleep(2)
            except Exception:
                pass

            # Vérification de la sécurité anti-boucle
            if len(liens_recoltes) == nb_avant:
                scrolls_sans_nouvelle_image += 1
            else:
                scrolls_sans_nouvelle_image = 0
                
            if scrolls_sans_nouvelle_image >= MAX_SCROLLS_VIDES:
                print(f"\nFin de la galerie atteinte. Impossible de trouver {TARGET_IMAGES} images (blocage à {len(liens_recoltes)}).")
                break

        print(f"\nPhase 1 terminée ! {len(liens_recoltes)} liens trouvés au total.")
        
        # ---------------------------------------------------------
        # PHASE 2 : TÉLÉCHARGEMENT
        # ---------------------------------------------------------

        print("\nPHASE 2: Début du téléchargement")
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Nom_Fichier", "Titre", "Artiste"])
            writer.writeheader()
            
            image_counter = 0
            
            for img_url, metadata in liens_recoltes.items():
                filename = f"{movement}_{image_counter:04d}.jpg"
                
                if download_image(img_url, movement_dir, filename):
                    writer.writerow({
                        "Nom_Fichier": filename,
                        "Titre": metadata["titre"],
                        "Artiste": metadata["artiste"]
                    })
                    image_counter += 1
                    # Affiche le téléchargement tous les 50 fichiers pour ne pas spammer la console
                    if image_counter % 50 == 0 or image_counter == len(liens_recoltes):
                        print(f"{image_counter}/{len(liens_recoltes)} téléchargées...")

        print(f"Terminé pour {movement}! {image_counter} images ajoutées physiquement.")
        
    driver.quit()
    print("\nScraping global de masse terminé !")

if __name__ == "__main__":
    run_scraper()
