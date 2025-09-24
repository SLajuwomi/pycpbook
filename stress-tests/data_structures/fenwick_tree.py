"""
@description
This script is a stress test for the 1D Fenwick Tree (Binary Indexed Tree)
implementation. It validates the correctness of the optimized `FenwickTree`
class by comparing its results against a simple, naive array-based implementation
over a large number of randomized operations.

The test randomly performs two main operations:
1.  add(idx, delta): A point update on the array.
2.  query(right): A prefix sum query.

It asserts that the outcome of these operations is consistent between the
optimized Fenwick Tree and the naive solution. This ensures that the
logarithmic-time implementation is bug-free and reliable for use in contests.
"""

import sys
import os
import random

# Add the project root to the Python path to allow importing from the 'content' directory.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.fenwick_tree import FenwickTree


class NaiveFenwickTree:
    """
    A naive implementation of a data structure that supports the same
    operations as a Fenwick Tree. It uses a simple list and is correct but slow.
    This serves as the ground truth for validation.
    """

    def __init__(self, size):
        """Initializes the underlying array with zeros."""
        self.arr = [0] * size

    def add(self, idx, delta):
        """Adds a delta to an element at a specific index. O(1)"""
        self.arr[idx] += delta

    def query(self, right):
        """Calculates the prefix sum up to `right-1` by iterating. O(N)"""
        return sum(self.arr[:right])


def run_test():
    """
    Performs a stress test on the FenwickTree implementation.
    It runs a series of random updates and queries, comparing the results
    of the optimized FenwickTree class with the naive implementation.
    """
    N = 1000  # Size of the array
    ITERATIONS = 10000  # Number of random operations to perform

    ft = FenwickTree(N)
    naive_ft = NaiveFenwickTree(N)

    for i in range(ITERATIONS):
        # 50% chance to add, 50% chance to query
        op_type = random.randint(0, 1)

        if op_type == 0:  # Add operation
            idx = random.randint(0, N - 1)
            val = random.randint(-1000, 1000)
            ft.add(idx, val)
            naive_ft.add(idx, val)
        else:  # Query operation
            # Query is on the prefix [0, idx), so idx can be from 0 to N.
            idx = random.randint(0, N)
            res_optimized = ft.query(idx)
            res_naive = naive_ft.query(idx)

            assert res_optimized == res_naive, (
                f"Query failed at index {idx} on iteration {i}!\n"
                f"Expected: {res_naive}, Got: {res_optimized}"
            )

    print("Fenwick Tree: All tests passed!")


if __name__ == "__main__":
    run_test()
