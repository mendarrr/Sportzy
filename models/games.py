from db.connection import get_connection
import sqlite3

class Game:
    def __init__(self, id, game_name, number_of_players,coach_id,coach_name):
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
    @classmethod
    def create(cls, game_name, number_of_players, coach_id, coach_name):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO games (game_name, number_of_players, coach_id, coach_name)
            VALUES (?, ?, ?, ?)
        """
        try:
            cursor.execute(query, (game_name, number_of_players, coach_id, coach_name))
            game_id = cursor.lastrowid
            conn.commit()
            return cls(game_id, game_name, number_of_players, coach_id, coach_name)
        except sqlite3.Error as error:
            print(error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

# Method that returns a list of players for a certain game
    def players(self):
        from models.players import Player
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM players
            WHERE game_id =?
        """
        try:
            cursor.execute(query, (self.id,))
            players = cursor.fetchall()
            return [Player(*player) for player in players]
        except sqlite3.Error as error:
            print(error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def coach(self):
        from models.coach import Coach
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM coach
            WHERE game_id =?
        """
        try:
            cursor.execute(query, (self.id,))
            coach = cursor.fetchone()
            return Coach(*coach)
        except sqlite3.Error as error:
            print(error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def equipment(self):
        from models.equipment import Equipment
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM equipment
            WHERE game_id =?
        """
        try:
            cursor.execute(query, (self.id,))
            equipment = cursor.fetchone()
            return Equipment(*equipment)
        except sqlite3.Error as error:
            print(error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()