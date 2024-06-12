from db.connection import get_connection
import sqlite3

class Player:
    all = {}
    def __init__(self, id, player_name, year_of_birth, gender, game_id):
        self.id = id
        self.player_name = player_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.game_id = game_id

    def __repr__(self):
        pass

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, game_id):
        self._game_id = game_id

    @property
    def player_name(self):
        return self._player_name
    
    @player_name.setter
    def player_name(self, player_name):
        self._player_name = player_name

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO players (player_name, year_of_birth, gender, game_id)
            VALUES (?,?,?,?)
        """
        try:
            cursor.execute(query, (self.player_name, self.year_of_birth, self.gender, self.game_id))
            conn.commit()
        except sqlite3.Error as error:
            print(error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def create(cls, player_name):
        player = cls(player_name)
        player.save()
        return player
    
    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM players
        """
        try:
            cursor.execute(query)
            players = cursor.fetchall()
            return [Player(*player) for player in players]
        except sqlite3.Error as error:
            print(error)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    # Method that returns a list of players for a certain game