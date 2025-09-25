"""
@description
This script is a stress test for the Number Theoretic Transform (NTT) based
polynomial multiplication. It validates the correctness of the `multiply`
function from the `ntt` module by comparing its results against a naive,
brute-force O(N^2) polynomial multiplication algorithm.

The test workflow is as follows:
1.  A `naive_multiply` function is defined, which computes the product of two
    polynomials using a simple double loop.
2.  For a number of iterations, two random polynomials with random coefficients
    are generated.
3.  The polynomials are multiplied using both the optimized `multiply` function
    (which uses NTT) and the `naive_multiply` function.
4.  The coefficients of the resulting polynomials are compared. The test
    asserts that they are identical.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.math.ntt import multiply, MOD
from stress_tests.utilities.random_gen import random_list


def naive_multiply(a, b):
    """
    A naive O(N^2) implementation of polynomial multiplication for validation.
    """
    n = len(a)
    m = len(b)
    if n == 0 or m == 0:
        return []

    res = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            res[i + j] = (res[i + j] + a[i] * b[j]) % MOD
    return res


def run_test():
    """
    Performs a stress test on the NTT polynomial multiplication implementation.
    """
    ITERATIONS = 100
    MAX_DEGREE = 256
    MAX_COEFF = 10**9

    for i in range(ITERATIONS):
        deg1 = random.randint(0, MAX_DEGREE)
        deg2 = random.randint(0, MAX_DEGREE)

        poly1 = random_list(deg1 + 1, 0, MAX_COEFF)
        poly2 = random_list(deg2 + 1, 0, MAX_COEFF)

        res_optimized_full = multiply(poly1, poly2)
        res_naive = naive_multiply(poly1, poly2)

        # The optimized version may have trailing zeros due to padding
        # Trim them for comparison
        res_optimized = res_optimized_full[: len(res_naive)]

        assert res_optimized == res_naive, (
            f"NTT multiplication failed on iteration {i}!\n"
            f"Poly1 (deg {deg1}): {poly1}\n"
            f"Poly2 (deg {deg2}): {poly2}\n"
            f"Expected: {res_naive}\n"
            f"Got: {res_optimized}"
        )

    # Test edge cases
    res_mul = multiply([1, 1], [1, 1])
    assert res_mul[:3] == [1, 2, 1]

    res_mul = multiply([5], [10])
    assert res_mul[:1] == [50]

    assert multiply([], [1, 2, 3]) == []
    assert multiply([1, 2, 3], []) == []

    print("NTT (Number Theoretic Transform): All tests passed!")


if __name__ == "__main__":
    run_test()
