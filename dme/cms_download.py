import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


DOWNLOAD_FOLDER = os.path.abspath("downloads")


def download_dme():

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

    print("Opening CMS DME page...")

    driver.get(
        "https://www.cms.gov/medicare/payment/fee-schedules/dmepos/dmepos-fee-schedule/dme26"
    )

    driver.maximize_window()

    time.sleep(5)

    print("Clicking DME26-A...")

    driver.find_element(
        By.PARTIAL_LINK_TEXT,
        "DME26-A"
    ).click()

    print("Downloading DME ZIP file...")

    time.sleep(3)

    driver.quit()

    print("DME ZIP downloaded successfully.")