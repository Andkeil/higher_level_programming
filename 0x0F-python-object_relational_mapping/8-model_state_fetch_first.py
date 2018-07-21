#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *
"""
Script first State object from hbtn_0e_6_usa
"""


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    rtrn = session().query(State).first()
    try:
        print("{}: {}".format(rtrn.id, rtrn.name))
    except:
        print("Nothing")
    session().close()
