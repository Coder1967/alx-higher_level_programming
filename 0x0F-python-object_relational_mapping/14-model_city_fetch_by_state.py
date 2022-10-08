#!/usr/bin/python3
"""module updates  state with id of 2
   to 'New Mexico'
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    i = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State.name, City.id, City.name).join(
            City).order_by(City.id).all()
    for row in rows:
        print('{}: ({}) {}'.format(row[0], row[1], row[2]))
