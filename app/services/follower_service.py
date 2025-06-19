from models.follower import Follower
from repositories.follower_repository import FollowerRepository

class FollowerService:

    def __init__(self, follower_repository: FollowerRepository):
        self.follower_repository = follower_repository

    def create_register_follower(self, followers, data_from_user_created: list):
        for follow in followers:
            follower_instance = Follower(follow["login"], data_from_user_created[0])
            self.follower_repository.create_register_follower(follower_instance)