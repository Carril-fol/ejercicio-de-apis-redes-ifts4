from config.db import Database

class UserRepository:

    def __init__(self, database: Database):
        self.database = database

    def create_user(self, username):
        try:
            query = "INSERT INTO users (username) VALUES (%s)"
            self.database.connection.cursor().execute(query, (username, ))
            self.database.connection.commit()
            print("Usuario registrado.")
        except Exception as error:
            print(f"Ocurrio un error: {error}")

    def get_user_by_username(self, username):
        try:
            query = "SELECT id FROM users WHERE username = %s"
            cursor = self.database.connection.cursor()
            cursor.execute(query, (username,))
            response = cursor.fetchone()
            cursor.close()
            return response
        except Exception as error:
            print(f"Ocurrio un error: {error}")