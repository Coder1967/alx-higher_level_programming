#!/usr/bin/python3
"""working with database via sqlalchemy"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    class State creates a table 'states' in a
    database
    """
    __tablename__ = "states"
    id = Column(Integer(), unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
