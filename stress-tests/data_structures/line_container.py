"""
@description
This script is a stress test for the Line Container (Convex Hull Trick)
implementation. It validates the correctness of the `LineContainer` class by
comparing its query results against a naive, brute-force implementation over a
large number of randomized operations.

The test workflow is as follows:
1.  A `NaiveLineContainer` is defined, which stores all lines and finds the
    minimum on query by checking every single line (O(N) per query).
2.  The test generates a series of lines with monotonically decreasing slopes,
    a prerequisite for the optimized `LineContainer` implementation.
3.  It randomly performs two operations:
    a. `add`: Adds a new line to both the optimized and naive containers.
    b. `query`: Asks for the minimum value at a random `x` coordinate.
4.  The results from the `query` operations are asserted to be identical. If
    they ever differ, the test fails, printing the context of the failure.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.line_container import LineContainer


class NaiveLineContainer:
    """
    A naive implementation using a simple list for validation. It finds the
    minimum by iterating through all stored lines.
    """

    def __init__(self):
        self.lines = []

    def add(self, m, c):
        self.lines.append((m, c))

    def query(self, x):
        if not self.lines:
            return float("inf")
        return min(m * x + c for m, c in self.lines)


def run_test():
    """
    Performs a stress test on the LineContainer implementation.
    """
    ITERATIONS = 20000
    MAX_ABS_SLOPE = 1000
    MAX_ABS_INTERCEPT = 10000
    MAX_ABS_X = 1000

    lc = LineContainer()
    naive_lc = NaiveLineContainer()

    current_slope = MAX_ABS_SLOPE + 1

    for i in range(ITERATIONS):
        op_type = random.randint(0, 1)

        if op_type == 0:  # Add operation
            # Generate a line with a smaller slope than the previous one
            current_slope -= random.randint(1, 10)
            m = current_slope
            c = random.randint(-MAX_ABS_INTERCEPT, MAX_ABS_INTERCEPT)

            lc.add(m, c)
            naive_lc.add(m, c)

        elif op_type == 1:  # Query operation
            if not naive_lc.lines:
                continue

            x = random.randint(-MAX_ABS_X, MAX_ABS_X)
            res_optimized = lc.query(x)
            res_naive = naive_lc.query(x)

            assert res_optimized == res_naive, (
                f"Query failed on iteration {i} for x = {x}!\n"
                f"Expected: {res_naive}, Got: {res_optimized}\n"
                f"Hull state: {lc.hull}"
            )

    print("Line Container: All tests passed!")


if __name__ == "__main__":
    run_test()
