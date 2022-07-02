#!/usr/bin/python3
"""Represents lookup function"""


def lookup(obj):
    """a function that returns a list of
    available attributes of an object"""
    return dir(obj)
