import sqlalchemy as db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flaskr.settings import SQLALCHEMY_DATABASE_URI

# Db initialization
database = SQLAlchemy()

# Connect to the db
engine = db.create_engine(SQLALCHEMY_DATABASE_URI)
connection = engine.connect()

# Create session object
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

metadata = db.MetaData()
# Define the tables
table_cryptos = db.Table('cryptos', metadata, autoload=True, autoload_with=engine)
table_prices = db.Table('prices', metadata, autoload=True, autoload_with=engine)

