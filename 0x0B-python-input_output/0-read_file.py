#!/usr/bin/python3
"""
0-read_file.py
read_file(filename="")
"""


def read_file(filename=""):
    """
    Reads a text file and prints it line by line
    """
    with open(filename) as fil:
        for line in fil:
            print("{}".format(line), end='')
