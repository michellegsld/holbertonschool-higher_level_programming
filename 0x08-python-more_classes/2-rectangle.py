#!/usr/bin/python3
"""
2-rectangle.py
class Rectangle
"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes private instance attributes: width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the private instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A property setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private instance attribute: height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, value):
        """A property setter to set height"""
        self.__height = value

    def area(self):
        """Retrieves the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Retrieves the perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2
