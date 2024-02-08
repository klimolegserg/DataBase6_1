import sqlalchemy
import configparser
from sqlalchemy.orm import sessionmaker
from models import create_tables

config = configparser.ConfigParser()
config.read('settings.ini')
DSN = config['token']['dsn']
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

session.close()
