#!/usr/bin/python3
"""

A module that representes a function that prints a string

"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints 'My name is <first_name> <last_name>'
    """
    if type(first_name) is not str:
        raise TypeError("first name must be a string")
    if type(last_name) is not str:
        raise TypeError("last name must be a string")

    print(f"My name is {first_name} {last_name}")
