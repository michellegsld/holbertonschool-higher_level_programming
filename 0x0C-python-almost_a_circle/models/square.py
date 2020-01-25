#!/usr/bin/python3
"""
square.py
class Square
imports and inherits class Rectangle
which imports and inherits class Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Creates a Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Sets all attributes
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints a specific statement with info about the instance
        """
        i, x, y, s = str(self.id), str(self.x), str(self.y), str(self.width)
        return ("[Square] (" + i + ") " + x + "/" + y + " - " + s)
