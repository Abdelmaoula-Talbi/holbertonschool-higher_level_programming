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

    def to_json_string(list_dictionaries):
        """
        A method to return the JSON string
        representation of list_dictionaries
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))
