#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_list = []    
        for i in range(len(matrix)):
            new_list.append(row[i] ** 2)
        new_matrix.append(new_list)
    return new_matrix
