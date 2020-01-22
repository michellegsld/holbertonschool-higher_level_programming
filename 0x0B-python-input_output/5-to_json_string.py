#!/usr/bin/python3
"""
5-to_json_string.py
to_json_string(my_obj)
imports json
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    """
    return json.JSONEncoder().encode(my_obj)
