#!/usr/bin/python3
"""
8-load_from_json_file.py
load_from_json_file(filename)
imports json
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a file using JSON representation
    """
    with open(filename) as fil:
        json.load(fil)
