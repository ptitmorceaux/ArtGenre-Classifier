import os
import time
import requests
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ART_MOVEMENTS = {
    "surrealism": "https://www.wikiart.org/fr/paintings-by-style/surrealism-0#!#filterName:all-works,viewType:masonry",
    "cubism": "https://www.wikiart.org/fr/paintings-by-style/cubism#!#filterName:all-works,viewType:masonry",
    "early-renaissance": "https://www.wikiart.org/fr/paintings-by-style/early-renaissance#!#filterName:all-works,viewType:masonry"
}

DATASET_DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'dataset')

def setup_driver():
    """Configure et retourne un driver Selenium pour Chrome."""
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def download_image(url, folder_path, filename):
    """Fonction pour télécharger une image à partir d'une URL et la sauvegarder localement."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(os.path.join(folder_path, filename), 'wb') as f:
                f.write(response.content)
            return True
    except Exception:
        pass
    return False

def load_more_images(driver, max_clicks=3):
    """Fonction pour cliquer sur le bouton 'Charger plus' et charger plus d'images."""
    print("Début du chargement des images supplémentaires")
    for i in range(max_clicks):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        try:
            load_button = driver.find_element(
                By.XPATH,
                "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'charger plus') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'load more')]"
            )
            if load_button.is_displayed():
                driver.execute_script("arguments[0].click();", load_button)
                print(f"Click {i+1}/{max_clicks} sur Charger Plus effectué")
                time.sleep(3)
            else:
                break
        except Exception:
            print("Limite atteinte.")
            break


def close_popup(driver):
    """Fonction pour fermer les pop-ups de cookies ou autres qui pourraient bloquer le scraping."""
    print("Vérification des pop-ups...")
    try:
        wait = WebDriverWait(driver, 5)
        bouton_accept = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'agree') or contains(@class, 'close')]")))
        bouton_accept.click()
        print("Pop-up fermé avec succès !")
        time.sleep(1)
    except Exception:
        print("Aucun pop-up bloquant détecté.")

