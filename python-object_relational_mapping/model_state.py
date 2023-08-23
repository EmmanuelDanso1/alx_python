#!/usr/bin/python3
"""
python file
that contains the class definition of a
State and an instance Base = declarative_base(
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
"""
Modifying the database URL accordingly
(username, password, db_name)
"""
db_url = 'mysql://username:password@localhost:3306/db_name'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
if __name__ == "__main__":
    # Creating the table in the database
    Base.metadata.create_all(engine)
