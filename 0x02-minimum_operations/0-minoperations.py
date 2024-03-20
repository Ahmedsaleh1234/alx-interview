#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Function: that calculates the fewest number of operations
    n: exactly n H characters in the file.
    Return: The sum of operation
    """
    if n < 2:
        return 0
    save_op = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n = n / i
                save_op.append(i)
    return sum(save_op)
