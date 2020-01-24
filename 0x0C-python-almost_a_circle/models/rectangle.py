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
        Sets the width
        """
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
        Sets the height
        """
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
        Sets x
        """
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
        Sets y
        """
        self.__y = value
