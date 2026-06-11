import sqlite3
import pandas as pd

DB_PATH = "database/waste_management.db"


def load_data():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT *
    FROM waste_readings
    ORDER BY id DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df
