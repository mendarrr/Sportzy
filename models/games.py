from db.connection import get_connection
import sqlite3

class Game:
    def __init__(self, id, game_name, number_of_players, coach_id, coach_name):
        self.id = id
        self.game_name = game_name
        self.number_of_players = number_of_players
        self.coach_name = coach_name
        self.coach_id = coach_id

    def __repr__(self):
        pass

    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id(self, player_id):
        self._player_id = player_id

    @property
    def player_name(self):
        return self._player_name
    
    @player_name.setter
    def player_name(self, player_name):
        self._player_name = player_name

    # Function to create a new row in the Game table
    @classmethod
    def create_game(cls):
        conn = get_connection()
        cursor = conn.cursor()
        game_name = input("Enter game name: ")
        number_of_players = int(input("Enter number of players: "))
        coach_name = input("Enter coach name: ")
        cursor.execute("INSERT INTO games (game_name, number_of_players, coach_name) VALUES (?,?,?)",
                        (game_name, number_of_players, coach_name))
        conn.commit()
        game_id = cursor.lastrowid
        print(f"Game created successfully! Game ID: {game_id}")
        return cls(game_id, game_name, number_of_players, None, coach_name)
    
    # Function to retrieve a game object using the name
    @classmethod
    def get_game_by_name(cls, game_name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM games WHERE game_name =?", (game_name,))
        game = cursor.fetchone()
        return cls(game[0], game[1], game[2], game[3], game[4])
    
    # Function to delete a record from the games table
    def delete_game(game_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM games WHERE id =?", (game_id,))
        conn.commit()
        print(f"Game with id {game_id} has been deleted successfully!")

    # Function that updates the contents of a games table
    @classmethod
    def update_game(cls, game_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM games WHERE id =?", (game_id,))
        game = cursor.fetchone()
        print(game)
        game_name = input("Enter game name: ")
        number_of_players = int(input("Enter number of players: "))
        coach_name = input("Enter coach name: ")
        cursor.execute("UPDATE games SET game_name =?, number_of_players =?, coach_name =? WHERE id =?",
                       (game_name, number_of_players, coach_name, game_id))
        conn.commit()
        print(f"Game with id {game_id} has been updated successfully!")

    