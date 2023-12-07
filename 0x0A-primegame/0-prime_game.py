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
    player_one_total_wins = 0
    player_two_total_wins = 0
    player_one_name = "Maria"
    player_two_name = "Ben"

    # Iterate per given number of rounds
    for i in range(x):
        num = nums[i]
        # Get the set used in the current round
        set_in_round = list(range(1, num + 1))

        # Get the prime numbers within the specified n range
        prime_numbers = get_prime_numbers_in_range(1, num)

        # We always start with player one, if we don't have
        # any prime numbers then automatically player two wins
        # the round
        if not prime_numbers:
            player_two_total_wins += 1
            continue

        # For every num in nums we must start the selection
        # with player one
        is_player_one_turn = True

        # Start iteration of the round since we have prime numbers
        while True:
            # If we don't find a prime number
            if not prime_numbers:
                if is_player_one_turn:
                    player_two_total_wins += 1
                else:
                    player_one_total_wins += 1
                break
            set_in_round = update_set_in_round(set_in_round,
                                               prime_numbers.pop(0))
            is_player_one_turn = not is_player_one_turn

    if player_one_total_wins > player_two_total_wins:
        return player_one_name
    elif player_two_total_wins > player_one_total_wins:
        return player_two_name
    return None


def update_set_in_round(set_in_round, selected_prime_number):
    """
     Args:
        set_in_round (list of ints): is an array of n numbers
        selected_prime_number (int): The selected prime number
    Return:
        String: name of the winner
    Returns new set in round with no multiple(s) of selected prime number
    """
    new_set_in_round = []
    for num in set_in_round:
        if num % selected_prime_number != 0:
            new_set_in_round.append(num)
    return new_set_in_round


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
