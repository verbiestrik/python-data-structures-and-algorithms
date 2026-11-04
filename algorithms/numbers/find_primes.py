"""
Find all prime numbers up to a given integer.

Problem description
-------------------
Given an integer n, return a list containing all prime numbers between
2 and n, inclusive.

Approach
--------
Use the Sieve of Eratosthenes.

1. Create a boolean list indicating whether each number is potentially prime.
2. Initially, mark every number as prime, except 0 and 1.
3. Starting at 2, iterate through the numbers up to sqrt(n).
4. If a number is still marked as prime, mark all its multiples as
   non-prime, starting at its square.
5. Return all numbers that remain marked as prime.

Complexity analysis
-------------------
Let n represent the upper limit.

- Time complexity: O(n log log n), using the Sieve of Eratosthenes.
- Auxiliary space complexity: O(n), for the boolean list.

Python alternatives
-------------------
- bytearray can replace the boolean list to reduce memory consumption.
- math.isqrt(n) provides an exact integer square root if an explicit
  square-root bound is preferred.
- range() efficiently generates the multiples that need to be marked.
"""


def find_primes(n: int) -> list[int]:
    """Return all prime numbers up to n, inclusive."""

    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n < 0:
        raise ValueError("Input must be non-negative.")

    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    i = 2

    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

        i += 1

    return [i for i in range(2, n + 1) if is_prime[i]]
