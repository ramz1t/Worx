from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

Engine = create_engine('sqlite:///data/data.db')
Base.metadata.create_all(Engine)
Sessions = sessionmaker(bind=Engine)