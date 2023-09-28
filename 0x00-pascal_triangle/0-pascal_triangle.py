#!/usr/bin/python3
"""
This module contains pascal's triangle function
"""


def pascal_triangle(n):
    """
       Generate a pascal's triangle with specified
       number of rows

       Args:
            n: The number of rows of the Pascal's triangle
    """
    triangle = []
    if n >= 1:
        triangle.append([1])

    if n >= 2:
        triangle.append([1, 1])

    if n >= 3:
        for i in range(3, n + 1):
            previous_row = triangle[i - 2]
            new_row = [1]

            for j in range(0, len(previous_row) - 1):
                new_row.append(previous_row[j] + previous_row[j + 1])
            new_row.append(1)
            triangle.append(new_row)

    return triangle
