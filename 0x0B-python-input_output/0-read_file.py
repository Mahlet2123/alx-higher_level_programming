#!/usr/bin/python3
""" a method to read a file """


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, 'r', encoding="utf-8") as f:
        f = f.read()
        print(f, end="")
