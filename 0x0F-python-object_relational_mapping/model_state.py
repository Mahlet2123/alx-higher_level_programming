#!/usr/bin/python3
"""State class module"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String



Base = declarative_base()


class State(Base):
    """ state class """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
