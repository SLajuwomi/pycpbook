"""
@description
This script is a stress test for Manacher's algorithm. It validates the
correctness of the `manacher` function by comparing its results against a
naive, brute-force approach for finding the longest palindromic substring.

The test workflow is as follows:
1.  A `naive_longest_palindrome` function is defined. It finds the longest
    palindromic substring by iterating through all possible substrings, checking
    if each is a palindrome, and keeping track of the longest one. This is
    computationally expensive but unambiguously correct.
2.  For many iterations, a random string is generated.
3.  The `manacher` function is called to find the longest palindrome in O(N) time.
4.  The naive function is also called on the same string.
5.  The script asserts that the length of the palindrome returned by `manacher`
    is equal to the length of the one found by the naive method. It also
    verifies that the returned string is indeed a palindrome.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.string.manacher import manacher
from stress_tests.utilities.random_gen import random_string


def is_palindrome(s):
    """Checks if a string is a palindrome."""
    return s == s[::-1]


def naive_longest_palindrome(s):
    """A naive O(N^3) implementation for finding the longest palindromic substring."""
    n = len(s)
    if n == 0:
        return ""
    longest_pal = ""
    for i in range(n):
        for j in range(i, n):
            substring = s[i : j + 1]
            if is_palindrome(substring):
                if len(substring) > len(longest_pal):
                    longest_pal = substring
    return longest_pal


def run_test():
    """
    Performs a stress test on the Manacher's algorithm implementation.
    """
    ITERATIONS = 200
    MAX_LEN = 200
    ALPHABET = "abc"

    for i in range(ITERATIONS):
        s_len = random.randint(0, MAX_LEN)
        s = random_string(s_len, ALPHABET)

        res_optimized = manacher(s)
        res_naive = naive_longest_palindrome(s)

        assert is_palindrome(
            res_optimized
        ), f"Manacher's did not return a palindrome on iteration {i}!\nString: '{s}'\nGot: '{res_optimized}'"

        assert len(res_optimized) == len(res_naive), (
            f"Manacher's algorithm failed on iteration {i}!\n"
            f"String: '{s}'\n"
            f"Expected length: {len(res_naive)} (from '{res_naive}')\n"
            f"Got length: {len(res_optimized)} (from '{res_optimized}')"
        )

    print("Manacher's Algorithm: All tests passed!")


if __name__ == "__main__":
    run_test()
