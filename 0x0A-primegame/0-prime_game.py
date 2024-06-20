#!/usr/bin/python3

def isWinner(x, nums):
    """Function that performs prime game"""
    player1_wins = 0
    player2_wins = 0
    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if all(i %
                          j != 0 for j in range(2, int(i**0.5) + 1)))
        if prime_count % 2 == 0:
            player2_wins += 1
        else:
            player1_wins += 1
    if player1_wins > player2_wins:
        return "Maria"
    elif player2_wins > player1_wins:
        return "Ben"
    else:
        return None
