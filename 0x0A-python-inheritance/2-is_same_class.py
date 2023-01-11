#!/usr/bin/python3
""" exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """ Afunction that returns True if the object is exactly
        an instance of the specified class ; otherwise False."""
    if type(obj) == a_class:
        return True
    else:
        return False
