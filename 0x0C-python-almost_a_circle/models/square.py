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
        self.__size = size

    def __str__(self):
        """
        Prints a specific statement with info about the instance
        """
        i, x, y, s = str(self.id), str(self.x), str(self.y), str(self.width)
        return ("[Square] (" + i + ") " + x + "/" + y + " - " + s)

    @property
    def size(self):
        """
        Returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Validates and sets the width
        """
        super().__init__(value, value, self.x, self.y, self.id)
        self.__size = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of Square
        """
        attkwarg = {"id": None, "size": None, "x": None, "y": None}
        attributes = {0: self.id, 1: self.__size, 2: self.x, 3: self.y}
        reinit = []
        if args is not None and len(args) > 0:
            for i in range(4):
                if i >= len(args):
                    reinit.append(attributes.get(i))
                else:
                    reinit.append(args[i])
        else:
            for key, value in kwargs.items():
                attkwarg.update({key: value})
            i = 0
            for value in attkwarg.values():
                if value is None:
                    reinit.append(attributes.get(i))
                else:
                    reinit.append(value)
                i += 1
        self.__init__(reinit[1], reinit[2], reinit[3], reinit[0])

    def to_dictionary(self):
        """
        Returns dictionary representation of Square
        """
        attributes = {"id": None, "x": None, "size": None, "y": None}
        final = []
        for key, value in attributes.items():
            value = getattr(self, key)
            attributes.update({key: value})
        return attributes