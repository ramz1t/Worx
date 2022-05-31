from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits, get_repo_contributors, get_user_repo_stats
from git.params import Auth_params
from logic.repo import get_repo_by_name, create_new_repo
from models.repo import ApiCreateRepo
from logic.user import create_new_user, change_user_email, change_user_password, change_user_gender, change_user_name
from models.user import ApiCreateUser, User, ChangeEmail, ChangeName, ChangePassword, ChangeGender
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


@app.post('/createaccount/{login}/{passhash}/{gender}/{name}')
def create_account(login, passhash, gender, name):
    user = ApiCreateUser(email=login, password=passhash, gender=gender, name=name)
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
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/profile")
def get_profile(request: Request, current_user=Depends(get_current_user)):
    return templates.TemplateResponse("profile.html", {"request": request, "email": current_user.email, "name": current_user.name})


@app.post("/change_email")
def change_email(body: ChangeEmail, current_user=Depends(get_current_user)):
    return change_user_email(email=current_user.email, new_email=body.new_email)


@app.post("/change_password")
def change_password(body: ChangePassword, current_user=Depends(get_current_user)):
    return change_user_password(email=current_user.email, old_password=body.old_password, new_password=body.new_password)


@app.post("/change_gender")
def change_gender(body: ChangeGender, current_user=Depends(get_current_user)):
    return change_user_gender(email=current_user.email, new_gender=body.new_gender)


@app.post("/change_name")
def change_name(body: ChangeName, current_user=Depends(get_current_user)):
    return change_user_name(email=current_user.email, new_name=body.new_name)


if __name__ == "__main__":  # Запуск сервера
    uvicorn.run(app, host="127.0.0.1", port=8000)
