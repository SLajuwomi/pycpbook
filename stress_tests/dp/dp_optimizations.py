"""
@description
This script is a stress test for the Convex Hull Trick (CHT) example provided
in `content/dp/dp_optimizations.py`. It validates the correctness of the
optimized CHT solution by comparing its results against a naive, O(N^2)
dynamic programming solution.

The test workflow is as follows:
1.  A `naive_solution` function is defined, which solves the example problem
    using a simple nested loop, which is slow but unambiguously correct.
2.  For a number of iterations, a random test case is generated. This involves
    creating a strictly increasing array of coordinates `p` and a constant
    jump cost `C`.
3.  The problem is solved using both the optimized `convex_hull_trick_example`
    function and the `naive_solution`.
4.  The script asserts that the minimum costs calculated by both methods are
    identical.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.dp.dp_optimizations import convex_hull_trick_example


def naive_solution(p, C):
    """
    A naive O(N^2) DP solution for the example problem for validation.
    dp[i] = min_{j<i} (dp[j] + (p[i] - p[j])^2 + C)
    """
    n = len(p)
    if n <= 1:
        return 0

    dp = [0] * n
    for i in range(1, n):
        min_cost = float("inf")
        for j in range(i):
            cost = dp[j] + (p[i] - p[j]) ** 2
            min_cost = min(min_cost, cost)
        dp[i] = min_cost + C

    return dp[n - 1]


def run_test():
    """
    Performs a stress test on the Convex Hull Trick example implementation.
    """
    ITERATIONS = 200
    MAX_N = 100
    MAX_COORD_STEP = 100
    MAX_C = 1000

    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)

        # Generate a strictly increasing array of coordinates
        p = [0] * n
        current_pos = 0
        for j in range(n):
            current_pos += random.randint(1, MAX_COORD_STEP)
            p[j] = current_pos

        C = random.randint(0, MAX_C)

        res_optimized = convex_hull_trick_example(p, C)
        res_naive = naive_solution(p, C)

        assert res_optimized == res_naive, (
            f"DP Optimization (CHT) failed on iteration {i}!\n"
            f"p: {p}\n"
            f"C: {C}\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )

    print("DP Optimizations (Convex Hull Trick): All tests passed!")


if __name__ == "__main__":
    run_test()
