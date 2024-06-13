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
    def get_equipment_by_id(equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipment WHERE id =?", (equipment_id,))
        equipment = cursor.fetchone()
        if equipment:
            return list(equipment)
            
        else:
            return None
    
    # Function to delete a record from the equipment table
    def delete_equipment(equipment_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipment WHERE id =?", (equipment_id,))
        conn.commit()
        print(f"Equipment with id {equipment_id} has been deleted successfully!")

    # Function that updates the contents of an equipment table
    def get_all_equipment():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipment")
        equipment = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        result = []
        for equipment in equipment:
            equipment_dict = dict(zip(column_names, equipment))
            result.append(equipment_dict)
        return result