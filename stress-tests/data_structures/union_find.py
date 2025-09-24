"""
@description
This script is a stress test for the Union-Find (Disjoint Set Union) data
structure implementation. It validates the correctness of the optimized
UnionFind class by comparing its behavior against a simple, naive
implementation over a large number of randomized operations.

The test performs two main types of operations randomly:
1. Union: Merges the sets of two random elements.
2. Find (Connectivity Check): Checks if two random elements belong to the same set.

It asserts that the outcome of these operations is consistent between the
optimized and naive versions, ensuring the optimizations (path compression and
union by size) do not introduce bugs.
"""

import sys
import os
import random

# Add the project root to the Python path to allow importing from the 'content' directory.
# This makes the script runnable from the project root (e.g., via `python build.py test`).
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.union_find import UnionFind


class NaiveUnionFind:
    """
    A simple, slow, but correct implementation of Union-Find for testing purposes.
    It uses a list where parent[i] stores the representative of the set.
    Union operations are slow (O(N)) because they require a full scan, but this
    makes them easy to verify.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.n = n

    def find(self, i):
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Re-label all elements from one set to the other.
            for k in range(self.n):
                if self.parent[k] == root_j:
                    self.parent[k] = root_i
            return True
        return False


def run_test():
    """
    Performs a stress test on the UnionFind implementation.
    It runs a series of random union and find operations and compares the
    results of the optimized UnionFind class with a naive, correct implementation.
    """
    N = 500  # Number of elements in the set.
    ITERATIONS = 5000  # Number of random operations to perform.

    uf = UnionFind(N)
    naive_uf = NaiveUnionFind(N)

    for i in range(ITERATIONS):
        # 50% chance to do a union, 50% chance to do a find/connectivity check.
        op_type = random.randint(0, 1)

        u = random.randint(0, N - 1)
        v = random.randint(0, N - 1)

        if op_type == 0:  # Union operation
            # Perform union on both structures and check if they agree on whether a merge happened.
            res_optimized = uf.union(u, v)
            res_naive = naive_uf.union(u, v)

            assert res_optimized == res_naive, (
                f"Union operation mismatch for ({u}, {v})! "
                f"Expected: {res_naive}, Got: {res_optimized}"
            )

        elif op_type == 1:  # Find operation (check for connectivity)
            # Two elements are in the same set if their roots (representatives) are the same.
            in_same_set_optimized = uf.find(u) == uf.find(v)
            in_same_set_naive = naive_uf.find(u) == naive_uf.find(v)

            assert in_same_set_optimized == in_same_set_naive, (
                f"Connectivity check failed for ({u}, {v})! "
                f"Expected: {in_same_set_naive}, Got: {in_same_set_optimized}"
            )

    # After all random operations, do a final comprehensive check.
    # This ensures the final state of all components is identical.
    for i in range(N):
        for j in range(i, N):
            same_opt = uf.find(i) == uf.find(j)
            same_naive = naive_uf.find(i) == naive_uf.find(j)
            assert (
                same_opt == same_naive
            ), f"Final verification failed for ({i}, {j})! Expected {same_naive}, Got {same_opt}"

    print("Union-Find: All tests passed!")


if __name__ == "__main__":
    run_test()
