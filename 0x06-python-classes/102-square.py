#!/usr/bin/python3
""" Write a class Square that defines a square by: (based on 4-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        - size must be an integer, otherwise raise a TypeError exception
                with the message size must be an integer
        - if size is less than 0, raise a ValueError exception
                with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
        that returns the current square area
        - Square instance can answer to comparators: 
            ==, !=, >, >=, < and <= based on the square area
    You are not allowed to import any module """


class Square:
    """define a class called square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """the current square area"""
        return self.__size**2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __it__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
