from db.connection import get_connection

class Game:
    def __init__(self, id, game_name, number_of_players, player_id, coach_id, equipment_id):
        self.id = id
        self.game_name = game_name
        self.number_of_players = number_of_players
        self.player_id = player_id
        self.coach_id = coach_id
        self.equipment_id = equipment_id

    def __repr__(self):
        pass