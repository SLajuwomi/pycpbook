"""
Author: PyCPBook Community
Source: Python official documentation
Description: This guide showcases powerful combinatorial iterators from Python's
`itertools` module. These functions are highly optimized and provide a clean,
efficient way to handle tasks involving permutations, combinations, and Cartesian
products, which are common in competitive programming problems.

`itertools.permutations(iterable, r=None)`:
Returns successive r-length permutations of elements from the iterable. If r is
not specified or is None, then r defaults to the length of the iterable, and all
possible full-length permutations are generated. The elements are treated as
unique based on their position, not their value.

`itertools.combinations(iterable, r)`:
Returns r-length subsequences of elements from the input iterable. The combination
tuples are emitted in lexicographic ordering according to the order of the input
iterable. Elements are treated as unique based on their position, not their value.

`itertools.product(*iterables, repeat=1)`:
Computes the Cartesian product of input iterables. It is equivalent to nested
for-loops. For example, `product(A, B)` returns the same as `((x,y) for x in A
for y in B)`.

These functions are implemented in C, making them significantly faster than
equivalent Python-based recursive or iterative solutions.
Time: The number of items returned is the primary factor. For an iterable of
length N, `permutations` returns $P(N, r)$ items, `combinations` returns $C(N, r)$
items, and `product` returns $N^k$ items for $k$ iterables.
Space: $O(r)$ or $O(N)$ for storing the intermediate tuple.
Status: Stress-tested
"""

import itertools


def itertools_examples():
    """
    Demonstrates the usage of common itertools functions.
    This function is primarily for inclusion in the notebook and is called
    by the stress test to ensure correctness.
    """
    elements = ["A", "B", "C"]

    # --- Permutations ---
    # All full-length permutations of elements
    perms_full = list(itertools.permutations(elements))
    # All 2-element permutations of elements
    perms_partial = list(itertools.permutations(elements, 2))

    # --- Combinations ---
    # All 2-element combinations of elements
    combs = list(itertools.combinations(elements, 2))

    # --- Cartesian Product ---
    pool1 = ["x", "y"]
    pool2 = [1, 2]
    prod = list(itertools.product(pool1, pool2))

    return {
        "perms_full": perms_full,
        "perms_partial": perms_partial,
        "combs": combs,
        "prod": prod,
    }
