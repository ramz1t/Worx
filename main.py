from fastapi import FastAPI
import uvicorn
import git

app = FastAPI()


@app.get('/repo/{repourl}')
def f(repourl):
    return repourl


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
