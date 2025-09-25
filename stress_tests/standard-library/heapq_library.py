"""
@description
This script is a correctness test for the `heapq` library examples provided in
`content/standard_library/heapq_library.py`. It also includes a more general
stress test to validate the core properties of a min-heap.
"""

import sys
import os
import heapq
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.standard_library.heapq_library import heapq_examples
from stress_tests.utilities.random_gen import random_list


def test_examples():
    """
    Executes the example function and asserts the correctness of its output.
    """
    results = heapq_examples()

    assert results["smallest_element"] == 1
    assert results["final_heap"] == [7]
    assert results["popped_elements"] == [1, 4]
    assert results["smallest_after_heapify"] == 1
    # Check heap property for the heapified list
    h = results["heapified_list"]
    for i in range(len(h)):
        if 2 * i + 1 < len(h):
            assert h[i] <= h[2 * i + 1]
        if 2 * i + 2 < len(h):
            assert h[i] <= h[2 * i + 2]


def test_heap_sort_property():
    """
    A stress test that verifies the fundamental property of a min-heap:
    popping elements from it yields a sorted sequence.
    """
    ITERATIONS = 200
    MAX_N = 500
    MAX_VAL = 1000

    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        data = random_list(n, -MAX_VAL, MAX_VAL)

        min_heap = []
        for item in data:
            heapq.heappush(min_heap, item)

        sorted_data = sorted(data)
        popped_data = [heapq.heappop(min_heap) for _ in range(n)]

        assert popped_data == sorted_data, (
            f"Heap sort property failed on iteration {i}!\n"
            f"Original Data: {data}\n"
            f"Expected (Sorted): {sorted_data}\n"
            f"Got (from heap): {popped_data}"
        )


def run_test():
    test_examples()
    test_heap_sort_property()
    print("Standard Library (heapq): All tests passed!")


if __name__ == "__main__":
    run_test()
