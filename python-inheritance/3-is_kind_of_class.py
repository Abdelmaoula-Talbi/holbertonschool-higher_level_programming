#!/usr/bin/python3
"""

A module that representes a function that
checks if an object is an instance a class

"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    return (isinstance(obj, a_class))
