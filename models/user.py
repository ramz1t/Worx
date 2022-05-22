from pydantic import BaseModel
from data.data import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    """
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    gender = Column(String)

class ApiCreateUser(BaseModel):
    email: str
    password: str
