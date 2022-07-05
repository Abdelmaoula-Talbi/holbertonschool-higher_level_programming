#!/usr/bin/python3
"""Represents a class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt inherits from int
    but has == and != operators inverted
    """
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
