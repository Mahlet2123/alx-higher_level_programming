#!/usr/bin/python3
""" the Rectangle module """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name, value):
        """ validates all values """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if (name == "x" or name == "y") and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """rectangle's x position"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """rectangle's y position"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value
