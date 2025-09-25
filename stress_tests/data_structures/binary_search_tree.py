"""
@description
This script is a stress test for the standard (unbalanced) Binary Search Tree
implementation. It validates the correctness of the `BinarySearchTree` class by
comparing its behavior against a Python `set` over a large number of randomized
operations.

The test randomly performs three main operations:
1. insert(key): Adds a key to both the BST and the set.
2. delete(key): Removes a key from both data structures.
3. search(key): Checks for the existence of a key and asserts that both
   structures return the same result.

This ensures that the core logic, especially the complex cases for the `delete`
method, is implemented correctly.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.binary_search_tree import BinarySearchTree


def run_test():
    """
    Performs a stress test on the BinarySearchTree implementation.
    """
    ITERATIONS = 20000
    MAX_VAL = 5000

    bst = BinarySearchTree()
    naive_set = set()

    for i in range(ITERATIONS):
        op_type = random.randint(0, 2)
        val = random.randint(0, MAX_VAL)

        if op_type == 0:  # Insert operation
            if val not in naive_set:
                bst.insert(val)
                naive_set.add(val)
        elif op_type == 1:  # Delete operation
            if not naive_set:
                continue
            # Choose a value that exists in the set to delete
            val_to_delete = random.choice(list(naive_set))
            bst.delete(val_to_delete)
            naive_set.remove(val_to_delete)
        elif op_type == 2:  # Search operation
            res_optimized = bst.search(val)
            res_naive = val in naive_set

            assert res_optimized == res_naive, (
                f"Search failed on iteration {i} for value {val}!\n"
                f"Expected: {res_naive}, Got: {res_optimized}"
            )

    # Final verification check across the full range of values
    for val_check in range(MAX_VAL + 1):
        res_optimized = bst.search(val_check)
        res_naive = val_check in naive_set
        assert res_optimized == res_naive, (
            f"Final verification failed for value {val_check}!\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )

    print("Binary Search Tree: All tests passed!")


if __name__ == "__main__":
    run_test()
