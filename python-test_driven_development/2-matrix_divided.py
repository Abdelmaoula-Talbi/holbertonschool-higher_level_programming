#!/usr/bin/python3
"""

A module that represents a function that divides a matrix

"""


def matrix_divided(matrix, div):
    """
    A function that take a matrix as argument and divide
    all its elements by a number div
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for row in matrix:
        new_row = []
        for elem in row:
            if (type(matrix) is not list or type(row) is not list or
                    type(elem) not in (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
            if (len(row) != len(matrix[0])):
                raise TypeError("Each row of the matrix must \
have the same size")
            new_row.append(round(elem/div, 2))
        new_list.append(new_row)
    return new_list
