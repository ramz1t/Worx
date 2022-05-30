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

from fastapi import Depends, FastAPI, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from models.auth_token import Token
from logic.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user, \
    oauth2_scheme
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")
templates = Jinja2Templates(directory="views/templates")


@app.post('/addrepo/{reponame}/{owner_username}')
def add_repo(reponame, owner_username):
    repo = ApiCreateRepo(name=reponame, owner_username=owner_username)
    response = create_new_repo(repo)
    return response


@app.post('/createaccount/{login}/{passhash}/{gender}')
def create_account(login, passhash, gender):
    user = ApiCreateUser(email=login, password=passhash, gender=gender)
    response = create_new_user(user)
    return response


@app.post("/token", response_model=Token)
def login_for_access_token(response: Response,form_data: OAuth2PasswordRequestForm = Depends()):  #added response as a function parameter
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
def auth(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/users/me/")
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user


@app.get("/profile")
def get_profile(current_user=Depends(get_current_user)):
    return current_user.email

if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
