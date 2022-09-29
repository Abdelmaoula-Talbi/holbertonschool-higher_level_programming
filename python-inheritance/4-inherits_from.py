#!/usr/bin/python3
"""

A module that representes a function that
checks if an object is an instance a class

"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
