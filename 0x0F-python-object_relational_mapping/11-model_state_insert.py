#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *
"""
Script adding a new state
"""


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    new_state_add = session.query(State)\
                    .filter_by(name=new_state.name).first()
    print(new_state_add.id)
    session.commit()
    session.close()
