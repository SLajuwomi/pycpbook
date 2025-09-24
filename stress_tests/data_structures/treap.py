"""
@description
This script is a stress test for the Treap (randomized balanced binary search tree)
implementation. It validates the correctness of the `Treap` class by comparing
its behavior against a simple, correct data structure (a Python `set`) over a
large number of randomized operations.

The test randomly performs three main operations:
1. insert(key): Adds a key to the data structure.
2. delete(key): Removes a key from the data structure.
3. search(key): Checks for the existence of a key.

After each operation, it asserts that the `search` result is consistent between
the `Treap` and the `set`. This ensures that the complex `split` and `merge`
logic underlying the Treap's `insert` and `delete` methods works correctly.
The test also keeps track of the elements present to ensure valid operations
(e.g., deleting existing elements).
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.treap import Treap


def run_test():
    """
    Performs a stress test on the Treap implementation.
    """
    ITERATIONS = 20000
    MAX_VAL = 5000

    treap = Treap()
    naive_set = set()

    for i in range(ITERATIONS):
        op_type = random.randint(0, 2)
        val = random.randint(0, MAX_VAL)

        if op_type == 0:  # Insert operation
            treap.insert(val)
            naive_set.add(val)
        elif op_type == 1:  # Delete operation
            if not naive_set:
                continue
            # Choose a value that exists in the set to delete
            val_to_delete = random.choice(list(naive_set))
            treap.delete(val_to_delete)
            naive_set.remove(val_to_delete)
        elif op_type == 2:  # Search operation
            res_optimized = treap.search(val)
            res_naive = val in naive_set

            assert res_optimized == res_naive, (
                f"Search failed on iteration {i} for value {val}!\n"
                f"Operation was search.\n"
                f"Expected: {res_naive}, Got: {res_optimized}"
            )

    # Final verification check across the full range of values
    for val_check in range(MAX_VAL + 1):
        res_optimized = treap.search(val_check)
        res_naive = val_check in naive_set
        assert res_optimized == res_naive, (
            f"Final verification failed for value {val_check}!\n"
            f"Expected: {res_naive}, Got: {res_optimized}"
        )

    print("Treap: All tests passed!")


if __name__ == "__main__":
    run_test()
