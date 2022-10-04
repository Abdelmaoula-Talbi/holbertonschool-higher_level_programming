#!/usr/bin/python3
"""

A module that representes a function that returns
the JSON representation of an object

"""


def to_json_string(my_obj):
    """
    A function to_json_string() that returns the
    JSON representation of an object (string)
    """
    import json
    return (json.dumps(my_obj))
