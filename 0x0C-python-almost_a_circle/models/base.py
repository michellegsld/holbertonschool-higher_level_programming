#!/usr/bin/python3
"""
base.py
class Base
importing json
"""
import json


class Base:
    """
    Main purpose: manage the id attribute and handle json
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

    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation
        """
        return json.dumps(list_dictionaries)
