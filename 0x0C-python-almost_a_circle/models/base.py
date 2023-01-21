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
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a .json file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(
                    cls.to_json_string(
                        [i.to_dictionary() for i in list_objs]
                        )
                    )

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_instance = cls(2, 5)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """that serializes in CSV"""
        filename = cls.__name__ + ".csv"
        res = [item.to_dictionary() for item in list_objs]
        with open(filename, "w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """that deserializes in CSV"""
        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    res_dict[k] = int(v)
                # formatting with create()
                res.append(cls.create(**res_dict))
        return res

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ opens a window and draws all the Rectangles and Squares """

