from fastapi import FastAPI, requests, status
from fastapi.responses import JSONResponse
import uvicorn
from git.gitfuncs import get_repo_commits, get_repo_contributors, get_user_repo_stats, get_repo_branches
from git.params import Auth_params
from logic.repo import get_repo_by_name, create_new_repo, create_repo
from models.repo import ApiCreateRepo, RepoInfo
from logic.user import create_new_user, change_user_email, change_user_password, change_user_gender, change_user_name, \
    add_repo_to_user, get_user_added_repos
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
from func.helpers import get_repo_users_count, get_most_effective_user, get_least_effective_user, \
    get_repo_commits_count, get_user_repo_commits, get_repo_branches_count, get_commits_leaderboard
import requests
from data.data import SERVER_DOMAIN
from git.params import Auth_params


app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")
templates = Jinja2Templates(directory="views/templates")


'''urls to add smth'''


@app.post('/addrepo')
def add_repo(repo: ApiCreateRepo, current_user=Depends(get_current_user)):
    user_repo = create_repo(repo)
    response = add_repo_to_user(user_repo, current_user.id)
    return response


@app.post('/createaccount')
def create_account(user: ApiCreateUser):
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


'''urls to get pages'''


@app.get("/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/profile")
def get_profile(request: Request, current_user=Depends(get_current_user)):
    repos = get_user_added_repos(user_id=current_user.id)
    return templates.TemplateResponse("profile.html", {"request": request,
                                                       "email": current_user.email,
                                                       "name": current_user.name,
                                                       "gender": current_user.gender,
                                                       "repos": repos})


@app.get("/main")
def get_main_page(request: Request, current_user=Depends(get_current_user)):
    return templates.TemplateResponse("mainpage.html", {"request": request,
                                                        "gender": current_user.gender})


@app.get("/stats/{reponame}/{user}")
def get_stats(reponame: str, user: str, request: Request, current_user=Depends(get_current_user)):
    db_repo = get_repo_by_name(repo_name=reponame)
    contributors_list = get_repo_contributors(auth_params=Auth_params, repo_name=reponame, users_name=db_repo.owner_username)
    commits = get_repo_commits(auth_params=Auth_params, repo_name=reponame, username=db_repo.owner_username)
    repo_contributors_count = get_repo_users_count(contributors_list)
    most_effective_user = get_most_effective_user(commits)
    least_effective_user = get_least_effective_user(commits)
    commits_count = get_repo_commits_count(commits)
    user_repo_commits = get_user_repo_commits(commits, user)
    branches = get_repo_branches(auth_params=Auth_params, repo_name=reponame, username=db_repo.owner_username)
    repo_branches = get_repo_branches_count(branches)
    print(commits[0])
    commit_leaderboard = get_commits_leaderboard(commits)
    return templates.TemplateResponse("stats.html", {"request": request,
                                                     "reponame": reponame,
                                                     "username": user,
                                                     "gender": current_user.gender,
                                                     "repo_contributors_count": repo_contributors_count,
                                                     "most_effective_user": most_effective_user,
                                                     "least_effective_user": least_effective_user,
                                                     "repo_commits_count": commits_count,
                                                     "user_repo_commits": user_repo_commits,
                                                     "repo_branches": repo_branches,
                                                     "commit_leaderboard": commit_leaderboard})


'''urls to edit smth'''


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
