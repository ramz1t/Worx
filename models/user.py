from models.__base__ import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    """

    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    api_key = Column(String)
