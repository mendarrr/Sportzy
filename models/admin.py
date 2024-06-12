from db.connection import get_connection

class Admin:
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        pass

    def check_authentication(self, username, password):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM admin_credentials 
            WHERE username = ?
            AND password = ?
        """
        try:
            cursor.execute(query, (username, password))
            admin = cursor.fetchone()
            if admin:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @classmethod
    def get(cls, username):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM admin_credentials 
            WHERE username = ?
        """
        try:
            cursor.execute(query, (username,))
            admin = cursor.fetchone()
            if admin:
                return cls(admin["id"], admin["username"], admin["hashed_password"], admin["role"])
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()
            