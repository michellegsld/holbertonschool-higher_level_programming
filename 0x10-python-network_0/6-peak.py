#!/usr/bin/python3
"""
6-peak.py
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    ints = list_of_integers
    num = None
    for i in range(len(ints)):
        num = ints[i]
        if i == 0:
            if num >= ints[i + 1]:
                break
        if i < len(ints) - 1:
            if num >= ints[i + 1] and num >= ints[i - 1]:
                break
        if i == len(ints) - 1:
            if num >= ints[i - 1]:
                break
    return num
