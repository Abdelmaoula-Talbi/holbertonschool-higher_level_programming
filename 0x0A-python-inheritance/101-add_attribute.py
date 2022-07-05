#!/usr/bin/python3
"""Represents a function that adds attribute"""


def add_attribute(obj, attr, value):
    """function to add a new attribute if it is possible"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
