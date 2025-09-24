"""
@description
This script is a stress test for the Sparse Table implementation.
It validates the correctness of the `SparseTable` class, designed for
fast Range Minimum Queries (RMQ), by comparing its results against a
simple, naive solution over a large number of randomized queries.

The test workflow is as follows:
1. A large random array of integers is generated.
2. An instance of `SparseTable` is created and precomputes its lookup table
   based on the random array.
3. For a large number of iterations, a random range [l, r] is generated.
4. A query for this range is performed on the `SparseTable` instance.
5. A query for the same range is performed using a naive, brute-force
   method (iterating through the array slice and finding the minimum).
6. The results from both methods are asserted to be identical.

This process ensures that the precomputation logic and the O(1) query
mechanism of the Sparse Table are correct and handle all range cases properly.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.sparse_table import SparseTable


class NaiveSolution:
    """
    A naive implementation using a simple list for validation. It finds the
    range minimum by iterating through the specified slice, providing a
    correct baseline for comparison.
    """

    def __init__(self, arr):
        self.arr = list(arr)

    def query(self, l, r):
        """Queries the minimum by checking every element in the slice. O(N)"""
        if l > r:
            return float("inf")
        return min(self.arr[l : r + 1])


def run_test():
    """
    Performs a stress test on the SparseTable implementation.
    """
    N = 1000  # Size of the array
    ITERATIONS = 10000  # Number of random queries to perform
    MAX_VAL = 10**9  # Max value for array elements

    initial_arr = [random.randint(-MAX_VAL, MAX_VAL) for _ in range(N)]

    sparse_table = SparseTable(initial_arr)
    naive = NaiveSolution(initial_arr)

    for i in range(ITERATIONS):
        l = random.randint(0, N - 1)
        r = random.randint(l, N - 1)

        res_optimized = sparse_table.query(l, r)
        res_naive = naive.query(l, r)

        assert res_optimized == res_naive, (
            f"Query failed on iteration {i} for range [{l}, {r}]!\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )

    print("Sparse Table: All tests passed!")


if __name__ == "__main__":
    run_test()
