#!/usr/bin/python3
"""
This module contains the function that solves the UTF-8 validation challenge
"""


def validUTF8(data):
    """
        Determines if a given data set represents a valid UTF-8 encoding

        Args:
            data (list): List of integers representing UTF-8 characters
        Return:
                True if is a valid UTF-8 encoding ELSE, return False
    """
    if not isinstance(data, list):
        return False
    for x in data:
        if not isinstance(x, int):
            return False
    state = 0
    for byte in data:
        if state == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                state += 1
            elif (byte >> 4) == 0b1110:
                state += 2
            elif (byte >> 3) == 0b11110:
                state += 3
            else:
                return False
        else:
            if (byte >> 6) == 0b10:
                state -= 1
            else:
                return False
    return state == 0
