class Admin:
    admins = {
        1: {"username": "menda", "password": "@menda2024", "admin_type": "Games Manager"},
        2: {"username": "sarah", "password": "@sarah2024", "admin_type": "Player Manager"},
        3: {"username": "ombuna", "password": "@ombuna2024", "admin_type": "Equipment Manager"},
        4: {"username": "abby", "password": "@abby2024", "admin_type": "Coach Manager"}
    }

    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"Admin(id={self.id}, username={self.username}, password={self.password}, role={self.role})"

    def check_authentication(self, username, password):
        for admin in self.admins.values():
            if admin["username"] == username and admin["password"] == password:
                return True
        return False

    @classmethod
    def get(cls, username):
        for id, admin in cls.admins.items():
            if admin["username"] == username:
                return cls(id, admin["username"], admin["password"], admin["admin_type"])
        return None