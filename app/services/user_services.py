from repositories.user_repository import UserRepository

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str):
        return self.user_repository.create_user(username)
    
    def get_user_by_username(self, username: str):
        return self.user_repository.get_user_by_username(username)