import os
import csv
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


MOUVEMENTS = {
    "suréalisme": "https://www.wikiart.org/fr/paintings-by-style/surrealisme",
    "cubisme": "https://www.wikiart.org/fr/paintings-by-style/cubisme",
    "early renaissance": "https://www.wikiart.org/fr/paintings-by-style/early-renaissance"
}

DATASET_DIR = os.path.join(os.path.dirname(__file__), '..', 'dataset')


def setup_driver():
    """Configure et retourne un driver Selenium pour Chrome."""
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def download_image(url, folder_path, filename):
    """Fonction pour télécharger une image à partir d'une URL et la sauvegarder localement."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            save_path = os.path.join(folder_path, filename)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"Exception lors du téléchargement de l'image : {e}")
    return False