"""
@description
This script is a stress test for the Polynomial Hashing implementation.
It validates the correctness of the `StringHasher` class by comparing its
O(1) substring hash query results against a simple, but slower, naive
hash computation.

The test workflow is as follows:
1.  A large random string is generated.
2.  An instance of `StringHasher` is created, which performs the O(N)
    precomputation. The randomized base and moduli are retrieved from the
    instance for the naive calculation.
3.  For a large number of iterations, a random substring range [l, r) is
    generated.
4.  The hash for this range is computed using the `StringHasher.query` method.
5.  The hash is also computed using a naive, iterative function that processes
    the substring character by character.
6.  The results from both methods are asserted to be identical for both moduli.
"""

import sys
import os
import random
import string

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.string.polynomial_hashing import StringHasher


def naive_substring_hash(sub, p, m):
    """
    A naive O(len(sub)) implementation of polynomial rolling hash for validation.
    """
    h = 0
    for char in sub:
        h = (h * p + ord(char)) % m
    return h


def run_test():
    """
    Performs a stress test on the StringHasher implementation.
    """
    N = 1000
    ITERATIONS = 5000

    s = "".join(random.choices(string.ascii_letters + string.digits, k=N))
    hasher = StringHasher(s)

    p = hasher.p
    m1 = hasher.m1
    m2 = hasher.m2

    for i in range(ITERATIONS):
        l = random.randint(0, N - 1)
        r = random.randint(l + 1, N)

        substring = s[l:r]

        h_opt1, h_opt2 = hasher.query(l, r)

        h_naive1 = naive_substring_hash(substring, p, m1)
        h_naive2 = naive_substring_hash(substring, p, m2)

        assert h_opt1 == h_naive1, (
            f"Hash mismatch for modulus 1 on iteration {i} for range [{l}, {r})!\n"
            f"Substring: '{substring}'\n"
            f"Expected: {h_naive1}, Got: {h_opt1}"
        )
        assert h_opt2 == h_naive2, (
            f"Hash mismatch for modulus 2 on iteration {i} for range [{l}, {r})!\n"
            f"Substring: '{substring}'\n"
            f"Expected: {h_naive2}, Got: {h_opt2}"
        )

    print("Polynomial Hashing: All tests passed!")


if __name__ == "__main__":
    run_test()
