#!/usr/bin/python3
"""

A module that representes a function
that writes a string to a text file

"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
