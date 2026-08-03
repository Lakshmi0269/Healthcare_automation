import mysql.connector


def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="lachu"
    )

    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS HCPCS_DB")

    # Select the database
    cursor.execute("USE HCPCS_DB")

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS HCPCS (
            YEAR INT,
            HCPCS VARCHAR(10),
            EFF_DATE DATE,
            INDICATOR CHAR(1),
            RATE DECIMAL(10,2)
        )
    """)

    conn.commit()

    print("Database and Table Ready")

    cursor.close()

    return conn


def insert_data(conn, df):

    cursor = conn.cursor()

    # Delete old records
    cursor.execute("DELETE FROM HCPCS")

    sql = """
        INSERT INTO HCPCS
        (YEAR, HCPCS, EFF_DATE, INDICATOR, RATE)
        VALUES (%s, %s, %s, %s, %s)
    """

    records = []

    for _, row in df.iterrows():

        # Convert date from YYYYMMDD to YYYY-MM-DD
        eff_date = (
            row["EFF_DATE"][:4] + "-" +
            row["EFF_DATE"][4:6] + "-" +
            row["EFF_DATE"][6:]
        )

        records.append((
            int(row["YEAR"]),
            row["HCPCS"],
            eff_date,
            row["INDICATOR"],
            float(row["RATE"])
        ))

    cursor.executemany(sql, records)

    conn.commit()

    print(f"{cursor.rowcount} Records Inserted Successfully")

    cursor.close()


def update_physician_data(conn, df):

    cursor = conn.cursor()

    sql = """
        INSERT INTO HCPCS
        (
            YEAR,
            HCPCS,
            EFF_DATE,
            INDICATOR,
            RATE
        )
        VALUES (%s, %s, NULL, %s, %s)
    """

    records = []

    for _, row in df.iterrows():

        try:
            records.append((
                int(str(row["YEAR"]).strip()),
                str(row["HCPCS"]).strip(),
                str(row["INDICATOR"]).strip(),
                float(str(row["RATE"]).replace(",", "").strip())
            ))
        except Exception:
            continue

    cursor.executemany(sql, records)

    conn.commit()

    print(f"{cursor.rowcount} Physician Records Inserted Successfully")

    cursor.close()