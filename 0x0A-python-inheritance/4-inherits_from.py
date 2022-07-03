#!/usr/bin/python3
"""Represents a function to verify an object inheritance"""


def inherits_from(obj, a_class):
    """Verify if an object is a subclass of a given class
    Arg:
        obj: object to check.
        a_class: class to check its inheritance.
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ;
        otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
