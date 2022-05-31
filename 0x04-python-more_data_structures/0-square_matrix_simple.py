#!/usr/bin/python3
"""A function to computes the square
value of all integers of a matrix.
"""

new_matrix = []


def square_matrix_simple(matrix=[]):
    for i in matrix:
        new_element = list(map((lambda x: x ** 2), i))
        new_matrix.append(new_element)
    return new_matrix
