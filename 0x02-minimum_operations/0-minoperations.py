#!/usr/bin/python3
"""
This module contains the function that solves the lockboxes challenge
"""


def minOperations(n):
    """
    Determines the minimum number of operations required to create
    a text file with H characters using Copy all and Paste operations

    Args:
       n (integer): The number of H characters that should be generaterd
    Return: The number of minimum operations required or 0 if not possible
    """
    if n <= 1:
        return 0

    operations_count = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            operations_count = operations_count + divisor
            n = n / divisor
        else:
            divisor = divisor + 1

    return operations_count
