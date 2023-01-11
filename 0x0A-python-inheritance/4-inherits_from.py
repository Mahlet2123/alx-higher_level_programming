#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """ Afunction that returns True if the object is exactly
        an instance of the specified class ; otherwise False."""
    """if (issubclass(obj, a_class)):"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
