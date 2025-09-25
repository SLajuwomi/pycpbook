"""
@description
This script is a stress test for the 1D and 2D prefix sum implementations.
It validates the correctness of the `build_prefix_sum_1d` and
`build_prefix_sum_2d` functions by comparing their returned query functions
against naive, brute-force summation over random ranges.

The test workflow includes:
1.  A 1D test that generates a random array, builds the prefix sum query
    function, and then performs thousands of random range sum queries,
    validating each result against Python's `sum(arr[l:r])`.
2.  A 2D test that generates a random grid, builds the 2D prefix sum query
    function, and then performs thousands of random rectangular sum queries,
    validating each result against a naive double-loop summation.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.prefix_sums import build_prefix_sum_1d, build_prefix_sum_2d
from stress_tests.utilities.random_gen import random_list


def test_1d():
    N = 500
    ITERATIONS = 5000
    MAX_VAL = 1000

    arr = random_list(N, -MAX_VAL, MAX_VAL)
    query_optimized = build_prefix_sum_1d(arr)

    for i in range(ITERATIONS):
        left = random.randint(0, N)
        right = random.randint(left, N)

        res_optimized = query_optimized(left, right)
        res_naive = sum(arr[left:right])

        assert res_optimized == res_naive, (
            f"1D Prefix Sum failed on iteration {i} for range [{left}, {right})!\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )


def test_2d():
    ROWS, COLS = 50, 50
    ITERATIONS = 5000
    MAX_VAL = 100

    grid = [random_list(COLS, -MAX_VAL, MAX_VAL) for _ in range(ROWS)]
    query_optimized = build_prefix_sum_2d(grid)

    for i in range(ITERATIONS):
        r1 = random.randint(0, ROWS)
        r2 = random.randint(r1, ROWS)
        c1 = random.randint(0, COLS)
        c2 = random.randint(c1, COLS)

        res_optimized = query_optimized(r1, c1, r2, c2)

        res_naive = 0
        for r in range(r1, r2):
            for c in range(c1, c2):
                res_naive += grid[r][c]

        assert res_optimized == res_naive, (
            f"2D Prefix Sum failed on iteration {i} for rect ({r1},{c1}) to ({r2},{c2})!\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )


def run_test():
    test_1d()
    test_2d()
    print("Prefix Sums: All tests passed!")


if __name__ == "__main__":
    run_test()
