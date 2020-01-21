#!/usr/bin/python3
"""
3-write_file.py
write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    Writes to or creates a file
    """
    with open(filename, "w+") as fil:
        return fil.write(text)
