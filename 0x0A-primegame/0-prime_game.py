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
    # Add checks to avoid index out of range problems
    # and unnecessary processes for no rounds
    if not x or not nums or x > len(nums):
        return None

    maria_total_wins = 0
    ben_total_wins = 0

    # Iterate per given number of rounds
    for i in range(x):
        num = nums[i]
        # Get the prime numbers within the specified n range
        prime_numbers_count = len(get_prime_numbers_in_range(1, num))

        # The trick is whenever the prime numbers are even in our range
        # Then Player#1 will always have the last pick and win the round
        # Otherwise it will always favour Player#2
        if prime_numbers_count % 2 == 0:
            ben_total_wins += 1
        else:
            maria_total_wins += 1

    if maria_total_wins > ben_total_wins:
        return "Maria"
    elif ben_total_wins > maria_total_wins:
        return "Ben"
    return None



def get_prime_numbers_in_range(start, end):
    """
    Returns a list of prime numbers between start and end (inclusive)
    Args:
        start (int): Start range to look for prime number
        end (int): End range (inclusive) to look for prime number
    Return:
        (list): List of prime number within specified range
    """
    def is_prime(number):
        """
        Returns True if n is prime, else False
         Args:
            number (int): Start range to look for prime number
        Return:
            (boolean): True if number is prime, ELSE false
        """
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes
