"""
Author: PyCPBook Community
Source: Python official documentation
Description: This guide explains how to use Python's `bisect` module to
efficiently search for elements and maintain the sorted order of a list. The
module provides functions for binary searching, which is significantly faster
than a linear scan for large lists.

The `bisect` module is particularly useful for finding insertion points for new
elements while keeping a list sorted, without having to re-sort the entire list
after each insertion.

Key functions:
- `bisect.bisect_left(a, x)`: Returns an insertion point which comes before (to
  the left of) any existing entries of `x` in `a`. This is equivalent to finding
  the index of the first element greater than or equal to `x`.
- `bisect.bisect_right(a, x)`: Returns an insertion point which comes after (to
  the right of) any existing entries of `x` in `a`. This is equivalent to finding
  the index of the first element strictly greater than `x`.
- `bisect.insort_left(a, x)`: Inserts `x` into `a` in sorted order. This is
  efficient for finding the position, but the insertion itself can be slow ($O(N)$)
  as it requires shifting elements.

These functions are fundamental for problems that require maintaining a sorted
collection or performing searches like "count elements less than x" or
"find the first element satisfying a condition."

Time: `bisect_left` and `bisect_right` are $O(\log N)$. `insort_left` is $O(N)$
due to the list insertion.
Space: $O(1)$ for searches.
Status: To be stress-tested
"""

import bisect


def bisect_examples():
    """
    Demonstrates the usage of the bisect module.
    This function is primarily for inclusion in the notebook and is called
    by the stress test to ensure correctness.
    """
    data = [10, 20, 20, 30, 40]

    # --- bisect_left ---
    # Find insertion point for 20 (before existing 20s)
    idx_left_20 = bisect.bisect_left(data, 20)
    # Find insertion point for 25 (between 20 and 30)
    idx_left_25 = bisect.bisect_left(data, 25)

    # --- bisect_right ---
    # Find insertion point for 20 (after existing 20s)
    idx_right_20 = bisect.bisect_right(data, 20)
    # Find insertion point for 25 (same as bisect_left)
    idx_right_25 = bisect.bisect_right(data, 25)

    # --- insort ---
    # insort_left inserts at the position found by bisect_left
    data_for_insort = [10, 20, 20, 30, 40]
    bisect.insort_left(data_for_insort, 25)

    return {
        "idx_left_20": idx_left_20,
        "idx_left_25": idx_left_25,
        "idx_right_20": idx_right_20,
        "idx_right_25": idx_right_25,
        "list_after_insort": data_for_insort,
    }
