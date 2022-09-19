#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda x: x**2, matrix[x])), range(len(matrix))))
