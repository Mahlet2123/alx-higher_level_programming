#!/usr/bin/python3
""" a method to append to a file """


def append_write(filename="", text=""):
    """ A function that appends a string to a text file (UTF8) and,
        returns the number of characters written """
    with open(filename, 'a', encoding="utf-8") as f:
        f = f.write(text)
        return (f)
