#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    mariaWinsCount = 0
    benWinsCount = 0

    primesSet = primes_in_range(max(nums))

    for num in nums:
        roundsSet = list(range(1, num + 1))

        if num not in primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        for prime in primesSet:
            if prime > num:
                break

            roundsSet = [x for x in roundsSet if x % prime != 0]

            isMariaTurns = not isMariaTurns

        if isMariaTurns:
            benWinsCount += 1
        else:
            mariaWinsCount += 1

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"
    elif mariaWinsCount < benWinsCount:
        return "Winner: Ben"
    else:
        return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(n):
    """Returns a set of prime numbers up to n."""
    primes = set()
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    for i in range(2, n + 1):
        if sieve[i]:
            primes.add(i)

    return primes
