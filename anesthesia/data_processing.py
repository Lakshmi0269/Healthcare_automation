import os
import pandas as pd


def read_data():

    extract_folder = "extracted"

    csv_files = [
        f for f in os.listdir(extract_folder)
        if f.lower().endswith(".csv")
        and not f.startswith("._")
    ]

    if not csv_files:
        print("No CSV file found.")
        return pd.DataFrame()

    file_path = os.path.join(extract_folder, csv_files[0])

    print(f"Reading: {csv_files[0]}")

    df = pd.read_csv(
        file_path,
        skiprows=4,
        dtype=str
    )

    df.columns = [
        "CONTRACTOR",
        "LOCALITY",
        "LOCALITY_NAME",
        "WORK_GPCI",
        "PE_GPCI",
        "MP_GPCI",
        "NON_Q_APM_CF",
        "Q_APM_CF"
    ]

    return df