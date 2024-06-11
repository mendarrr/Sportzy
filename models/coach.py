from db.connection import get_connection

class Coach:
    def __init__(self, id, coach_name, year_of_birth, gender, game_id):
        self.id = id
        self.coach_name = coach_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.game_id = game_id

    def __repr__(self):
        pass