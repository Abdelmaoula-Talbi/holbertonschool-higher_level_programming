#!/usr/bin/python3
"""

A module that representes a class Rectangle

"""

from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A class constructor to initialise an instance
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for the attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method for the attribute width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for the height attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter method for the x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for the x attribute"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter method for the y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for the y attribute"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        area function that calculates the area of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with
        the character # by taking care of x and y"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__method to print the Rectangle instance representation"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute"""
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        keys = ["id", "width", "height", "x", "y"]
        zipped = zip(keys, args)
        tuple_zip = tuple(zipped)
        for i in range(len(args)):
            setattr(self, tuple_zip[i][0], tuple_zip[i][1])

    def to_dictionary(self):
        """method that returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
