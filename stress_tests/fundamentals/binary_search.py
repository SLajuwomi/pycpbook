"""
@description
This script is a stress test for the binary search implementation. It validates
the correctness of the `binary_search` function, which finds a specific target
in a sorted array, by comparing its results against a naive linear scan or
Python's `list.index()` method.

The test workflow is as follows:
1.  A random sorted list of unique integers is generated.
2.  For a large number of iterations, a random operation is chosen:
    a. Search for an element known to be in the list. The test asserts that
       `binary_search` returns a correct index.
    b. Search for an element known not to be in the list. The test asserts
       that `binary_search` returns -1.
3.  This process ensures the implementation is correct for both successful and
    unsuccessful searches.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.binary_search import binary_search


def naive_search(arr, target):
    """
    A simple O(N) linear search for validation.
    """
    try:
        return arr.index(target)
    except ValueError:
        return -1


def run_test():
    """
    Performs a stress test on the binary_search implementation.
    """
    ITERATIONS = 5000
    MAX_N = 1000
    MAX_VAL = 2000

    for i in range(ITERATIONS):
        n = random.randint(0, MAX_N)
        # Generate a sorted list of unique elements
        arr = sorted(list(set(random.randint(0, MAX_VAL) for _ in range(n))))

        # 50% chance to search for an existing element, 50% for a non-existing one
        if arr and random.random() < 0.5:
            # Search for an existing element
            target = random.choice(arr)
            expected_idx = naive_search(arr, target)
            res_optimized = binary_search(arr, target)

            # The array has unique elements, so index() is fine.
            # If duplicates were allowed, we'd need to check arr[res_optimized] == target
            assert res_optimized == expected_idx, (
                f"Binary search failed on iteration {i} for existing target!\n"
                f"Array: {arr}\n"
                f"Target: {target}\n"
                f"Expected index: {expected_idx}, Got: {res_optimized}"
            )
        else:
            # Search for a non-existing element
            target = MAX_VAL + random.randint(1, 100)  # Guaranteed not to be in arr
            expected_idx = -1
            res_optimized = binary_search(arr, target)

            assert res_optimized == expected_idx, (
                f"Binary search failed on iteration {i} for non-existing target!\n"
                f"Array: {arr}\n"
                f"Target: {target}\n"
                f"Expected index: {expected_idx}, Got: {res_optimized}"
            )

    # Test edge cases
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 30) == 2
    assert binary_search(arr, 10) == 0
    assert binary_search(arr, 50) == 4
    assert binary_search(arr, 5) == -1
    assert binary_search(arr, 55) == -1
    assert binary_search(arr, 35) == -1
    assert binary_search([], 10) == -1  # Empty array

    print("Binary Search: All tests passed!")


if __name__ == "__main__":
    run_test()
