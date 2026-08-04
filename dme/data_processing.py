import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXTRACT_FOLDER = os.path.join(BASE_DIR, "extracted")


def read_data():

    txt_files = [
        f for f in os.listdir(EXTRACT_FOLDER)
        if f.lower().endswith(".txt")
    ]

    if not txt_files:
        print("No TXT file found.")
        return pd.DataFrame()

    file_path = os.path.join(EXTRACT_FOLDER, txt_files[0])

    print(f"Reading: {txt_files[0]}")

    df = pd.read_csv(
        file_path,
        sep="\t",
        dtype=str
    )

    df.columns = [
        "STATE",
        "ZIP_CODE",
        "YEAR_QTR"
    ]

    return df