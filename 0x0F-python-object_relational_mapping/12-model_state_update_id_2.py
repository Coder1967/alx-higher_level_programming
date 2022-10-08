#!/usr/bin/python3
"""module updates  state with id of 2
   to 'New Mexico'
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
    state1 = session.query(State).filter(State.id == 2).first()
    state1.name = 'New Mexico'
    session.commit()
