#!/usr/bin/python3
""" the base module """
import json
import csv


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if  list_dictionaries == None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a .json file """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs == None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([item.to_dictionary() for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string == None:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy_instance = cls(2, 5)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        with open(filename, 'r') as f:
            return json.load(f)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ that serializes in CSV """
        filename = cls.__name__ + ".csv"
        

    @classmethod
    def load_from_file_csv(cls):
        """ that deserializes in CSV """
