#!/usr/bin/python3
"""
This  module contains the solution for the
rotate 2D Matrix by 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix by 90 degrees

    Args:
        matrix (List[List[int]]): The matrix to rotate

    Returns:
        None: The matrix is rotated in-place, thus no return value.
    """
    n = len(matrix)

    # Transpose the matrix by interchanging rows and columns
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row in the transposed matrix
    for i in range(n):
        left = 0
        right = n - 1
        while left < right:
            matrix[i][left], matrix[i][right] =\
                matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
