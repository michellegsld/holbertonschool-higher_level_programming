#!/usr/bin/python3
"""
9-rectangle.py
class Rectangle
imports and inherits class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        width and height must be validated and are privately set here
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Implements area() and overrides it
        """
        return self.__width * self.__height

    def __str__(self):
        """
        A Description of the Rectangle
        """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
