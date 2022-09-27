#!/usr/bin/python3
"""

A module that representes a class Rectangle

"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    with two instance attributes 'width' and 'height'
    """
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        string = ""
        if self.perimeter == 0:
            return ""
#        return ("#" * self.__width + "\n") * self.__height
        for row in range(self.__height):
            if row > 0:
                string += "\n"
            for column in range(self.__width):
                string += "#"
        return string
