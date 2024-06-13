from db.connection import get_connection

class Player:
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

    # Function to create a new row for player table
    @classmethod
    def create_player(cls):
        conn = get_connection()
        cursor = conn.cursor()
        player_name = input("Enter player name: ")
        year_of_birth = int(input("Enter the player's year of Birth: "))
        gender = input("Enter your gender(F or M): ")
        game_name = input(f"Which game will Player {player_name} be playing: ")
        cursor.execute("INSERT INTO players (player_name, year_of_birth, gender, game_name) VALUES (?,?,?,?)",
                       (player_name, year_of_birth, gender, game_name))
        conn.commit()
        player_id = cursor.lastrowid
        print(f"Player created successfully! Player ID: {player_id}")
        return cls(player_id, player_name, year_of_birth, gender, game_name)
    
    # Function to retrieve a player object using id
    def get_player_by_id(player_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE id =?", (player_id,))
        player = cursor.fetchone()
    
    # Function to delete a record from the players table
    def delete_player(player_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM players WHERE id =?", (player_id,))
        conn.commit()
        print(f"Player with id {player_id} has been deleted successfully!")

    # Function that Updates the contents of player table
    @classmethod
    def update_player(cls, player_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE id =?", (player_id,))
        player = cursor.fetchone()
        print(player)
        player_name = input("Enter player name: ")
        year_of_birth = int(input("Enter the player's year of Birth: "))
        gender = input("Enter your gender(F or M): ")
        game_name = input(f"Which game will Player {player_name} be playing: ")
        cursor.execute("UPDATE players SET player_name =?, year_of_birth =?, gender =?, game_name =? WHERE id =?",
                       (player_name, year_of_birth, gender, game_name, player_id))
        conn.commit()
        print(f"Player with id {player_id} has been updated successfully!")
