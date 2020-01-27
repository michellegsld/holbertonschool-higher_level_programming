#!/usr/bin/python3
"""
base.py
class Base
importing json
importing os.path
"""
import json
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation
        -- before had:
        if list_dictionaries is None or not list_dictionaries:
            return json.dumps("[]")
        return json.dumps(list_dictionaries)
        -- now:
        """
        ld = list_dictionaries
        return ("[]" if ld is None or not ld else json.dumps(ld))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON string representation to a file
        """
        filename = str(cls.__name__) + ".json"
        if list_objs is None:
            list_objs = []
        finlist = []
        for item in list_objs:
            finlist.append(item.to_dictionary())
        with open(filename, "w+", encoding="utf-8") as fil:
            fil.write(Base.to_json_string(finlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        -- before:
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
        -- now:
        """
        js = json_string
        return ([] if js is None or not js else json.loads(js))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        jsonlist = []
        if not os.path.isfile(filename):
            return []
        with open(filename) as fil:
            jsonlist = cls.from_json_string(fil.read())
        return [cls.create(**item) for item in jsonlist]
