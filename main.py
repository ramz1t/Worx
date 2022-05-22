from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits, get_repo_contributors, get_user_repo_stats
from git.params import Auth_params
from logic.repo import get_repo_by_name, create_new_repo
from models.repo import ApiCreateRepo
from logic.user import create_new_user
from models.user import ApiCreateUser, User
import json
from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel


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


@app.post('/createaccount/{login}/{passhash}/{gender}')
def create_account(login, passhash, gender):
    user = ApiCreateUser(email=login, password=passhash, gender=gender)
    response = create_new_user(user)
    return response


from models.auth_token import Token
from logic.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user, \
    oauth2_scheme


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/")
def main_page():
    return {"Hello": "World"}


@app.get("/users/me/")
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(token: str = Depends(oauth2_scheme)):
    return [{"item_id": "Foo", "owner": "current_user.username"}]


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
