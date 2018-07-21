#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *
"""
Script State object from hbtn_0e_6_usa with name as user input
"""


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    arr = []
    for stateID in session().query(State.id)\
                            .filter(State.name == '{}'.format(sys.argv[4])):
        arr.append(stateID)
    try:
        print(arr[0][0])
    except:
        print("Not found")
    session().close()
