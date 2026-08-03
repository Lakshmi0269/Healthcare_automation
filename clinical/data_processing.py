import os
import pandas as pd


def read_data():

    extract_folder = "extracted_files"

    clinical_file = None

    # Search Clinical HCPCS file recursively
    for root, dirs, files in os.walk(extract_folder):

        for file in files:

            if file.upper().startswith("PUF_CLFS") and file.upper().endswith(".TXT"):

                clinical_file = os.path.join(root, file)
                break

        if clinical_file:
            break

    if clinical_file is None:
        print("Clinical file not found.")
        return pd.DataFrame()

    print(f"Reading: {os.path.basename(clinical_file)}")

    df = pd.read_csv(
        clinical_file,
        sep="~",
        skiprows=7,
        engine="python",
        dtype=str,
        on_bad_lines="skip"
    )

    df.columns = [
        "YEAR",
        "HCPCS",
        "MOD",
        "EFF_DATE",
        "INDICATOR",
        "RATE",
        "SHORTDESC"
    ]

    return df


def read_physician_data():

    extract_folder = "extracted_files"

    physician_file = None

    # Search Physician file recursively
    for root, dirs, files in os.walk(extract_folder):

        for file in files:

            if file.upper() == "PFREV26C.TXT":

                physician_file = os.path.join(root, file)
                break

        if physician_file:
            break

    if physician_file is None:
        print("Physician file not found.")
        return pd.DataFrame()

    print(f"Reading: {os.path.basename(physician_file)}")

    with open(physician_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Ignore last 4 footer lines
    lines = lines[:-4]

    physician_data = []

    for line in lines:

        row = [x.strip().replace('"', '') for x in line.strip().split(",")]

        if len(row) < 10:
            continue

        physician_data.append({
            "YEAR": row[0],
            "HCPCS": row[1],
            "RATE": row[5],          # 6th column
            "INDICATOR": row[9]      # 10th column
        })

    df = pd.DataFrame(physician_data)

    return df