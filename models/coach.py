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

    #Function to create a new row in the coach table
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

    # Function to get a coach object using the id
    def get_coach_by_id(coach_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coach WHERE id =?", (coach_id,))
        coach = cursor.fetchone()
        if coach:
            return list(coach)
            
        else:
            return None

    # Function to delete a record from the coach table
    def delete_coach(coach_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM coach WHERE id =?", (coach_id,))
        conn.commit()
        print(f"Coach with id {coach_id} has been deleted successfully!")

    # Function that updates the contents of a coach table
    @classmethod
    def update_coach(cls, coach_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coach WHERE id =?", (coach_id,))
        coach = cursor.fetchone()
        print(coach)
        coach_name = input("Enter coach name: ")
        year_of_birth = int(input("Enter your year of Birth: "))
        gender = input("Enter your gender(F or M): ")
        game_name = input(f"Which game will Coach {coach_name} be coaching: ")
        cursor.execute("UPDATE coach SET coach_name =?, year_of_birth =?, gender =?, game_name =? WHERE id =?",
                       (coach_name, year_of_birth, gender, game_name, coach_id))
        conn.commit()
    