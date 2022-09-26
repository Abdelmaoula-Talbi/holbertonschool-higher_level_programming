#!/usr/bin/python3
"""

A module that representes a function that prints a square"

"""

def print_square(size):
    """
    A function that prints a square with the symbol '#'
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
