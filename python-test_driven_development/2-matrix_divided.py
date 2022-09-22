#!/usr/bin/python3
"""A module that contains
a function that divides all
elements of a matrix"""

def matrix_divided(matrix, div):
    """A function to divide all
    matrix elements

    Args:
        matrix: list of lists if integers/floats
        div: number on wich all elements of matrix will be divided

    Return:
        A new matrix"""

    matrix_divided = []
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        matrix_divided.append(list(map(lambda x: round((x / div), 2), row)))
    return matrix_divided
