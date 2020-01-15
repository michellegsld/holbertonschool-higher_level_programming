#!/usr/bin/python3
"""
6-rectangle.py
class Rectangle
"""


class Rectangle:
    """Represents a Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes private instance attributes: width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A property setter to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retrieves the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Retrieves the perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns the string that prints the Rectangle"""
        rec = ''
        if self.__height > 0 and self.__width > 0:
            for i in range(self.__height):
                rec = rec + ('#' * self.__width) + '\n'
        return rec[:-1]

    def __repr__(self):
        """Returns a string representation of the Rectangle"""
        sw, sh = str(self.__width), str(self.__height)
        return "Rectangle(" + sw + ", " + sh + ")"

    def __del__(self):
        """Destroys an instance"""
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1
