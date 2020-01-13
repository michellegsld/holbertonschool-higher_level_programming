#!/usr/bin/python3
"""
2-matrix_divided.py
def matrix_divided(matrix, div)
tests/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix, else raises an error
    """
    te_str = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix[0]) is 0:
        raise TypeError(te_str)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0 or type(div) is None:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(te_str)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int \
               and type(matrix[i][j]) is not float:
                raise TypeError(te_str)
    rowlen = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) is not rowlen:
            raise TypeError("Each row of the matrix must have the same size")
    newmat = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newmat[i][j] = round(matrix[i][j] / div, 2)
    return newmat
