#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import *
"""
Script delete all States containing letter 'a'
"""


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    session.commit()
    session.close()
