#!/usr/bin/python3
"""Defines a function that determines the winner of the prime game"""


def isWinner(x, nums):
    """
    Return the name of the winner of the prime game
    Args:
        x (int): number of rounds
        nums (list of ints): is an array of n numbers
    Return:
        String: name of the winner
    """
    if not isinstance(x, int) or not isinstance(nums, list):
        return None

    maria_total_wins = 0
    ben_total_wins = 0

    # Iterate per given number of rounds
    for i in range(min(x, len(nums))):
        num = nums[i]
        # Get the set used in the current round
        set_in_round = list(range(1, num + 1))

        while True:
            # Start by allowing Maria to pick a number
            number_picked_by_maria = pick_prime_number(set_in_round)

            # If Maria can't make a selection the Ben wins this round
            if number_picked_by_maria is None:
                ben_total_wins += 1
                break

            # If Maria picks a number then remove it and its multiples and
            # then let Ben have his pick
            set_in_round[:] = \
                [num for num in set_in_round
                 if num % number_picked_by_maria != 0]

            # Ben picks the number after Maria
            number_picked_by_ben = pick_prime_number(set_in_round)

            # If Ben can't pick a number then Maria wins this round
            if number_picked_by_ben is None:
                maria_total_wins += 1
                break

            # If Ben picks a number remove it and its multiples in
            # and let Maria have another pick in the next iteration
            set_in_round[:] = \
                [num for num in set_in_round
                 if num % number_picked_by_ben != 0]

    if maria_total_wins > ben_total_wins:
        return "Maria"
    elif ben_total_wins > maria_total_wins:
        return "Ben"
    return None


def pick_prime_number(nums):
    """
    Picks a prime number in an optimal manner
    Args:
        nums (list of ints): is an array of n numbers
    Return:
        int: Prime number picked by player
    """
    for num in nums:
        if is_prime(num):
            return num
    return None


def is_prime(n):
    """
    Returns True if n is prime, else False
     Args:
        n (int): Start range to look for prime number
    Return:
        (boolean): True if number is prime, ELSE false
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_prime_numbers_in_range(start, end):
    """
    Returns a list of prime numbers between start and end (inclusive)
    Args:
        start (int): Start range to look for prime number
        end (int): End range (inclusive) to look for prime number
    Return:
        (list): List of prime number within specified range
    """
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes
