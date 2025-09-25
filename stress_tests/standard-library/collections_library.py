"""
@description
This script is a correctness test for the `collections` library examples provided
in `content/standard_library/collections_library.py`. It verifies that the
demonstrations of `deque`, `Counter`, and `defaultdict` work as expected.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.standard_library.collections_library import collections_examples


def run_test():
    """
    Executes the example function and asserts the correctness of its output.
    """
    results = collections_examples()

    # --- Verify deque behavior ---
    assert results["final_deque"] == [1, 2, 3]
    assert results["q_pop_left"] == 0
    assert results["q_pop_right"] == 4

    # --- Verify Counter behavior ---
    assert results["counter_a"] == 3
    assert results["counter_d"] == 0

    # --- Verify defaultdict behavior ---
    # The adjacency list for key 5 was accessed, so it should exist in the final dict
    expected_adj = {0: [1, 2], 1: [0, 2], 2: [0, 1], 5: []}
    assert results["adj_list"] == expected_adj
    assert results["adj_list_missing"] == []

    print("Standard Library (collections): All examples are correct!")


if __name__ == "__main__":
    run_test()
