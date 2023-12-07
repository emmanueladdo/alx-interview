#!/usr/bin/python3
"""
This module is for function to onlock
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): Each box contains keys
        represented by positive integers.
                    The first box (boxes[0]) is unlocked.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    keys = [0]
    for n in keys:
        for key in boxes[n]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    return len(keys) == len(boxes)
