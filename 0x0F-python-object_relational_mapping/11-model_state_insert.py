#!/usr/bin/python3
"""module prints adds a new state
   'Louisiana' to database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state1 = State(name="Louisiana")
    session.add(state1)
    session.commit()
    print(state1.id)
