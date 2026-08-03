import os
import pandas as pd


def read_data():

    extract_folder = "extracted"

    txt_files = [
        f for f in os.listdir(extract_folder)
        if f.lower().endswith(".txt")
    ]

    if not txt_files:
        print("No TXT file found.")
        return pd.DataFrame()

    file_path = os.path.join(extract_folder, txt_files[0])

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