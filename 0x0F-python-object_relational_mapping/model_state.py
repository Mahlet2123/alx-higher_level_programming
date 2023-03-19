#!/usr/bin/python3
"""State class module"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String



Base = declarative_base()


class state(base):
    """ state class """
    __tablename__ = 'states'

    id = column(Integer, autoincrement=True, nullable = False, primary-key = True)
    name = column(String(128), nullable=False)
