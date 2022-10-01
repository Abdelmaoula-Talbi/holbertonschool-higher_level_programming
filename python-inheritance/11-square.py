#!/usr/bin/python3
"""

A module that representes a class Square

"""


class Square(__import__('9-rectangle').Rectangle):
    """
    A class Square that is a subclass of the class Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[{Square.__name__}] {self.__size}/{self.__size}"
