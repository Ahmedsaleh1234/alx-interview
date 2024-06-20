#!/usr/bin/python3
"""Program that performs prime game"""


def isWinner(x, nums):
    """Function that performs prime game"""
    player1 = 0
    player2 = 0
    if not nums or x < 1:
        return None
    for i in nums:
        if (i % 2 == 0 or i == 1) and (i != 2 or i != 3):
            player2 += 1
        else:
            player1 += 1
    if player1 > player2:
        return 'Maria'
    else:
        return 'Ben'
    return None
