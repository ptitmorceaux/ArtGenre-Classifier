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

