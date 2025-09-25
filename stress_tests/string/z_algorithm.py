"""
@description
This script is a stress test for the Z-algorithm implementation. It validates
the correctness of the `z_function` by comparing its output against a simple,
brute-force naive implementation over a large number of randomized strings.

The test workflow is as follows:
1.  A `naive_z_function` is defined, which computes the Z-array in O(N^2) by
    directly comparing the string with each of its suffixes. This serves as the
    ground truth.
2.  For a large number of iterations, a random string is generated.
3.  The Z-array is computed for this string using both the optimized `z_function`
    from the content library and the `naive_z_function`.
4.  The script asserts that the two resulting arrays are identical. If they ever
    differ, the test fails and prints the context of the failure.

This process ensures that the linear-time Z-algorithm implementation is correct
and handles all cases as expected.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.string.z_algorithm import z_function
from stress_tests.utilities.random_gen import random_string


def naive_z_function(s):
    """
    A naive O(N^2) implementation of the Z-algorithm for validation.
    """
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    for i in range(1, n):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z


def run_test():
    """
    Performs a stress test on the Z-algorithm implementation.
    """
    ITERATIONS = 500
    MAX_LEN = 1000

    for i in range(ITERATIONS):
        s_len = random.randint(1, MAX_LEN)
        # Use a small alphabet to create more interesting LCPs
        s = random_string(s_len, "abcde")

        res_optimized = z_function(s)
        res_naive = naive_z_function(s)

        assert res_optimized == res_naive, (
            f"Z-algorithm failed on iteration {i}!\n"
            f"String: '{s[:100]}...'\n"
            f"Expected: {res_naive}\n"
            f"Got: {res_optimized}"
        )

    # Test edge cases
    assert z_function("") == [], "Edge case: empty string failed"
    assert z_function("a") == [0], "Edge case: single character string failed"
    assert z_function("aaaaa") == [0, 4, 3, 2, 1], "Edge case: all same characters"
    assert z_function("abacaba") == [0, 0, 1, 0, 3, 0, 1], "Edge case: standard example"

    print("Z-Algorithm: All tests passed!")


if __name__ == "__main__":
    run_test()
