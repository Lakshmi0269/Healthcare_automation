from .cleanup import clean_folders
from .cms_download import download_clfs, download_physician
from .zip_extractor import extract_all_zip_files
from .data_processing import read_data, read_physician_data
from .database import connect_db, insert_data, update_physician_data


def run_clinical():

    clean_folders()

    print("HCPCS Automation Started")

    # Connect to MySQL
    connection = connect_db()

    # =====================================================
    # Clinical HCPCS File
    # =====================================================

    print("\nDownloading Clinical HCPCS File...")
    download_clfs()

    print("\nExtracting Clinical ZIP...")
    extract_all_zip_files()

    print("\nReading Clinical File...")
    clinical_data = read_data()

    print("\nInserting Clinical Data...")
    insert_data(connection, clinical_data)

    # =====================================================
    # Physician Fee Schedule File
    # =====================================================

    print("\nDownloading Physician File...")
    download_physician()

    print("\nExtracting Physician ZIP...")
    extract_all_zip_files()

    print("\nReading Physician File...")
    physician_data = read_physician_data()

    print("\nUpdating HCPCS Table...")
    update_physician_data(connection, physician_data)

    # Close Connection
    connection.close()

    print("\nAutomation Completed Successfully!")


if __name__ == "__main__":
    run_clinical()