#!/usr/bin/python3
"""
This script contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

_metadata = MetaData()
Base = declarative_base(metadata=_metadata)

class State(Base):
    """
    Table states
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
