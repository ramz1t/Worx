from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits, get_repo_contributors
from git.params import Auth_params

app = FastAPI()


@app.get('/repo/{repourl}/{username}')
def get_repo_stats(repourl, username):
    commits = get_repo_contributors(repo_name=repourl, auth_params=Auth_params, users_name=username)
    for i in commits:
        if i['login'] == username:
            return i


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
