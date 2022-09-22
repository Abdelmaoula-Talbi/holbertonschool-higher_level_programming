#!/usr/bin/python3
"""
A module that represents a Square class
"""


class Square:
    """A class square that defines a square and calculate its
    area, using getter and setter to retrieve and set the size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (type(position) is not tuple or
                len(position) != 2 or
                position[0] < 0 or
                position[1] < 0 or
                type(position[0]) is not int or
                type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """A getter to retrieve the value of the attribute position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """A setter to set the value for the attribute position"""
        if (type(value) is not tuple or
                len(value) != 2 or
                value[0] < 0 or
                value[1] < 0 or
                type(value[0]) is not int or
                type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate the area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if (self.__size == 0):
            print()
        else:
            for k in range(self.position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
