#!/usr/bin/python3
"""
A module that represents a Square class
"""


class Square:
    """A class square that defines a square and calculate its area"""
    def __init__(self, size=0):
        """Initialize a Square object"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
