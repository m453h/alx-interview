#!/usr/bin/python3
"""
This module contains the function that solves the making change problem
"""


def makeChange(coins, total):
    """
       Determines the fewest number of coins needed to meet a given
       amount total

       Args:
            coins (List[int]): A list of the values of the coins
            total: The total amount needing change
       Return: (int) The total number of coins that need to be returned
                -1 if total cannot be met by any number of coins present

    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    number_of_coins = 0
    i = 0
    while True:
        if i < len(coins):
            if coins[i] <= total:
                total -= coins[i]
                number_of_coins += 1
            else:
                i += 1
        else:
            break
    if total != 0:
        number_of_coins = -1
    return number_of_coins
