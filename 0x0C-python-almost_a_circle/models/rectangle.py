#!/usr/bin/python3
""" the Rectangle module """
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name, value):
        """validates all values"""
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

    def area(self):
        """the calculates the area"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            for new_line in range(self.__y):
                print()
        for i in range(0, self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for i in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str method"""
        return f"[Rectangle] ({self.id})\
                {self.__x}/{self.__y} {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            if len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "height":
                        self.__height = value
                    elif key == "width":
                        self.__width = value
                    elif key == "id":
                        self.id = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
