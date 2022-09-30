#!/usr/bin/python3
"""

A module that representes a class Square

"""


class Square(__import__('9-rectangle').Rectangle):
    """
    A class that defines a Square class that
    is a subclass of Rectangle class
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
