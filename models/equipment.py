from db.connection import get_connection

class Equipment:
    def __init__(self, id, equipment_name, game_id):
        self.id = id
        self.equipment_name = equipment_name
        self.game_id = game_id

    def __repr__(self):
        pass