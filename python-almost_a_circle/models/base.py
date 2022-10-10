#!/usr/bin/python3
"""

A module that representes a class Base

"""


class Base:
    """
    A class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A method to return the JSON string
        representation of list_dictionaries
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """A class method that writes the JSON string
        representation of list_objs to a file"""
        import json
        my_list = []
        filename = cls.__name__ + ".json"
        for i in list_objs:
            my_list.append(cls.to_json_string(i.__dict__))
        with open(filename, mode="w", encoding='utf-8') as my_file:
            if list_objs is None:
                my_file.write("[]")
            my_file.write(str(my_list))
