#!/usr/bin/python3
"""
Module contains ``matrix_mul``:
a matrix multiplication function
"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    inverted_b = []
    for Row in range(len(m_b[0])):
        new_row = []
        for Column in range(len(m_b)):
            new_row.append(m_b[Column][Row])
        inverted_b.append(new_row)  
    new_matrix = []
    for row in m_a:
        new_row = []
        for column in inverted_b:
            product = 0
            for i in range(len(inverted_b[0])):
                product += row[i] * column[i]
            new_row.append(product)
        new_matrix.append(new_row)  
    return new_matrix
