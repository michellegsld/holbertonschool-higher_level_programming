#!/usr/bin/python3
"""
14-pascal_triangle.py
pascal_triangle(n)
"""


def pascal_triangle(n):
    """
    Returns a list of lists that rep. the Pascal’s triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
