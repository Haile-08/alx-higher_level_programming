#!/usr/bin/python3
"""matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """matrix_mul
    Args:
        m_a: list input
        m_b: list input
    """
    if not isinstance(m_a, list):
        TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            TypeError("m_b must be a list of lists")
    for i in m_a:
        if not i:
            ValueError("m_a can't be empty")
    for i in m_b:
        if not i:
            ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if type(j) not in [int, float]:
                TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) not in [int, float]:
                TypeError("m_b should contain only integers or floats")
    num = 0
    for i in m_a:
        if num == 0:
            num = len(i)
        elif num != len(i):
            TypeError("each row of m_a must be of the same size")
    num = 0
    for i in m_b:
        if num == 0:
            num = len(i)
        elif num != len(i):
            TypeError("each row of m_b must be of the same size")
    if len(m_a) != len(m_b[0]):
        ValueError("m_a and m_b can't be multiplied")
    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
