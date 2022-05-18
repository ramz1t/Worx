from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from data.data import Base


class ApiNewAuth(BaseModel):
    email: str
    password: str


class AuthSession(Base):
    __tablename__ = 'AuthSessions'
    token = Column(String, primary_key=True)
    id = Column(Integer)
