#!/usr/bin/python3
"""

A module that representes a function
that reads a text file

"""


def read_file(filename=""):
    """
    A function read_file() that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
