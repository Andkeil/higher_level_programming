#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *
"""
Script list all State objects from hbtn_0e_6_usa
"""


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    for instance in session().query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
    session().close()
