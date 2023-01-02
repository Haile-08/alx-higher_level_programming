#!/usr/bin/python3
"""divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """return matrix divided by div"""

    row_len = 0
    div_list = []

    for i in matrix:
        if row_len is 0:
            row_len = len(i)
        else:
            if row_len != len(i):
                raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_len = len(i)
    if type(div) is not in [int, float]:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        row = []
        for j in i:
            row.append(j/div)
        div_list.append(row)
        row.clear()
    return div_list
