#!/usr/bin/python3
"""
4-inherits_from.py
inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a_class that was (in)directly inherited
    """
    return(not issubclass(a_class, type(obj)))
