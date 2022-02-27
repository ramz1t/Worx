import jwt
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ApiServer.Cryptic.cryptic import oauth2_scheme, SECRET_KEY, ALGORITHM

server=FastAPI()
'''
def get_session():
    session=session_factory()
    try:
        yield session
    except:
        session.close()
'''
@server.post("/user")
def create_user(user: CreateUser, session: Session = Depends(get_session)):
    return register_new_user(session, User(**user.dict()))


@server.post("/auth")
def auth(token: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    return auth(token.username, token.password, session)


@server.post("/user/{token}")
def get_user_by_token(token: str = Depends(oauth2_scheme),session: Session=Depends(get_session)):
    data=jwt.decode(token, SECRET_KEY, ALGORITHM)
    return data
