#!/usr/bin/python3
"""Represents a function that verify an object"""


def is_same_class(obj, a_class):
    """verify if object is an instance of
    a specific class
    Args:
        obj: the object to verify.
        a_class: the class to verify if the obj is an instance of it.
    Returns:
        True if the object is exactly an instance of the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
