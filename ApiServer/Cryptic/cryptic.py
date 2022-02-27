import datetime

import jwt as jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

pwd_context = CryptContext(schemes=['bcrypt'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "93dfa0cadfa52a24ca6ae079612e2d53"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 40


def to_hash(password: str):
    return pwd_context.hash(password)


def verify_password(password, password_hash):
    return pwd_context.verify(password, password_hash)


def generate_token(username: str):
    return jwt.encode(
        {
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
            'sub': username
        }
        , SECRET_KEY, algorithm=ALGORITHM)
