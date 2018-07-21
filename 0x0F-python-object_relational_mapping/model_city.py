#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import *
"""
Class 'City'
"""


Base = declarative_base()


class City(Base):
    """
    Class Definition State
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
