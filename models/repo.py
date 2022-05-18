from data.data import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class Repo(Base):
    """
    """
    __tablename__ = 'repos'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_username = Column(String)


class ApiCreateRepo(BaseModel):
    id: int
    name: str
    owner_username: str
