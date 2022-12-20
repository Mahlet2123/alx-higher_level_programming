#!/usr/bin/python3
"""   class Square that defines a square by: (based on 0-square.py)
    private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module """


class Square:
    """ define a class called square """
    def __init__(self, size):
        """ Private instance attribute: size """
        self.__size = size
