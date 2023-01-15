#!/usr/bin/python3
""" the Square module """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square  """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__()
        self.width = size
        self.height = size
