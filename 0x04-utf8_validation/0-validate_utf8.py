#!/usr/bin/python3
"""
a method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    determine if the given data set represents
    a valid UTF-8 encoding
    """
    numOfBytes = 0
    for num in data:
        mask = 1 << 7
        if not numOfBytes:
            while mask & num:
                numOfBytes += 1
                mask >>= 1
            if not numOfBytes:
                continue
            if numOfBytes == 1 or numOfBytes > 4:
                return False
        else:
            if num >> 6 != 0b10:
                return False
        numOfBytes -= 1
    return numOfBytes == 0
