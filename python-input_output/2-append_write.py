#!/usr/bin/python3
"""

A module that representes a function
that appends a string to a text file

"""


def append_write(filename="", text=""):
    """
    A function that appends a string to the end of a text file
    and returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
