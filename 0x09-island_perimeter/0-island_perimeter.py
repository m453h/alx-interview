#!/usr/bin/python3
"""Defines a function for calculating perimeter of an island"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in a grid.

    Args:
        grid: A list of lists of integers

    Returns:
        (int) - The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # If we encounter a cell with 1 we add 4 in permiter
                perimeter += 4

                # If there is a cell on the left we subtract 2 (shared side)
                perimeter -= 2 * (j > 0 and grid[i][j - 1] == 1)

                # If there is a cell above we subtract 2 (shared side)
                perimeter -= 2 * (i > 0 and grid[i - 1][j] == 1)

    return perimeter
