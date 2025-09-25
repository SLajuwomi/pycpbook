"""
@description
This script is a stress test for the Sieve of Eratosthenes implementation.
It validates the correctness of the `sieve` function by comparing its output
against a simple, brute-force primality test for every number up to a given
limit.

The test workflow is as follows:
1.  A `is_prime_naive` function is defined, which checks for primality by
    trial division up to the square root of the number. This is slow but
    unambiguously correct.
2.  The `sieve` function is called to generate a boolean array of primes up
    to a specified limit (e.g., 2000).
3.  The script then iterates from 0 to the limit. For each number `i`, it
    compares the result from the sieve (`sieve_result[i]`) with the result
    from the naive primality test (`is_prime_naive(i)`).
4.  If any discrepancy is found, an assertion fails, indicating an error in
    the sieve implementation.
"""

import sys
import os
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.math.sieve import sieve


def is_prime_naive(n):
    """
    A simple, correct primality test for validation.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def run_test():
    """
    Performs a stress test on the Sieve of Eratosthenes implementation.
    """
    LIMIT = 2000

    sieve_result = sieve(LIMIT)

    assert (
        len(sieve_result) == LIMIT + 1
    ), f"Sieve result has incorrect length. Expected {LIMIT + 1}, Got {len(sieve_result)}"

    for i in range(LIMIT + 1):
        res_optimized = sieve_result[i]
        res_naive = is_prime_naive(i)

        assert res_optimized == res_naive, (
            f"Sieve primality check failed for number {i}!\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )

    print("Sieve of Eratosthenes: All tests passed!")


if __name__ == "__main__":
    run_test()
