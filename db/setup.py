from .connection import get_connection
import sqlite3

def create():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       game_name TEXT,
                       number_of_players INTEGER
                       );
    """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipment(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       equipment_name TEXT,
                       game_id INTEGER);
    """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       player_name TEXT,
                       year_of_birth INTEGER,
                       gender TEXT,
                       game_id INTEGER);
    """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS coaches(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       coach_name TEXT,
                       year_of_birth INTEGER,
                       gender TEXT,
                       game_id INTEGER
                       );
""")
        conn.commit()   
    except sqlite3.Error as error:
        print(error)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()