import os
import shutil

def clean_folders():

    folders = ["downloads", "extracted_files"]

    for folder in folders:

        if os.path.exists(folder):

            for item in os.listdir(folder):

                item_path = os.path.join(folder, item)

                try:
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    else:
                        shutil.rmtree(item_path)

                except PermissionError:
                    print(f"Skipping locked file/folder: {item_path}")

        else:
            os.makedirs(folder)

    print("Downloads and Extracted folders cleaned.")