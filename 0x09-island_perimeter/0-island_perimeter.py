#!/usr/bin/python3
"""
Module return the perimeter
of a the island grid
"""


def island_perimter(grid):
    """
    Function takes Grid as arg
    and returns the peimeter
    """
    perimeter = 0
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == 1:
                perimeter += 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
            j += 1
        i += 1
    return perimeter
