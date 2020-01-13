#!/usr/bin/python3
"""
3-say_my_name.py
def say_my_name(first_name, last_name="")
tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a first and last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
