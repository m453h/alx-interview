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
    # Perform initial checks to ensure that a list is provided
    if not isinstance(data, list):
        return False

    # Check if the list provided only contains integers
    for x in data:
        if not isinstance(x, int):
            return False
    # State will help us to track continuation bytes expected i.e. 10xxxxxx
    state = 0

    # Iterate through th e list of bytes in the data to perform validation
    for byte in data:
        # Make sure that each byte is within the valid 8-bit range
        byte %= 256

        # If an invalid byte value is encountered then return false
        if byte >= 248:
            return False

        # In state 0, identify and count expected continuation bytes
        if state == 0:
            # 1 Byte character, 0 continuation bytes
            if (byte >> 7) == 0:
                continue
            # 2 Bytes character, 1 continuation byte
            elif (byte >> 5) == 0b110:
                state += 1
            # 3 Bytes character, 2 continuation bytes
            elif (byte >> 4) == 0b1110:
                state += 2
            # 4 Bytes character, 3 continuation bytes
            elif (byte >> 3) == 0b11110:
                state += 3
            else:
                # Improper format, return false
                return False
        else:
            # For continuation bytes, check if they start with '10'
            if (byte >> 6) == 0b10:
                # Reduce the state count, aim is to reach 0 for valid UTF-8
                state -= 1
            else:
                # Otherwise we are in continuation and we don't have 10xxxxxx
                return False

    # If state is 0, all characters were correctly terminated
    return state == 0
