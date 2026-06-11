import sqlite3

from backend.config import DATABASE_PATH


class DatabaseManager:

    def __init__(self):
        self.db_path = DATABASE_PATH

    def insert_reading(self, bin_id, distance, fill_percentage, status, alert):

        connection = sqlite3.connect(self.db_path)

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO waste_readings
            (
                bin_id,
                distance,
                fill_percentage,
                status,
                alert
            )
            VALUES
            (?, ?, ?, ?, ?)
            """,
            (bin_id, distance, fill_percentage, status, int(alert)),
        )

        connection.commit()

        connection.close()
