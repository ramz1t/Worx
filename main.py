from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits

app = FastAPI()


@app.get('/repo/{repourl}')
def get_repo_stats(repourl):
    commits = get_repo_commits(repo_name=repourl, auth_params=('username: rakomorzh',
'GIT_TOKEN: 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'))
    return commits


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
