#!/usr/bin/python3
"""Represents a class that defines a square
    by private attribute size
    and calculates the square area.

"""


class Square:
    """Square class with exception raising
    and public instance method to calculate
    the square area and print the square by
    using '#' and spaces.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class Square
        Args:
            size (int): paramater size to define the size of the square.
            position (tuple): paramater position to define the spaces into the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """A getter method to retrieve the size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter method to set the value
        of the size private attribute
        Args:
            value (int): new value to set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """A getter method to retrieve the position private attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """A setter method to set the value of the position private attribute
        Args:
            value (tuple): new value to set the position of the square"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Public instance method that returns the current square area
        Returns:
            The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints in stdout the square
        with the character #, if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        for l in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
