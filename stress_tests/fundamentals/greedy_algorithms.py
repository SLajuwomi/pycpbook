"""
@description
This script is a stress test for the greedy algorithm example implementation.
It validates the correctness of the `activity_selection` function by comparing
its output against a correct, but slower, dynamic programming solution.

The test workflow is as follows:
1.  A `naive_solution` function is defined, which solves the activity selection
    problem using dynamic programming. After sorting activities by start time,
    it computes the maximum number of activities that can be scheduled from
    each possible starting point.
2.  For a large number of iterations, a random set of activities is generated,
    each with a random start and end time.
3.  The problem is solved using both the optimized greedy algorithm and the
    naive DP solution.
4.  The script asserts that the maximum number of activities found by both
    methods are identical.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.greedy_algorithms import activity_selection


def naive_solution(activities):
    """
    A correct O(N^2) DP solution for the activity selection problem.
    """
    n = len(activities)
    if n == 0:
        return 0

    # Sort activities by their start times
    activities.sort(key=lambda x: x[0])

    dp = [1] * n
    for i in range(n - 2, -1, -1):
        max_val = 0
        for j in range(i + 1, n):
            if activities[j][0] >= activities[i][1]:  # Non-overlapping
                max_val = max(max_val, dp[j])
        dp[i] = 1 + max_val

    return max(dp) if dp else 0


def run_test():
    """
    Performs a stress test on the greedy_algorithms implementation.
    """
    ITERATIONS = 500
    MAX_N = 50
    MAX_TIME = 200

    for i in range(ITERATIONS):
        n = random.randint(0, MAX_N)
        activities = []
        for _ in range(n):
            start = random.randint(0, MAX_TIME - 1)
            end = random.randint(start + 1, MAX_TIME)
            activities.append((start, end))

        # Create copies of the list as they are sorted in-place
        activities_for_greedy = list(activities)
        activities_for_naive = list(activities)

        res_optimized = activity_selection(activities_for_greedy)
        res_naive = naive_solution(activities_for_naive)

        assert res_optimized == res_naive, (
            f"Greedy Algorithms (Activity Selection) failed on iteration {i}!\n"
            f"Activities: {activities}\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )

    print("Greedy Algorithms (Activity Selection): All tests passed!")


if __name__ == "__main__":
    run_test()
