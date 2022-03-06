from fastapi.responses import JSONResponse
from fastapi import status

from data.data import Sessions
from user.helpers import get_user_by_username
from auth.models import AuthSession, ApiNewAuth
from auth.helpers import generate_token
from user.helpers import hashing_password


def new_auth(auth: ApiNewAuth) -> str or JSONResponse:
    with Sessions() as session:
        user = get_user_by_username(auth.username)
        if not user or user.password_hash != hashing_password(auth.password):
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='Incorrect login or password')
        auth_session = AuthSession(token=generate_token(), user_id=user.id)
        session.add(auth_session)
        session.commit()
        return auth_session.token
