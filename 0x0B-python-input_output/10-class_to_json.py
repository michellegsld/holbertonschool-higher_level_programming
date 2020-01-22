#!/usr/bin/python3
"""
10-class_to_json.py
class_to_json(obj)
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    """
    if obj.__dict__:
        return obj.__dict__
