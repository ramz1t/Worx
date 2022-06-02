from pydantic import BaseModel
from data.data import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.association_user_repo import association_table

class User(Base):
    """
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    gender = Column(String)
    name = Column(String)
    repos = relationship("Repo", secondary=association_table)


class ApiCreateUser(BaseModel):
    email: str
    password: str
    gender: str
    name: str


class ChangeEmail(BaseModel):
    new_email: str


class ChangeName(BaseModel):
    new_name: str


class ChangeGender(BaseModel):
    new_gender: str


class ChangePassword(BaseModel):
    old_password: str
    new_password: str
