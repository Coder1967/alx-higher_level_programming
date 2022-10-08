#!/usr/bin/python3
""" creating table 'cities' in
    the database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, ForeignKey
from model_state import State, Base


class City(Base):
    """
    definition for the class 'cities'
    """
    __tablename__ = 'cities'
    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
