#!/usr/bin/python3
"""Represents a function to verify an object inheritance"""


def is_kind_of_class(obj, a_class):
    """Verify if object obj is an instance of of a subclass
    of a given class
    Args:
        obj: object to verify
        a_class: class to check its inheritance
    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
