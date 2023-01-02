#!/usr/bin/python3
""" an empty class rectangle that defines a rectangle """


class Rectangle:
    """define a class called Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0:
            return ""
        if self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        self.number_of_instances -= 1
        print("Bye rectangle...")
