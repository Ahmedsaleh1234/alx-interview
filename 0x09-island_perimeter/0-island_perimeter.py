#!/usr/bin/python3
"""" 0-island_perimeter.py"""


def island_perimeter(grid):
    """
    Function:  that returns the perimeter of the island described in grid
    grid: is a list of list of integers
    """
    p = 0
    conn = 0
    rows_lengt = len(grid)
    column_length = len(grid[0])
    for i in range(0, rows_lengt):
        for j in range(0, column_length):
            if grid[i][j] == 1:
                p += 4
                if i != 0 and grid[i - 1][j] == 1:
                    conn += 2
                if j != 0 and grid[i][j - 1] == 1:
                    conn += 2
    solution = p - conn
    return solution
