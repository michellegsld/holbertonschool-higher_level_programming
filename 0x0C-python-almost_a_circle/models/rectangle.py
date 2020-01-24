#!/usr/bin/python3
"""
rectangle.py
class Rectangle
imports and inherits class Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Create a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Sets all attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validates and sets the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validates and sets the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Validates and sets x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returns y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Validates and sets y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints in stdout the Rectangle made up of '#', accounting for x and y
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(0, self.__x):
                print(" ", end='')
            print('#' * self.__width)

    def __str__(self):
        """
        Prints a specific statement with info about the instance
        """
        i, x, y = str(self.id), str(self.__x), str(self.__y)
        w, h = str(self.__width), str(self.__height)
        return ("[Rectangle] (" + i + ") " + x + "/" + y + " - " + w + "/" + h)
