#!/usr/bin/python3
"""

A module that representes a Square class

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square that is a subclass of Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method to print the Square instance representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter method for size attribute"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
