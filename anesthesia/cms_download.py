import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


DOWNLOAD_FOLDER = os.path.abspath("downloads")


def download_anesthesia():

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": DOWNLOAD_FOLDER,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print("Opening CMS Anesthesia page...")

    driver.get(
        "https://www.cms.gov/anesthesiologists-information-center"
    )

    driver.maximize_window()

    time.sleep(5)

    print("Clicking 2026 Anesthesia Conversion Factors (ZIP)...")

    driver.find_element(
        By.PARTIAL_LINK_TEXT,
        "2026 Anesthesia Conversion Factors"
    ).click()

    print("Downloading Anesthesia ZIP file...")

    time.sleep(5)

    driver.quit()

    print("Anesthesia ZIP downloaded successfully.")