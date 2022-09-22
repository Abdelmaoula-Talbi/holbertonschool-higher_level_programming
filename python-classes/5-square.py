#!/usr/bin/python3
"""
A module that represents a Square class
"""


class Square:
    """A class square that defines a square and calculate its
    area, and using getter and setter to retrieve and set the size attribute"""
    def __init__(self, size=0):
        """Initialize a Square object"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """A getter for the value of the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter for the value of the attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate the area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
