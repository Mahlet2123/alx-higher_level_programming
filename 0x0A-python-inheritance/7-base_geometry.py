#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ Public instance method:
        def area(self): that raises an Exception with the
        message area() is not implemented """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
            
