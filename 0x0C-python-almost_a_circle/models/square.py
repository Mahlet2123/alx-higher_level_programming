#!/usr/bin/python3
""" the Square module """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.width = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
