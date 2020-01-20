#!/usr/bin/python3
"""
3-is_kind_of_class.py
is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a specified class
    """
    return(isinstance(obj, a_class))
