import hashlib

class UserModel:
    def __init__(self, db):
        self.db = db

    def hash_password(self, password):
        # basic hashing for class project
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        hashed = self.hash_password(password)
        try:
            self.db.query(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed)
            )
            return True, "Account created!"
        except Exception:
            return False, "Username already exists."

    def login(self, username, password):
        hashed = self.hash_password(password)
        cursor = self.db.query(
            "SELECT id FROM users WHERE username=? AND password=?",
            (username, hashed)
        )
        row = cursor.fetchone()
        if row:
            return True, row[0]
        return False, None
