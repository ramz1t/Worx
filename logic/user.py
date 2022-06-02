from fastapi.responses import JSONResponse
from fastapi import status
from models.user import User, ApiCreateUser
from data.data import Sessions
from logic.auth import get_password_hash, verify_password
from models.repo import ApiCreateRepo

def create_new_user(api_user) -> JSONResponse:
    with Sessions() as session:
        if not session.query(User).filter_by(email=api_user.email).first() is None:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content='Email already in use')
        if len(api_user.password) < 8 or len(api_user.email) < 4:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Invalid data')
        user = User(email=api_user.email, password=get_password_hash(api_user.password), gender=api_user.gender, name=api_user.name)
        session.add(user)
        session.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def change_user_email(email, new_email):
    with Sessions() as session:
        user = session.query(User).filter_by(email=email).first()
        user.email = new_email
        session.add(user)
        session.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def change_user_name(email, new_name):
    with Sessions() as session:
        user = session.query(User).filter_by(email=email).first()
        user.name = new_name
        session.add(user)
        session.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def change_user_gender(email, new_gender):
    with Sessions() as session:
        user = session.query(User).filter_by(email=email).first()
        user.gender = new_gender
        session.add(user)
        session.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def change_user_password(email, old_password, new_password):
    with Sessions() as session:
        user = session.query(User).filter_by(email=email).first()
        if not verify_password(plain_password=old_password, hashed_password=user.password):
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content='Password missmatch')
        user.password = get_password_hash(new_password)
        session.add(user)
        session.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def get_user_info(user_id: int):
    with Sessions() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='user not found')
    return [user.email, user.password, user.api_key]


def delete_user(_id):
    with Sessions() as session:
        if not session.query(User).filter_by(id=_id).first() is None:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content='error,lol wtf')
        user = session.query(User).filter_by(id=_id).first()
        session.delete(user)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def add_repo_to_user(repo: ApiCreateRepo, user_id):
    with Sessions() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='user not found')
        user.repos.append(repo)
        session.add(user)
        session.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def get_user_added_repos(user_id: int):
    with Sessions() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='user not found')
        repos = []
        for repo in user.repos:
            repos.append(repo.name)
        return repos
