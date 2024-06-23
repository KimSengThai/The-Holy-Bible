from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# for setting connection to SQLite database using SQLAlchemy
# Imports SQLAlchemy Components: create_engine to establish database connections, and sessionmaker to manage sessions.
# Creates Database Engine: Connects to an SQLite database located at lib/data.db.
# Sets Up Session Factory: Configures a factory for creating session objects bound to the engine.
# Creates Session: Instantiates a session to interact with the database.

engine = create_engine("sqlite:///lib/data.db")
Session = sessionmaker(bind=engine)
session = Session()