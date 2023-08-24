#!/usr/bin/python3
"""A script that prints the first State object
from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # Create a MySQL connection using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query the database to get the first State object
    first_state = session.query(State).order_by(State.id).first()
    # Check if the table is empty
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
    session.close()
