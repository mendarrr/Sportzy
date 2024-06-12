from .connection import get_connection
import sqlite3

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games(
                       id INTEGER,
                       game_name TEXT PRIMARY KEY,
                       number_of_players INTEGER,
                       coach_name TEXT,
                       FOREIGN KEY(coach_name) REFERENCES coach(coach_name),
                       );
    """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipment(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       equipment_name TEXT,
                       game_name TEXT,
                       FOREIGN KEY(game_name) REFERENCES games(game_name)
                       );
    """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS players(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       player_name TEXT,
                       year_of_birth INTEGER,
                       gender TEXT,
                       game_name TEXT,
                       FOREIGN KEY(game_name) REFERENCES games(game_name),
                       );
    """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS coaches(
                       id INTEGER,
                       coach_name TEXT PRIMARY KEY,
                       year_of_birth INTEGER,
                       gender TEXT,
                       game_name TEXT,
                       FOREIGN KEY(game_name) REFERENCES games(game_name),
                       );
""")
        conn.commit()   
    except sqlite3.Error as error:
        print(error)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()