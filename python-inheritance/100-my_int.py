#!/usr/bin/python3
"""

A module that representes the class MyInt

"""


class MyInt(int):
    """
    A class MyInt that is a subclass of class int
    """
    def __init__(self, integer):
        self.__integer = integer

    def __eq__(self, integer):
        return super().__ne__(integer)

    def __ne__(self, integer):
        return super().__eq__(integer)
