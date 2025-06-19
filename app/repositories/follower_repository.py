from config.db import Database
from models.follower import Follower

class FollowerRepository:

    def __init__(self, database: Database):
        self.database = database
    
    def create_register_follower(self, follower_instance: Follower):
        try:
            query = "INSERT INTO followers (username_follower, id_user) VALUES (%s, %s)"
            cursor = self.database.connection.cursor()
            cursor.execute(query, (follower_instance.username_follower, follower_instance.id_user,))
            self.database.connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Ocurrio un error: {error}")