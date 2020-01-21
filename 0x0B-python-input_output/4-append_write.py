#!/usr/bin/python3
"""
4-append_write.py
append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Appends to or creates a file
    """
    with open(filename, "a+") as fil:
        return fil.write(text)
