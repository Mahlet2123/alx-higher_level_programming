#!/usr/bin/python3
""" Write a class Square that defines a square by: (based on 6-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        - size must be an integer, otherwise raise a TypeError exception
                with the message size must be an integer
        - if size is less than 0, raise a ValueError exception
                with the message size must be >= 0
    Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
        - position must be a tuple of 2 positive integers, otherwise
            raise a TypeError exception with the
                - message position must be a tuple of 2 positive integers

    Instantiation with optional size and optional position:
        def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self):
        that returns the current square area
    Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
            - if size is equal to 0, print an empty line
            - position should be use by using space -
                Don’t fill lines by spaces when position[1] > 0

    Printing a Square instance should have the same behavior as my_print()
    You are not allowed to import any module """


class Square:
    """define a class called square"""

    def __str__(self):
        """stringifyies a value"""
        return (self.my_ret[:-1])


    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(val, int) for val in value)
            or not all(val >= 0 for val in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """the current square area"""
        return self.__size**2

    def my_ret(self):
        """Public instance method"""
        ret = ""

        if self.__size == 0:
            return "\n"
        else:
            for new_line in range(0, self.__position[1]):
                ret += "\n"
        for i in range(0, self.__size):
            for space in range(self.__position[0]):
                ret += " "
            for j in range(self.__size):
                ret += "#"
            ret += "\n"
        return ret

    def my_print(self):
        """ prints the square"""
        print (self.ret, end="")
