#!/usr/bin/python3
"""

A module that representes a function
that checks for the type of an object

"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    return (type(obj) is a_class)
