"""
@description
This script is a stress test for the Ordered Set implementation. It validates
the correctness of the `OrderedSet` class by comparing its behavior against
a simple, correct data structure (a sorted Python list) over a large number
of randomized operations.

The test randomly performs four main operations:
1.  insert(key): Adds a key to both the OrderedSet and the sorted list.
2.  delete(key): Removes a key from both structures.
3.  find_by_order(k): Compares the k-th element from the OrderedSet with
    the element at index k in the sorted list.
4.  order_of_key(key): Compares the rank of a key in the OrderedSet with
    the result of a binary search (`bisect_left`) on the sorted list.

By rigorously and randomly testing all public methods, this script ensures that
the complex underlying logic (augmented Treap with split/merge) is correct
and handles all edge cases properly.
"""

import sys
import os
import random
import bisect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.ordered_set import OrderedSet


def run_test():
    """
    Performs a stress test on the OrderedSet implementation.
    """
    ITERATIONS = 20000
    MAX_VAL = 5000

    oset = OrderedSet()
    sorted_list = []

    for i in range(ITERATIONS):
        op_type = random.randint(0, 3)
        val = random.randint(0, MAX_VAL)

        if op_type == 0:  # Insert
            if val not in sorted_list:
                oset.insert(val)
                bisect.insort_left(sorted_list, val)

        elif op_type == 1:  # Delete
            if sorted_list:
                val_to_delete = random.choice(sorted_list)
                oset.delete(val_to_delete)
                sorted_list.remove(val_to_delete)

        elif op_type == 2:  # find_by_order
            if sorted_list:
                k = random.randint(0, len(sorted_list) - 1)
                res_optimized = oset.find_by_order(k)
                res_naive = sorted_list[k]
                assert res_optimized == res_naive, (
                    f"find_by_order({k}) failed on iteration {i}!\n"
                    f"Expected: {res_naive}, Got: {res_optimized}"
                )

        elif op_type == 3:  # order_of_key
            rank_optimized = oset.order_of_key(val)
            rank_naive = bisect.bisect_left(sorted_list, val)
            assert rank_optimized == rank_naive, (
                f"order_of_key({val}) failed on iteration {i}!\n"
                f"Expected: {rank_naive}, Got: {rank_optimized}"
            )

        # Sanity check for size
        assert len(oset) == len(
            sorted_list
        ), f"Size mismatch! Expected {len(sorted_list)}, Got {len(oset)}"

    print("Ordered Set: All tests passed!")


if __name__ == "__main__":
    run_test()
