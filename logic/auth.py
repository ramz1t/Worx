from datetime import timedelta, datetime
from typing import Union

from fastapi.responses import JSONResponse
from fastapi import status, HTTPException, Depends

from data.data import Sessions
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from models.auth import AuthSession, ApiNewAuth
from func.helpers import generate_token
from func.helpers import hashing_password
from passlib.context import CryptContext
from models.auth_token import TokenData
from func.helpers import get_user_by_email

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# def new_auth(auth: ApiNewAuth) -> str or JSONResponse:
#     with Sessions() as session:
#         user = get_user_by_username(auth.username)
#         if not user or user.password_hash != hashing_password(auth.password):
#             return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Incorrect login or password')
#         auth_session = AuthSession(token=generate_token(), user_id=user.id)
#         session.add(auth_session)
#         session.commit()
#         return auth_session.token


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(email=token_data.username)
    if user is None:
        raise credentials_exception
    return user
