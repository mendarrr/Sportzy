import sqlite3
DATABASE_NAME = "./sports.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn