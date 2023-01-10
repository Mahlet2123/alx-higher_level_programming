#!/usr/bin/python3
""" object (Python data structure) represented by a JSON string """


import json
""" imports the module """
def from_json_string(my_str):
    """ A function that returns the an object (Python data structure)
        represented by a JSON string"""
    return (json.loads (my_str))
