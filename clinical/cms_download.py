import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():

    download_folder = os.path.abspath("downloads")

    os.makedirs(download_folder, exist_ok=True)

    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    return driver


# -----------------------------
# Clinical HCPCS Download
# -----------------------------
def download_clfs():

    driver = get_driver()

    driver.get(
        "https://www.cms.gov/medicare/payment/fee-schedules/clinical-laboratory-fee-schedule-clfs/files/26clabq3"
    )

    print("Clinical CMS page opened")

    wait = WebDriverWait(driver, 20)

    file_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "26CLABQ3"))
    )

    file_link.click()

    print("Clicked 26CLABQ3")

    accept_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//input[@value='Accept'] | //button[contains(., 'Accept')]"
            )
        )
    )

    accept_button.click()

    print("Clinical file download started")

    time.sleep(10)

    driver.quit()

    print("Clinical file downloaded successfully")


# -----------------------------
# Physician Fee Schedule Download
# -----------------------------
def download_physician():

    driver = get_driver()

    driver.get(
        "https://www.cms.gov/medicare/payment/fee-schedules/physician/national-payment-amount-file/pfrev26c"
    )

    print("Physician CMS page opened")

    wait = WebDriverWait(driver, 20)

    file_link = wait.until(
        EC.element_to_be_clickable(
            (By.PARTIAL_LINK_TEXT, "PFREV26C")
        )
    )

    file_link.click()

    print("Clicked PFREV26C")

    # Give Chrome time to finish downloading
    time.sleep(10)

    driver.quit()

    print("Physician file downloaded successfully")