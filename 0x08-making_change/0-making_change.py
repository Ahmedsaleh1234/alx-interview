#!/usr/bin/env python3
"""0-making_change.py"""


def makeChange(coins, total):
    """
    pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total.
    """
    coins.sort(reverse=True)
    count = 0
    coin = 0
    if total <= 0:
        return 0
    for i in coins:
        while coin < total:
            coin += i
            count += 1
            if coin == total:
                return count
        coin -= i
        count -= 1
    return -1
