#!/usr/bin/python3
"""
Contains isPrime and isWinner Functions
"""


def is_prime(n):
    """
    Returns prime numbers between 1 and n
    (sieve of Eratosthenes)
    """
    prime_nums = []
    sieve = [True] * (n + 1)

    for num in range(2, n + 1):
        if sieve[num]:
            prime_nums.append(num)
            for i in range(num, n + 1, num):
                sieve[i] = False

    return prime_nums


def is_winner(x, nums):
    """Function to determine the winner of the Prime game"""
    if x is None or nums is None or x == 0 or not nums:
        return None

    maria_count = 0
    ben_count = 0

    for n in range(x):
        prime_nums = is_prime(nums[n])
        if len(prime_nums) % 2 != 0:
            maria_count += 1
        else:
            ben_count += 1

    if maria_count > ben_count:
        return "Maria"
    elif ben_count > maria_count:
        return "Ben"
    else:
        return None
