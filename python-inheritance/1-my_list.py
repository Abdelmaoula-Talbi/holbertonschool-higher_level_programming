#!/usr/bin/python3
"""

A module that representes a class
that is a subclass of list

"""

class MyList(list):
    """
    A class that represents
    a subclass of list
    """
    def print_sorted(self):
        print(sorted(self))
