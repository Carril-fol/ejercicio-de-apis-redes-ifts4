from models.repository import Repository
from repositories.repo_repository import RepoRepository

class RepoService:

    def __init__(self, repo_repository: RepoRepository):
        self.repo_repository = repo_repository

    def create_repo(self, data, data_from_user_created):
        for repo in data:
            repo_instance = Repository(repo["name"], data_from_user_created[0])
            self.repo_repository.create_repo(repo_instance)