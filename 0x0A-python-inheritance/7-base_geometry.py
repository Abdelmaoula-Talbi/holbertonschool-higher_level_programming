#!/usr/bin/python3
"""Represents a class with public instance method"""


class BaseGeometry:
    """BaseGeometry with public instance
    method that raises an exception"""
    def area(self):
        """method to raise an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Validates value
        Args:
            name: name of value to validate.
            value: value to validate.
        Raises:
            TypeError if value is not integer.
            ValueError if value <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
