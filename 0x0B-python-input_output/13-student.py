#!/usr/bin/python3
"""
13-student.py
class Student
"""


class Student:
    """
    Defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Prints the __dict__
        """
        if type(attrs) is list:
            for i in range(len(attrs)):
                if type(attrs[i]) is not str:
                    return self.__dict__
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces the attributes of the Student isntance
        """
        for key, value in json.items():
            return
