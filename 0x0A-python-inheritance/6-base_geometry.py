#!/usr/bin/python3
"""Represents a class with public instance method"""


class BaseGeometry:
    """BaseGeometry with public instance
    method that raises an exception"""
    def area(self):
        """method to raise an exception"""
        raise Exception("area() is not implemented")
