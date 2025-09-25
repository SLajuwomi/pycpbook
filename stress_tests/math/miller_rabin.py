"""
@description
This script is a stress test for the Miller-Rabin primality test. It validates
the correctness of the `is_prime` function by comparing its results against two
sources of ground truth:
1.  A pre-computed Sieve of Eratosthenes for all numbers up to a certain limit.
    This ensures correctness for smaller numbers.
2.  A curated list of known large prime and composite numbers. This ensures
    correctness for inputs that are too large for a sieve.

The test asserts that the Miller-Rabin implementation correctly classifies all
these numbers, providing high confidence in its reliability for competitive
programming use cases.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.math.miller_rabin import is_prime
from content.math.sieve import sieve


def run_test():
    """
    Performs a stress test on the Miller-Rabin primality test implementation.
    """
    # --- Test against Sieve for smaller numbers ---
    SIEVE_LIMIT = 2000
    sieve_result = sieve(SIEVE_LIMIT)

    for i in range(SIEVE_LIMIT + 1):
        res_mr = is_prime(i)
        res_sieve = sieve_result[i]
        assert res_mr == res_sieve, (
            f"Miller-Rabin failed for number {i}!\n"
            f"Expected (from Sieve): {res_sieve}, Got: {res_mr}"
        )

    # --- Test against known large primes ---
    large_primes = [
        1000000007,
        998244353,
        2147483647,
        982451653,
        10**9 + 7,
        10**9 + 9,
        (1 << 61) - 1,
    ]
    for p in large_primes:
        assert is_prime(p), f"Miller-Rabin failed for known prime: {p}"

    # --- Test against known large composites ---
    large_composites = [
        1000000007 * 1000000009,
        998244353 * 998244353,
        4759123141 + 2,  # Known composite
        10**12,
        (1 << 61),
        341550071728321,  # A Carmichael number
    ]
    for c in large_composites:
        assert not is_prime(c), f"Miller-Rabin failed for known composite: {c}"

    print("Miller-Rabin Primality Test: All tests passed!")


if __name__ == "__main__":
    run_test()
