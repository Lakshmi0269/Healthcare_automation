from .cleanup import clean_folders
from .cms_download import download_anesthesia
from .zip_extractor import extract_all_zip_files
from .data_processing import read_data
from .database import connect_db, insert_data


def run_anesthesia():

    print("Anesthesia Automation Started")

    clean_folders()

    conn = connect_db()

    print("\nDownloading Anesthesia File...")
    download_anesthesia()

    print("\nExtracting ZIP Files...")
    extract_all_zip_files()

    print("\nReading File...")
    df = read_data()

    print("\nInserting Data...")
    insert_data(conn, df)

    conn.close()

    print("\nAnesthesia Automation Completed Successfully")


if __name__ == "__main__":
    run_anesthesia()