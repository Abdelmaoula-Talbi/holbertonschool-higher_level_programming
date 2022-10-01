#!/usr/bin/python3
"""

A modulte that representes a function

"""


def add_attribute(My_class, My_att, My_value):
    """
    A function that adds an attribute to a class
    """
    if dir(My_class)[0] != "__class__":
        raise TypeError("can't add new attribute")
    else:
        setattr(My_class, My_att, My_value)
