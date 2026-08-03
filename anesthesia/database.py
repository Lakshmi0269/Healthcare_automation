import mysql.connector
import pandas as pd

def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="lachu"
    )

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS ANESTHESIA_DB")

    cursor.execute("USE ANESTHESIA_DB")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ANESTHESIA_CF (

            CONTRACTOR VARCHAR(20),
            LOCALITY VARCHAR(20),
            LOCALITY_NAME VARCHAR(100),
            WORK_GPCI DECIMAL(10,3),
            PE_GPCI DECIMAL(10,3),
            MP_GPCI DECIMAL(10,3),
            NON_Q_APM_CF DECIMAL(10,2),
            Q_APM_CF DECIMAL(10,2)

        )
    """)

    conn.commit()

    print("Database and Table Ready")

    cursor.close()

    return conn


def insert_data(conn, df):

    cursor = conn.cursor()

    cursor.execute("DELETE FROM ANESTHESIA_CF")

    sql = """
        INSERT INTO ANESTHESIA_CF
        (
            CONTRACTOR,
            LOCALITY,
            LOCALITY_NAME,
            WORK_GPCI,
            PE_GPCI,
            MP_GPCI,
            NON_Q_APM_CF,
            Q_APM_CF
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    records = []

    for _, row in df.iterrows():

        # Skip rows with missing Contractor
        if pd.isna(row["CONTRACTOR"]):
            continue

        records.append((
            str(row["CONTRACTOR"]).strip(),
            str(row["LOCALITY"]).strip(),
            str(row["LOCALITY_NAME"]).strip(),
            float(row["WORK_GPCI"]),
            float(row["PE_GPCI"]),
            float(row["MP_GPCI"]),
            float(row["NON_Q_APM_CF"]),
            float(row["Q_APM_CF"])
        ))

    cursor.executemany(sql, records)

    conn.commit()

    print(f"{cursor.rowcount} Records Inserted Successfully")

    cursor.close()