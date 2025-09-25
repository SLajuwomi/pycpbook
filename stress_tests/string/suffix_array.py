"""
@description
This script is a stress test for the Suffix Array and LCP Array construction
algorithms. It validates the correctness of `build_suffix_array` and
`build_lcp_array` by comparing their outputs against simple, brute-force
naive implementations.

The test workflow is as follows:
1.  For a number of iterations, a random string is generated.
2.  **Suffix Array Validation**:
    a. A naive suffix array is created by generating all suffixes, pairing them
       with their original indices, and sorting this list lexicographically.
    b. The `build_suffix_array` function is called.
    c. The resulting suffix array is asserted to be identical to the naively
       generated one.
3.  **LCP Array Validation**:
    a. A naive LCP array is created by iterating through the sorted suffix
       array and directly comparing adjacent suffixes character by character
       to find the length of their longest common prefix.
    b. The `build_lcp_array` function is called.
    c. The resulting LCP array is asserted to be identical to the naive one.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.string.suffix_array import build_suffix_array, build_lcp_array
from stress_tests.utilities.random_gen import random_string


def naive_build_suffix_array(s):
    """A naive O(N^2 log N) implementation for validation."""
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort(key=lambda x: x[0])
    return [index for suffix, index in suffixes]


def naive_lcp(s1, s2):
    """Calculates LCP of two strings naively."""
    l = 0
    while l < len(s1) and l < len(s2) and s1[l] == s2[l]:
        l += 1
    return l


def naive_build_lcp_array(s, sa):
    """A naive O(N^2) implementation for validation."""
    n = len(s)
    if n == 0:
        return []
    lcp = [0] * n
    for i in range(1, n):
        suffix1 = s[sa[i - 1] :]
        suffix2 = s[sa[i] :]
        lcp[i] = naive_lcp(suffix1, suffix2)
    return lcp


def run_test():
    """
    Performs a stress test on the Suffix Array and LCP Array implementations.
    """
    ITERATIONS = 100
    MAX_LEN = 200

    for i in range(ITERATIONS):
        s_len = random.randint(1, MAX_LEN)
        # Use a small alphabet to create more interesting LCPs
        s = random_string(s_len, "abc")

        # Test Suffix Array
        sa_optimized = build_suffix_array(s)
        sa_naive = naive_build_suffix_array(s)

        assert sa_optimized == sa_naive, (
            f"Suffix Array failed on iteration {i}!\n"
            f"String: '{s}'\n"
            f"Expected: {sa_naive}\n"
            f"Got: {sa_optimized}"
        )

        # Test LCP Array
        lcp_optimized = build_lcp_array(s, sa_optimized)
        lcp_naive = naive_build_lcp_array(s, sa_optimized)

        assert lcp_optimized == lcp_naive, (
            f"LCP Array failed on iteration {i}!\n"
            f"String: '{s}'\n"
            f"Suffix Array: {sa_optimized}\n"
            f"Expected: {lcp_naive}\n"
            f"Got: {lcp_optimized}"
        )

    # Test edge cases
    s_empty = ""
    assert build_suffix_array(s_empty) == []
    assert build_lcp_array(s_empty, []) == []

    s_single = "a"
    assert build_suffix_array(s_single) == [0]
    assert build_lcp_array(s_single, [0]) == [0]

    print("Suffix Array and LCP Array: All tests passed!")


if __name__ == "__main__":
    run_test()
