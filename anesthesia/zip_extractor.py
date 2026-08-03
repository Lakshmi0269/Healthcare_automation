import os
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "downloads")
EXTRACT_FOLDER = os.path.join(BASE_DIR, "extracted")


def extract_all_zip_files():

    os.makedirs(EXTRACT_FOLDER, exist_ok=True)

    # Extract downloaded ZIP files
    zip_files = [
        file for file in os.listdir(DOWNLOAD_FOLDER)
        if file.lower().endswith(".zip")
    ]

    if not zip_files:
        print("No ZIP files found.")
        return

    for zip_name in zip_files:

        zip_path = os.path.join(DOWNLOAD_FOLDER, zip_name)

        print(f"Extracting {zip_name}...")

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(EXTRACT_FOLDER)

        print(f"{zip_name} extracted successfully.")

    # Look for nested ZIP files (__MACOSX.zip or any other ZIP)
    for root, dirs, files in os.walk(EXTRACT_FOLDER):

        for file in files:

            if file.lower().endswith(".zip"):

                nested_zip = os.path.join(root, file)

                print(f"Extracting nested ZIP: {file}...")

                with zipfile.ZipFile(nested_zip, "r") as zip_ref:
                    zip_ref.extractall(root)

                print(f"{file} extracted successfully.")

    print("\nAll ZIP files extracted successfully.")