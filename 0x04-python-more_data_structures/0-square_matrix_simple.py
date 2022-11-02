#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [[row[coloumn]**2 for coloumn in range(len(matrix[0]))] for row in matrix]
