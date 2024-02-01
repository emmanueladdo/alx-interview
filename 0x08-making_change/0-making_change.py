#!/usr/bin/python3
"""
This module takes a coins, total
as args an returns the fewest number
to meet a give total
"""


def makeChange(coins, total) -> int:
    """
    Function makechange returns
    number
    """
    sum = 0
    if total is None and total <= 0:
        return 0
    coins.sort(reverse=True)
    for item in coins:
        if (total < item):
            pass
        quotient, remainder = divmod(total, item)
        total = remainder
        sum += quotient
    if (total != 0):
        return -1
    return sum
