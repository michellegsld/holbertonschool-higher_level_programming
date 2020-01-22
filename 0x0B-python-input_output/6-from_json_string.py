#!/usr/bin/python3
"""
6-from_json_string.py
from_json_string(my_str)
imports json
"""
import json


def from_json_string(my_str):
    """
    Returns the object from a JSON representation
    """
    return json.JSONDecoder().decode(my_str)
