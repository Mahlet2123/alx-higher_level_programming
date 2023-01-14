#!/usr/bin/python3
""" the base module """


class Base:
    """ class base """
    __nb_objects = 0
    def __init__(self, id=None):
        """ Instantiation with id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
