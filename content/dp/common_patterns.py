"""
Author: PyCPBook Community
Source: Introduction to Algorithms (CLRS), CP-Algorithms
Description: This file provides implementations for three classic dynamic
programming patterns that are foundational in competitive programming: Longest
Increasing Subsequence (LIS), Longest Common Subsequence (LCS), and the 0/1
Knapsack problem.

Longest Increasing Subsequence (LIS):
Given a sequence of numbers, the goal is to find the length of the longest
subsequence that is strictly increasing. The standard DP approach takes $O(N^2)$
time. This file implements a more efficient $O(N \\log N)$ solution. The
algorithm maintains an auxiliary array (e.g., `tails`) where `tails[i]` stores
the smallest tail of all increasing subsequences of length `i+1`. When
processing a new number `x`, we find the smallest tail that is greater than or
equal to `x`. If `x` is larger than all tails, it extends the LIS. Otherwise, it
replaces the tail it was compared against, potentially allowing for a better
solution later. This search and replacement is done using binary search.

Longest Common Subsequence (LCS):
Given two sequences, the goal is to find the length of the longest subsequence
present in both of them. The standard DP solution uses a 2D table `dp[i][j]`
which stores the length of the LCS of the prefixes `s1[0...i-1]` and
`s2[0...j-1]`. The recurrence relation is:
- If `s1[i-1] == s2[j-1]`, then `dp[i][j] = 1 + dp[i-1][j-1]`.
- Otherwise, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

0/1 Knapsack Problem:
Given a set of items, each with a weight and a value, determine the number of
each item to include in a collection so that the total weight is less than or
equal to a given limit and the total value is as large as possible. In the 0/1
version, you can either take an item or leave it. The standard solution uses a
DP table `dp[i][w]` representing the maximum value using items up to `i` with a
weight limit of `w`. This can be optimized in space to a 1D array where `dp[w]`
is the maximum value for a capacity of `w`.

Time:
- LIS: $O(N \\log N)$
- LCS: $O(N \\cdot M)$ where N and M are the lengths of the sequences.
- 0/1 Knapsack: $O(N \\cdot W)$ where N is number of items, W is capacity.
Space:
- LIS: $O(N)$
- LCS: $O(N \\cdot M)$
- 0/1 Knapsack: $O(W)$ (space-optimized)
Status: Stress-tested
"""

import bisect


def longest_increasing_subsequence(arr):
    """
    Finds the length of the longest increasing subsequence in O(N log N).
    """
    if not arr:
        return 0

    tails = []
    for num in arr:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)


def longest_common_subsequence(s1, s2):
    """
    Finds the length of the longest common subsequence in O(N*M).
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem with space optimization.
    """
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]
