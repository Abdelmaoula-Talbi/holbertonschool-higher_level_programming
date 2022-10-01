#!/usr/bin/python3
"""

A module that representes a function
that adds attribute to an object

"""


def add_attribute(My_class, My_att, My_value):
    """
    A function that adds an attribute to an object
    if it is possible, otherwise it raises an exception
    """
    if hasattr(My_class, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(My_class, My_att, My_value)
