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

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute"""
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        keys = ["id", "size", "x", "y"]
        zipped = zip(keys, args)
        tuple_zip = tuple(zipped)
        for i in range(len(args)):
            setattr(self, tuple_zip[i][0], tuple_zip[i][1])
