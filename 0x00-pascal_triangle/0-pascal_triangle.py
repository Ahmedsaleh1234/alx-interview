#!/usr/bin/python3
"""
that returns a list of lists of
integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    function: reperesnets an pascal traingle
    n: is the number of rows
    return: list of lists of integers
    """

    traingle = [[1]]
    if (type(n) is not int):
        raise TypeError("n must be an intger")

    if (n <= 0):
        traingle = []

    for i in range(1, n):
        row = [1]
        for j in range(i - 1):
            row.append(traingle[-1][j] + traingle[-1][1 + j])
        row.append(1)
        traingle.append(row)
    return traingle
