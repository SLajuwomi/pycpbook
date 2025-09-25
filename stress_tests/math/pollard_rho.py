import random
import sys
import os
import math

# Add project root to path to import the solution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.math.pollard_rho import factorize


def prime_sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False
    prime_numbers = [i for i, is_p in enumerate(primes) if is_p]
    return prime_numbers


def run_test():
    # Test cases: small numbers, primes, powers of primes, composed numbers
    test_cases = [
        (1, []),
        (2, [2]),
        (7, [7]),
        (131, [131]),
        (4, [2, 2]),
        (10, [2, 5]),
        (81, [3, 3, 3, 3]),
        (100, [2, 2, 5, 5]),
        (97 * 101, [97, 101]),
        (12345, [3, 5, 823]),
        (111111, [3, 7, 11, 13, 37]),
        (17 * 19 * 23 * 29, [17, 19, 23, 29]),
    ]

    for n, expected in test_cases:
        result = factorize(n)
        assert result == expected, f"Failed on n={n}. Got {result}, expected {expected}"

    # Stress test with randomly generated numbers by multiplying known primes
    small_primes = prime_sieve(1000)

    for _ in range(100):
        n = 1
        expected_factors = []
        num_factors = random.randint(2, 5)

        for _ in range(num_factors):
            p = random.choice(small_primes)
            n *= p
            expected_factors.append(p)

        expected_factors.sort()

        if n > 10**18:  # Keep numbers within a reasonable range for testing
            continue

        result = factorize(n)
        assert (
            result == expected_factors
        ), f"Failed on random n={n}. Got {result}, expected {expected_factors}"

    # Stress test with large random numbers, check if product of factors equals n
    for _ in range(50):
        n = random.randint(10**9, 10**12)
        factors = factorize(n)

        product = 1
        for f in factors:
            product *= f

        assert (
            product == n
        ), f"Product of factors does not match n. n={n}, factors={factors}, product={product}"

    # Test large primes
    large_primes = [10**9 + 7, 10**9 + 9, 998244353]
    for p in large_primes:
        result = factorize(p)
        assert result == [p], f"Failed on large prime p={p}. Got {result}"

    print("Pollard's Rho: All tests passed!")


if __name__ == "__main__":
    run_test()
