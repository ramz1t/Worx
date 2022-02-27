from models.__base__ import Base
from sqlalchemy import Column, Integer, String


class Team(Base):
    """

    """
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)
