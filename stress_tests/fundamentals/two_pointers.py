"""
@description
This script is a stress test for the Two Pointers / Sliding Window example
implementation. It validates the correctness of the `longest_substring_with_k_distinct`
function by comparing its results against a naive, O(N^2) brute-force solution.

The test workflow is as follows:
1.  A `naive_solution` function is defined, which finds the longest valid
    substring by iterating through all possible substrings and checking the
    number of distinct characters for each one.
2.  For a large number of iterations, a random string and a random integer `k`
    are generated.
3.  The problem is solved using both the optimized sliding window function and
    the naive solution.
4.  The script asserts that the lengths of the substrings found by both methods
    are identical.
"""

import sys
import os
import random
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.two_pointers import longest_substring_with_k_distinct
from stress_tests.utilities.random_gen import random_string


def naive_solution(s, k):
    """
    A naive O(N^2) solution for finding the longest substring with at most k
    distinct characters.
    """
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i : j + 1]
            if len(set(substring)) <= k:
                max_len = max(max_len, len(substring))
    return max_len


def run_test():
    """
    Performs a stress test on the two_pointers implementation.
    """
    ITERATIONS = 500
    MAX_LEN = 200
    ALPHABET = "abcdef"

    for i in range(ITERATIONS):
        s_len = random.randint(0, MAX_LEN)
        s = random_string(s_len, ALPHABET)
        k = random.randint(0, len(ALPHABET) + 1)

        res_optimized = longest_substring_with_k_distinct(s, k)
        res_naive = naive_solution(s, k)

        assert res_optimized == res_naive, (
            f"Two Pointers/Sliding Window failed on iteration {i}!\n"
            f"String: '{s}'\n"
            f"k: {k}\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )

    print("Two Pointers / Sliding Window: All tests passed!")


if __name__ == "__main__":
    run_test()
