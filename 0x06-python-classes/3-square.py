#!/usr/bin/python3
"""Represents a class that defines a square
    by private attribute size
    and calculates the square area.

"""


class Square:
    """Square class with exception raising
    and public instance method to calculate
    the square area

    """
    def __init__(self, size=0):
        """Initialize the class Square
        Args:
            size (int): paramater size to define the size of the square.
        """
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
