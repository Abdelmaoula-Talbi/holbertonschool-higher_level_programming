#!/usr/bin/python3
"""

A module that represents a function

"""


def add_integer(a, b=98):

    """
    function add_integer that adds 2 integers
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if (a+1) == a:
        raise OverflowError('number too large')
    if b+1 == b:
        raise OverflowError('number too large')
    return (a + b)
