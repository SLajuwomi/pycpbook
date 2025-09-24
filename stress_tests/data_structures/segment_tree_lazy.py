"""
@description
This script is a stress test for the Segment Tree with lazy propagation.
It validates the correctness of the optimized `SegmentTree` class by comparing
its results against a simple, naive array-based implementation over a large
number of randomized operations.

The test randomly performs two main operations:
1. update(l, r, addval): A range update, adding a value to all elements
   in the inclusive range [l, r].
2. query(l, r): A range sum query on the inclusive range [l, r].

It asserts that the outcome of query operations is consistent between the
optimized Segment Tree and the naive solution. This is critical for catching
subtle bugs in the lazy propagation logic, range handling, and recursive updates.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.segment_tree_lazy import SegmentTree


class NaiveSolution:
    """
    A naive implementation using a simple list for validation. It supports
    the same interface as the Segment Tree but with slow, brute-force logic.
    """

    def __init__(self, arr):
        self.arr = list(arr)

    def update(self, l, r, addval):
        """Updates by iterating through the range. O(N)"""
        for i in range(l, r + 1):
            self.arr[i] += addval

    def query(self, l, r):
        """Queries by summing the slice. O(N)"""
        return sum(self.arr[l : r + 1])


def run_test():
    """
    Performs a stress test on the SegmentTree implementation.
    """
    N = 500  # Size of the array
    ITERATIONS = 5000  # Number of random operations to perform
    MAX_VAL = 1000  # Max value for array elements and update values

    initial_arr = [random.randint(-MAX_VAL, MAX_VAL) for _ in range(N)]

    seg_tree = SegmentTree(initial_arr)
    naive = NaiveSolution(initial_arr)

    for i in range(ITERATIONS):
        # 50% chance to update, 50% chance to query
        op_type = random.randint(0, 1)

        l = random.randint(0, N - 1)
        r = random.randint(l, N - 1)

        if op_type == 0:  # Update operation
            addval = random.randint(-MAX_VAL, MAX_VAL)
            seg_tree.update(l, r, addval)
            naive.update(l, r, addval)
        else:  # Query operation
            res_optimized = seg_tree.query(l, r)
            res_naive = naive.query(l, r)

            assert res_optimized == res_naive, (
                f"Query failed on iteration {i} for range [{l}, {r}]!\n"
                f"Initial Array Slice: {initial_arr[l:r+1]}\n"
                f"Expected: {res_naive}, Got: {res_optimized}"
            )

    print("Segment Tree with Lazy Propagation: All tests passed!")


if __name__ == "__main__":
    run_test()
