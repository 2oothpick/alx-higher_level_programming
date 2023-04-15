#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    # exception raised for m_a not being a list of a list
    for i in m_a:
        if type(i) is not list:
            raise ValueError('shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)')
    #   exception for m_b not being list of list
    for i in m_b:
        if type(i) is not list:
            raise ValueError('shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)')
    return (np.matmul(m_a, m_b))
