"""
@description
This script is a stress test for the classic dynamic programming patterns
implemented in `content/dp/common_patterns.py`. It validates the correctness
of the optimized LIS, LCS, and Knapsack functions by comparing their results
against naive, recursive, brute-force solutions.

The test includes:
- `test_lis()`: Compares the O(N log N) LIS solution against a simple O(N^2) DP solution.
- `test_lcs()`: Compares the O(N*M) LCS solution against a naive recursive solution.
- `test_knapsack()`: Compares the space-optimized O(N*W) Knapsack solution
  against a naive recursive solution.

Each test function generates a large number of randomized inputs to ensure
the implementations are robust and correct across a wide range of scenarios.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.dp.common_patterns import (
    longest_increasing_subsequence,
    longest_common_subsequence,
    knapsack_01,
)


# --- Naive Solutions for Validation ---


def naive_lis(arr):
    n = len(arr)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if dp else 0


def naive_lcs(s1, s2):
    memo = {}

    def solve(i, j):
        if i == len(s1) or j == len(s2):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        if s1[i] == s2[j]:
            res = 1 + solve(i + 1, j + 1)
        else:
            res = max(solve(i + 1, j), solve(i, j + 1))
        memo[(i, j)] = res
        return res

    return solve(0, 0)


def naive_knapsack(weights, values, capacity):
    memo = {}
    n = len(weights)

    def solve(i, w):
        if i == n or w == 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]

        # Don't include item i
        res = solve(i + 1, w)
        # Include item i if it fits
        if weights[i] <= w:
            res = max(res, values[i] + solve(i + 1, w - weights[i]))

        memo[(i, w)] = res
        return res

    return solve(0, capacity)


# --- Test Functions ---


def test_lis():
    ITERATIONS = 500
    MAX_N = 100
    MAX_VAL = 200

    for i in range(ITERATIONS):
        n = random.randint(0, MAX_N)
        arr = [random.randint(1, MAX_VAL) for _ in range(n)]

        res_opt = longest_increasing_subsequence(arr)
        res_naive = naive_lis(arr)

        assert res_opt == res_naive, (
            f"LIS failed on iteration {i}!\n"
            f"Array: {arr}\n"
            f"Expected: {res_naive}, Got: {res_opt}"
        )


def test_lcs():
    ITERATIONS = 500
    MAX_N = 50
    MAX_M = 50
    MAX_VAL = 20

    for i in range(ITERATIONS):
        n = random.randint(0, MAX_N)
        m = random.randint(0, MAX_M)
        s1 = [random.randint(1, MAX_VAL) for _ in range(n)]
        s2 = [random.randint(1, MAX_VAL) for _ in range(m)]

        res_opt = longest_common_subsequence(s1, s2)
        res_naive = naive_lcs(s1, s2)

        assert res_opt == res_naive, (
            f"LCS failed on iteration {i}!\n"
            f"s1: {s1}\ns2: {s2}\n"
            f"Expected: {res_naive}, Got: {res_opt}"
        )


def test_knapsack():
    ITERATIONS = 500
    MAX_N = 20
    MAX_W = 100
    MAX_VAL = 100

    for i in range(ITERATIONS):
        n = random.randint(0, MAX_N)
        capacity = random.randint(0, MAX_W)
        weights = [random.randint(1, MAX_W // 2) for _ in range(n)]
        values = [random.randint(1, MAX_VAL) for _ in range(n)]

        res_opt = knapsack_01(weights, values, capacity)
        res_naive = naive_knapsack(weights, values, capacity)

        assert res_opt == res_naive, (
            f"Knapsack failed on iteration {i}!\n"
            f"Weights: {weights}\nValues: {values}\nCapacity: {capacity}\n"
            f"Expected: {res_naive}, Got: {res_opt}"
        )


def run_test():
    test_lis()
    test_lcs()
    test_knapsack()
    print("Common DP Patterns: All tests passed!")


if __name__ == "__main__":
    run_test()
