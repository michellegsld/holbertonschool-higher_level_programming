#!/usr/bin/python3
"""
base.py
class Base
"""


class Base:
    """
    Main purpose: manage the id attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Either set id or increment __nb__objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
