from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits, get_repo_contributors, get_user_repo_stats
from git.params import Auth_params
import json


app = FastAPI()


@app.get('/commits/{reponame}/{username}')
def get_repo_user_commits(reponame, username):
    commits = get_repo_contributors(repo_name=reponame, auth_params=Auth_params, users_name=username)
    return commits


@app.get('/stats/{reponame}')
def get_repo_stats(reponame):
    username = 'AlexGyver'
    stats = get_user_repo_stats(repo_name=reponame, auth_params=Auth_params, users_name=username)
    result = {'description': stats['description'], 'link': 'https://github.com/{}/{}'.format(username, reponame)}
    return result


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
