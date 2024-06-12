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
    @classmethod
    def get_player_by_id(cls, player_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE id =?", (player_id,))
        player = cursor.fetchone()
        return cls(player[0], player[1], player[2], player[3], player[4])
    
    def display_player_roles(self):
        for role in Player.roles:
            print(f"{role}: {self.roles[role]}")
