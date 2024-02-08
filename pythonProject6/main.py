import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables

DSN = 'postgresql://postgres:Python2023@localhost:5432/second'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

session.close()
