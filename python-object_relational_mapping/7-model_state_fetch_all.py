#!/usr/bin/python3
"""
A script that lists all State
objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    List all the state objects specified
    Args:
        username(str): username for database connection
        password(str): specified password for user
        db_name(str): database to be connected to
    Returns:
    list: list of State object
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py mysql_user mysql_password db_name")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # connection to the MYSQL server
    engine = create_engine('mysql+mysqdb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # quering the db to list all state object
    states = session.query(State).order_by(State.id).all
    # displaying the results
    for state in states:
        print("{}:{}".format(state.id, state.name))
    # closing session
    session.close()
