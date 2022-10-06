#!/usr/bin/python3
"""

A module that representes a class Rectangle

"""


class Rectangle(__import__("models.base").Base):
    """
    A class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A class constructor to initialise an instance
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for the attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method for the attribute width"""
        self.__width = width

    @property
    def height(self):
        """getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for the height attribute"""
        self.__height = height

    @property
    def x(self):
        """getter method for the x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for the x attribute"""
        self.__x = x

    @property
    def y(self):
        """getter method for the y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for the y attribute"""
        self.__y = y
