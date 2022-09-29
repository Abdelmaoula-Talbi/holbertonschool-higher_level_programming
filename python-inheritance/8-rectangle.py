#!/usr/bin/python3
"""

A module that representes the class Rectangle
that is a subclass of the class BaseGeometry

"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """
    A class Rectangle that is a subclass of BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
