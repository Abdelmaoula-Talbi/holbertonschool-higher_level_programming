#!/usr/bin/python3
"""Represents a class that defines a square
    by private attribute size
    and calculate the square area.

"""


class Square:
    """Initializes the class

    Args:
        size (int): The paramater to define the square
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Public instance method that returns the current square area
        Returns:
            The current square area.
        """
        return self.__size * self.__size
