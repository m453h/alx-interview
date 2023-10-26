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
    state = 0
    for byte in data:
        if state == 0:
            if (byte >> 7) == 0b0:
                state = 0
            elif (byte >> 5) == 0b110:
                state = 1
            elif (byte >> 4) == 0b1110:
                state = 2
            elif (byte >> 3) == 0b11110:
                state = 3
            else:
                return False
        elif state > 0:
            if (byte >> 6) != 0b10:
                return False
            state = state - 1
    return state == 0
