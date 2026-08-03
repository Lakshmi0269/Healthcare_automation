from .cleanup import clean_folders
from .cms_download import download_dme
from .zip_extractor import extract_all_zip_files
from .data_processing import read_data
from .database import connect_db, insert_data


def run_dme():

    # Clean old folders
    clean_folders()

    print("DME Automation Started")

    conn = connect_db()

    print("\nDownloading DME File...")
    download_dme()

    print("\nExtracting ZIP...")
    extract_all_zip_files()

    print("\nReading File...")
    df = read_data()

    print("\nInserting Data...")
    insert_data(conn, df)

    conn.close()

    print("\nDME Automation Completed Successfully")


if __name__ == "__main__":
    run_dme()