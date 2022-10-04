#!/usr/bin/python3
"""

A module that representes the function load_from_json_file(filename)

"""


def load_from_json_file(filename):
    """
    A function that creates an Object from a "JSON file"
    """
    import json
    with open(filename, encoding='utf-8') as my_file:
        return json.load(my_file)
