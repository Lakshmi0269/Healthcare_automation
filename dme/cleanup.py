import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def clean_folders():

    folders = [
        os.path.join(BASE_DIR, "downloads"),
        os.path.join(BASE_DIR, "extracted"),
    ]

    for folder in folders:

        if os.path.exists(folder):

            try:
                shutil.rmtree(folder)

            except PermissionError:

                print(f"Skipping locked file/folder: {folder}")

        os.makedirs(folder, exist_ok=True)

    print("Downloads and Extracted folders cleaned.")