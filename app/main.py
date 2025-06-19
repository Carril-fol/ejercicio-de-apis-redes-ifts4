import requests

from config.db import Database

from repositories.user_repository import UserRepository
from repositories.repo_repository import RepoRepository
from repositories.follower_repository import FollowerRepository

from services.user_services import UserService
from services.repo_service import RepoService
from services.follower_service import FollowerService

db = Database()

user_repository = UserRepository(db)
user_service = UserService(user_repository)

repo_repository = RepoRepository(db)
repo_service = RepoService(repo_repository)

follower_repository = FollowerRepository(db)
follower_service = FollowerService(follower_repository)

validation = True
while validation:
    try:
        # Ingreso de usuario
        print("Ingrese el nombre de usuario de Github que desea ver:")
        answer = input("# ").lower()

        # Si el usuario ingresa "salir"
        if answer == "salir":
            validation = False
            print("Gracias por usar el programa.")
            break

        # URLs que se van a utilizar
        url_repos = f"https://api.github.com/users/{answer}/repos" # URL de los repositorios del usuario correspondiente
        url_followers = f"https://api.github.com/users/{answer}/followers" # URL de los seguidores del usuario correspondiente

        # Respuestas de Github
        response_repos = requests.get(url_repos)
        response_followers = requests.get(url_followers)

        # Si el código de estado fue exitoso (200), entonces...
        if response_repos.status_code == 200:
            user_service.create_user(answer) # Creación del usuario
            data_from_user_created = user_service.get_user_by_username(answer) # Información del usuario

            repositories_from_github = response_repos.json() # Repositorios provenientes de la URL
            repo_service.create_repo(repositories_from_github, data_from_user_created) # Guardado en la base de datos los repositorios correspondientes del usuario

            followers_from_github = response_followers.json() # Seguidores provenientes de la URL
            follower_service.create_register_follower(followers_from_github, data_from_user_created) # Guardado en la base de datos los seguidores correspondientes del usuario

        # Si el código de estado fue 400 o 404, entonces...
        elif response_repos.status_code == 400 or response_repos.status_code == 404:
            print("Usuario no encontrado o no existe el usuario ingresado.")

    except Exception as error:
        print(f"Ocurrio un error: {error}")