"""
@description
This script is a correctness test for the `bisect` library examples and a
stress test for the `bisect` module's core functions. It validates that
`bisect_left` and `bisect_right` behave as expected by comparing their
results against a naive, linear scan.
"""

import sys
import os
import random
import bisect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.standard_library.bisect_library import bisect_examples
from stress_tests.utilities.random_gen import random_list


def naive_bisect_left(a, x):
    """Finds insertion point for x in a, maintaining sorted order (left variant)."""
    for i, item in enumerate(a):
        if item >= x:
            return i
    return len(a)


def naive_bisect_right(a, x):
    """Finds insertion point for x in a, maintaining sorted order (right variant)."""
    for i, item in enumerate(a):
        if item > x:
            return i
    return len(a)


def test_examples():
    """
    Executes the example function and asserts the correctness of its output.
    """
    results = bisect_examples()

    assert results["idx_left_20"] == 1
    assert results["idx_left_25"] == 3
    assert results["idx_right_20"] == 3
    assert results["idx_right_25"] == 3
    assert results["list_after_insort"] == [10, 20, 20, 25, 30, 40]


def test_bisect_functions():
    """
    A stress test that verifies the behavior of bisect_left and bisect_right
    against naive linear scans.
    """
    ITERATIONS = 2000
    MAX_N = 500
    MAX_VAL = 1000

    for i in range(ITERATIONS):
        n = random.randint(0, MAX_N)
        data = sorted(random_list(n, 0, MAX_VAL))
        target = random.randint(0, MAX_VAL + 50)

        # Test bisect_left
        res_optimized_left = bisect.bisect_left(data, target)
        res_naive_left = naive_bisect_left(data, target)
        assert res_optimized_left == res_naive_left, (
            f"bisect_left failed on iteration {i}!\n"
            f"Data: {data}\nTarget: {target}\n"
            f"Expected: {res_naive_left}, Got: {res_optimized_left}"
        )

        # Test bisect_right
        res_optimized_right = bisect.bisect_right(data, target)
        res_naive_right = naive_bisect_right(data, target)
        assert res_optimized_right == res_naive_right, (
            f"bisect_right failed on iteration {i}!\n"
            f"Data: {data}\nTarget: {target}\n"
            f"Expected: {res_naive_right}, Got: {res_optimized_right}"
        )


def run_test():
    test_examples()
    test_bisect_functions()
    print("Standard Library (bisect): All tests passed!")


if __name__ == "__main__":
    run_test()
