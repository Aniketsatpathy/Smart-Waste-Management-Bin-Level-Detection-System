import sqlite3

DB_NAME = "database/waste_management.db"

connection = sqlite3.connect(DB_NAME)

cursor = connection.cursor()

with open("database/schema.sql", "r") as file:
    schema = file.read()

cursor.executescript(schema)

connection.commit()
connection.close()

print("Database Created Successfully")
