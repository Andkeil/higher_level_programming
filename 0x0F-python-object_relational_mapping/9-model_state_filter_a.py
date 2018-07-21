#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *
"""
Script all State objects from hbtn_0e_6_usa containing 'a'
"""


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    for state in session().query(State)\
                          .filter(State.name.contains('a')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session().close()
