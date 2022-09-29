#!/usr/bin/python3
"""

A module that representes the class Rectangle
that is a subclass of the class BaseGeometry

"""


class BaseGeometry:
    """
    A class that defines a public instance method
    that raise an exception
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class Rectangle that is a subclass of BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
