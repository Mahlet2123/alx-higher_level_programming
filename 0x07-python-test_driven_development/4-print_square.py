#!/usr/bin/python3
"""module for print_square method"""


def print_square(size):
    """
    function that prints a square with the character #.

    size is the size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
