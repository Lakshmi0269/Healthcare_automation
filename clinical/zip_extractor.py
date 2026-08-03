import os
import zipfile

DOWNLOAD_FOLDER = "downloads"
EXTRACT_FOLDER = "extracted_files"


def extract_all_zip_files():

    os.makedirs(EXTRACT_FOLDER, exist_ok=True)

    # -------- First extraction --------
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

    # -------- Second extraction (PFREV26C_QP.zip) --------
    for root, dirs, files in os.walk(EXTRACT_FOLDER):

        for file in files:

            if file.upper() == "PFREV26C_QP.ZIP":

                qp_zip = os.path.join(root, file)

                print(f"Extracting {file}...")

                with zipfile.ZipFile(qp_zip, "r") as zip_ref:
                    zip_ref.extractall(root)

                print(f"{file} extracted successfully.")

    print("\nAll ZIP files extracted successfully.")