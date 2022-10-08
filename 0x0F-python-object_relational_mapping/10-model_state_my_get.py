#!/usr/bin/python3
"""module prints the id of the state
passed as the 4th argument in the cmd line
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
    results = session.query(State).filter(State.name == argv[4]).first()

    if results is not None:
        print(results.id)
    else:
        print('Not found')
