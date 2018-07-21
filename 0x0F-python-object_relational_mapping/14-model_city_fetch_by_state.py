#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *
from model_city import *
"""
Script print all City objects
"""


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for state, city in session.query(State, City)\
                              .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
