#!/usr/bin/python3
"""Represents a subclass that
inherits from built-in list class"""


class MyList(list):
    """a subclass that inherits from
    built-in list class and have a
    funtion to sort that list"""
    def print_sorted(self):
        """print the sorted list MyList in ascending order"""
        new_list = print(sorted(self))
        return new_list
