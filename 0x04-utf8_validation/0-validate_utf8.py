#!/usr/bin/python3
"""
This module contains the function that solves the UTF-8 validation challenge
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (list): A list of integers representing the UTF-8
                    set of characters

    Return:
            True if is a valid UTF-8 encoding ELSE, return False
    """
    if type(data) is not list and len(data) == 0:
        return False

    i = 0

    while i < len(data):
        binary_block = format(data[i], '08b')
        if binary_block.startswith('0'):
            i += 1
        elif binary_block.startswith('110'):
            if i + 1 < len(data) \
                    and format(data[i + 1], '08b').startswith('10'):
                i += 2
            else:
                return False
        elif binary_block.startswith('1110'):
            if i + 2 < len(data) \
                    and format(data[i + 1], '08b').startswith('10') \
                    and format(data[i + 2], '08b').startswith('10'):
                i += 3
            else:
                return False
        elif binary_block.startswith('11110'):
            if i + 3 < len(data) \
                    and format(data[i + 1], '08b').startswith('10') \
                    and format(data[i + 2], '08b').startswith('10') \
                    and format(data[i + 3], '08b').startswith('10'):
                i += 4
            else:
                return False
        else:
            return False

    return True
