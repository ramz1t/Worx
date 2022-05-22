from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits, get_repo_contributors, get_user_repo_stats
from git.params import Auth_params
from logic.repo import get_repo_by_name, create_new_repo
from models.repo import ApiCreateRepo
from logic.user import create_new_user
from models.user import ApiCreateUser
import json


app = FastAPI()


@app.get('/commits/{reponame}/{username}')
def get_repo_user_commits(reponame, username):
    repo = get_repo_by_name(repo_name=reponame)
    owner_username = repo.owner_username
    commits = get_repo_contributors(repo_name=reponame, auth_params=Auth_params, users_name=owner_username)
    for i in commits:
        if i['login'] == username:
            return i['contributions']


@app.get('/stats/{reponame}')
def get_repo_stats(reponame):
    repo = get_repo_by_name(repo_name=reponame)
    owner_username = repo.owner_username
    stats = get_user_repo_stats(repo_name=reponame, auth_params=Auth_params, users_name=owner_username)
    result = {'description': stats['description'], 'link': 'https://github.com/{}/{}'.format(owner_username, reponame)}
    return result


@app.post('/addrepo/{reponame}/{owner_username}')
def add_repo(reponame, owner_username):
    repo = ApiCreateRepo(name=reponame, owner_username=owner_username)
    response = create_new_repo(repo)
    return response


@app.get('/users/{reponame}')
def get_all_users(reponame):
    pass


@app.post('/createaccount/{login}/{passhash}')
def create_account(login, passhash):
    user = ApiCreateUser(email=login, password=passhash)
    response = create_new_user(user)
    return response


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
