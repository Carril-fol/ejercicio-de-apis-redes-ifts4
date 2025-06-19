from config.db import Database
from models.repository import Repository

class RepoRepository:

    def __init__(self, database: Database):
        self.database = database

    def create_repo(self, repo_instance: Repository):
        try:
            query = "INSERT INTO repositories (name, id_user) VALUES (%s, %s)"
            cursor = self.database.connection.cursor()
            cursor.execute(query, (repo_instance.name, repo_instance.id_user, ))
            self.database.connection.commit()
            cursor.close()
        except Exception as error:
            print(f"Ocurrio un error: {error}")