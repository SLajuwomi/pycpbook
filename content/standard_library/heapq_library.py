"""
This guide explains how to use Python's `heapq` module to implement a
min-priority queue. A heap is a specialized tree-based data structure that
satisfies the heap property. In a min-heap, for any given node `C`, if `P` is a
parent of `C`, then the key of `P` is less than or equal to the key of `C`. This
means the smallest element is always at the root of the tree.
The `heapq` module provides an efficient implementation of the min-heap algorithm.
It operates directly on a standard Python `list`, which is a key aspect of its
design.
Key functions:
- `heapq.heappush(heap, item)`: Pushes an `item` onto the `heap` (a list),
  maintaining the heap property. This operation is $O(\log N)$.
- `heapq.heappop(heap)`: Pops and returns the smallest `item` from the `heap`,
  maintaining the heap property. This is also $O(\log N)$.
- `heapq.heapify(x)`: Transforms a list `x` into a heap, in-place, in $O(N)$ time.
Since `heapq` implements a min-heap, the element at index 0 (`heap[0]`) is always
the smallest. To implement a max-heap, a common trick is to store the negative
of the values (or use a custom wrapper class).
"""

import heapq


def heapq_examples():
    """
    Demonstrates the usage of the heapq module.
    This function is primarily for inclusion in the notebook and is called
    by the stress test to ensure correctness.
    """
    # --- heappush and heappop ---
    min_heap = []
    heapq.heappush(min_heap, 4)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 7)

    # After pushes, the heap (list) is [1, 4, 7]
    # The smallest element is at index 0
    smallest_element = min_heap[0]

    popped_elements = []
    popped_elements.append(heapq.heappop(min_heap))  # Pops 1
    popped_elements.append(heapq.heappop(min_heap))  # Pops 4

    # --- heapify ---
    data_list = [5, 8, 2, 9, 1, 4]
    heapq.heapify(data_list)
    # After heapify, data_list is now [1, 4, 2, 9, 8, 5] (or similar,
    # it only guarantees the heap property, not a fully sorted list)
    heapified_list = list(data_list)
    smallest_after_heapify = data_list[0]

    return {
        "smallest_element": smallest_element,
        "final_heap": min_heap,
        "popped_elements": popped_elements,
        "heapified_list": heapified_list,
        "smallest_after_heapify": smallest_after_heapify,
    }
