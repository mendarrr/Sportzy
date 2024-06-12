from db.connection import get_connection

class Equipment:
    def __init__(self, id, equipment_name, game_id):
        self.id = id
        self.equipment_name = equipment_name
        self.game_id = game_id

    def __repr__(self):
        return f"Equipment('{self.equipment_name}')"
        pass

    @property
    def equipment_id(self):
        return self._equipment_id
    
    @equipment_id.setter
    def equipment_id(self, equipment_id):
        self._equipment_id = equipment_id

    @property
    def equipment_name(self):
        return self._equipment_name
    
    @equipment_name.setter
    def equipment_name(self, equipment_name):
        self._equipment_name = equipment_name

    #F unction to create a new row in the Equipment table
    @classmethod
    def create_equipment(cls):
        conn = get_connection()
        cursor = conn.cursor()
        equipment_name = input("Enter equipment name: ")
        game_name = input(f"In which game will {equipment_name} be used?: ")
        cursor.execute("INSERT INTO equipment (equipment_name, game_name) VALUES (?,?)",
                       (equipment_name, game_name))
        conn.commit()
        equipment_id = cursor.lastrowid
        print(f"Equipment created successfully! Equipment ID: {equipment_id}")

    # Function to get an equipment object usind the id
    @classmethod
    def get_equipment_by_id(cls, equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipment WHERE id =?", (equipment_id,))
        equipment = cursor.fetchone()
        return cls(equipment[0], equipment[1], equipment[2])