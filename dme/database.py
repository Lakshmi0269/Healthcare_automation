import mysql.connector


def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="lachu"
    )

    cursor = conn.cursor()

    # Create Database
    cursor.execute("CREATE DATABASE IF NOT EXISTS DME_DB")

    # Use Database
    cursor.execute("USE DME_DB")

    # Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DME_RURAL_ZIP (
            STATE VARCHAR(5),
            ZIP_CODE VARCHAR(10),
            YEAR_QTR INT
        )
    """)

    conn.commit()

    print("Database and Table Ready")

    cursor.close()

    return conn


def insert_data(conn, df):

    cursor = conn.cursor()

    # Delete old records
    cursor.execute("DELETE FROM DME_RURAL_ZIP")

    sql = """
        INSERT INTO DME_RURAL_ZIP
        (STATE, ZIP_CODE, YEAR_QTR)
        VALUES (%s, %s, %s)
    """

    records = []

    for _, row in df.iterrows():

        records.append((
            row["STATE"],
            row["ZIP_CODE"],
            int(row["YEAR_QTR"])
        ))

    cursor.executemany(sql, records)

    conn.commit()

    print(f"{cursor.rowcount} Records Inserted Successfully")

    cursor.close()