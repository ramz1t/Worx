from fastapi.responses import JSONResponse
from fastapi import status
from data import User
from lol import Sessions


def create_new_user(user) -> JSONResponse:
    with Sessions() as session:
        if not session.query(User).filter_by(username=user.username).first() is None:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content='Username already in use')
        if len(user.password) < 8 or len(user.username) < 4:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content='Invalid data')
        session.add(user)
        session.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def change_user(_id, new_email):
    with Sessions() as session:
        user = session.query(User).filter_by(id=_id).first()
        user.email = new_email
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
