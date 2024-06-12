from db.connection import get_connection

class Coach:
    def __init__(self, id, coach_name, year_of_birth, gender, game_id):
        self.id = id
        self.coach_name = coach_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.game_id = game_id

    def __repr__(self):
        return f"Coach('{self.coach_name}', {self.year_of_birth}, '{self.gender}')"
        pass

    @property
    def coach_id(self):
        return self._coach_id
    
    @coach_id.setter
    def coach_id(self, coach_id):
        self._coach_id = coach_id

    @property
    def coach_name(self):
        return self._coach_name
    
    @coach_name.setter
    def coach_name(self, coach_name):
        self._coach_name = coach_name

    @classmethod
    def create_coach(cls):
        conn = get_connection()
        cursor = conn.cursor()
        coach_name = input("Enter coach name: ")
        year_of_birth = int(input("Enter your year of Birth: "))
        gender = input("Enter your gender(F or M): ")
        game_name = input(f"Which game will Coach {coach_name} be coaching: ")
        cursor.execute("INSERT INTO coach (coach_name, year_of_birth, gender, game_name) VALUES (?,?,?,?)",
                       (coach_name, year_of_birth, gender, game_name))
        conn.commit()
        coach_id = cursor.lastrowid
        print(f"Coach created successfully! Coach ID: {coach_id}")

    