from models.data import Base
from sqlalchemy import Column, Integer, String


class Team(Base):
    """
    """
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
