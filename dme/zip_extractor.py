import os
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "downloads")
EXTRACT_FOLDER = os.path.join(BASE_DIR, "extracted")


def extract_all_zip_files():

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    os.makedirs(EXTRACT_FOLDER, exist_ok=True)

    print(f"DOWNLOAD_FOLDER: {DOWNLOAD_FOLDER}")
    print(f"EXTRACT_FOLDER: {EXTRACT_FOLDER}")

    files = os.listdir(DOWNLOAD_FOLDER)
    print(f"Files in downloads folder: {files}")

    zip_files = [
        file for file in files
        if file.lower().endswith(".zip")
    ]

    print(f"ZIP files found: {zip_files}")

    if not zip_files:
        print("No ZIP files found.")
        return

    for zip_name in zip_files:

        zip_path = os.path.join(DOWNLOAD_FOLDER, zip_name)

        print(f"Extracting {zip_name}...")

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(EXTRACT_FOLDER)

        print(f"{zip_name} extracted successfully.")

    print("\nAll ZIP files extracted successfully.")