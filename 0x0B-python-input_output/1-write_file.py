#!/usr/bin/python3
""" a method to write to a file """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        f = f.write(text)
        return (f)
