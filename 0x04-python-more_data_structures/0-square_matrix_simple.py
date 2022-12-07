#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        squares = [[r ** 2 for r in matrix[i]]for i in range(0, len(matrix))]
        return squares
