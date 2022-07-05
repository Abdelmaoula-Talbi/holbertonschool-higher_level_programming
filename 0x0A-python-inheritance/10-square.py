#!/usr/bin/python3
"""Represents a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from class Rectangle"""

    def __init__(self, size):
        """initiation"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Represents the area of the square"""
        return self.__size * self.__size
