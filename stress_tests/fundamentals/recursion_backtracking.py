"""
@description
This script is a stress test for the recursion and backtracking example.
It validates the correctness of the `generate_subsets` function by comparing
its output against a known-correct iterative method using bitmasks.

The test workflow is as follows:
1.  A `naive_solution` function is defined, which generates all subsets
    iteratively. It iterates from 0 to 2^N - 1. Each integer `i` in this range
    represents a unique subset, where the j-th bit of `i` being set indicates
    that the j-th element of the input array is included in the subset.
2.  For many iterations, a random list of unique numbers is generated.
3.  The power set is generated using both the recursive `generate_subsets`
    and the iterative `naive_solution`.
4.  Since the order of subsets in the final result may differ, the results
    are canonicalized by sorting each individual subset and then sorting the
    list of subsets.
5.  The script asserts that the two canonicalized power sets are identical.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.recursion_backtracking import generate_subsets
from stress_tests.utilities.random_gen import random_list


def naive_solution(nums):
    """
    Generates all subsets using an iterative bitmask approach.
    """
    n = len(nums)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(nums[j])
        subsets.append(subset)
    return subsets


def run_test():
    """
    Performs a stress test on the generate_subsets implementation.
    """
    ITERATIONS = 500
    MAX_N = 12  # Keep N small as the number of subsets is 2^N

    for i in range(ITERATIONS):
        n = random.randint(0, MAX_N)
        # Use a set to ensure unique elements, simplifying comparison
        nums = sorted(list(set(random_list(n, -100, 100))))

        res_optimized = generate_subsets(nums)
        res_naive = naive_solution(nums)

        # Canonicalize results for comparison
        # Sort each subset, then sort the list of subsets
        sorted_optimized = sorted([sorted(s) for s in res_optimized])
        sorted_naive = sorted([sorted(s) for s in res_naive])

        assert sorted_optimized == sorted_naive, (
            f"Recursion/Backtracking (Subsets) failed on iteration {i}!\n"
            f"Nums: {nums}\n"
            f"Expected: {sorted_naive}\n"
            f"Got: {sorted_optimized}"
        )

    print("Recursion / Backtracking (Subsets): All tests passed!")


if __name__ == "__main__":
    run_test()
