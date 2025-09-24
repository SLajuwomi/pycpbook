"""
@description
This script is a stress test for the 2D Fenwick Tree implementation.
It validates the correctness of the `FenwickTree2D` class by comparing its
prefix sum query results against a naive, brute-force 2D array implementation.

The test randomly performs two main operations on a grid:
1.  add(r, c, delta): A point update at cell (r, c).
2.  query(r, c): A prefix sum query for the rectangle from (0,0) to (r-1, c-1).

By asserting that the results from both the optimized and naive structures
are identical after each operation, we gain high confidence in the correctness
of the `FenwickTree2D` implementation.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.fenwick_tree_2d import FenwickTree2D


class NaiveFenwickTree2D:
    """
    A naive implementation using a simple 2D list for validation.
    It provides the same interface as FenwickTree2D but with slow,
    unambiguously correct logic.
    """

    def __init__(self, rows, cols):
        self.grid = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def add(self, r, c, delta):
        self.grid[r][c] += delta

    def query(self, r, c):
        total_sum = 0
        for i in range(r):
            for j in range(c):
                total_sum += self.grid[i][j]
        return total_sum


def run_test():
    """
    Performs a stress test on the FenwickTree2D implementation.
    """
    ROWS = 50
    COLS = 50
    ITERATIONS = 10000

    ft_2d = FenwickTree2D(ROWS, COLS)
    naive_ft_2d = NaiveFenwickTree2D(ROWS, COLS)

    for i in range(ITERATIONS):
        op_type = random.randint(0, 1)

        if op_type == 0:
            r = random.randint(0, ROWS - 1)
            c = random.randint(0, COLS - 1)
            val = random.randint(-100, 100)
            ft_2d.add(r, c, val)
            naive_ft_2d.add(r, c, val)
        else:
            r = random.randint(0, ROWS)
            c = random.randint(0, COLS)
            res_optimized = ft_2d.query(r, c)
            res_naive = naive_ft_2d.query(r, c)

            assert res_optimized == res_naive, (
                f"Query failed at (r={r}, c={c}) on iteration {i}!\n"
                f"Expected: {res_naive}, Got: {res_optimized}"
            )

    print("2D Fenwick Tree: All tests passed!")


if __name__ == "__main__":
    run_test()
