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
    Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
            - if size is equal to 0, print an empty line
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

    def my_print(self):
        """Public instance method"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
