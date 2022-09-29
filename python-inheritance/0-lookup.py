#!/usr/bin/python3*
"""

A module that representes a function that returns
a list of attributes of a given object

"""


def lookup(obj):
    """
    A funciton that returns a list of
    attributes and methods of an object
    """
    return dir(obj)
