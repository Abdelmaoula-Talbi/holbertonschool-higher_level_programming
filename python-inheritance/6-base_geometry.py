#!/usr/bin/python3
"""

A module that representes the class BaseGeometry

"""


class BaseGeometry:
    """
    A class that defines a public instance method
    that raise an exception
    """
    def area(self):
        raise Exception("area() is not implemented")
