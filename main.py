from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits, get_repo_contributors, get_user_repo_stats
from git.params import Auth_params
from logic.repo import get_repo_by_name
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


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
