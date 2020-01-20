#!/usr/bin/python3
"""
2-is_same_class.py
is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class
    """
    return(isinstance(obj, a_class))
