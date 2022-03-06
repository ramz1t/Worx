from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import create_engine
from sqlalchemy.orm import sessionmaker
import models.data as base

base.Base = declarative_base()

from models import *

base.Engine = create_engine('sqlite:///data/data.db')
base.Base.metadata.create_all(base.Engine)
base.Sessions = sessionmaker(bind=base.Engine)

