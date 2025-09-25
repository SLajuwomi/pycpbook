"""
@description
This script is a correctness test for the `itertools` library examples provided
in `content/standard_library/itertools_library.py`. It validates the output
of the key combinatorial functions (`permutations`, `combinations`, `product`)
by comparing them against naive, recursive/iterative implementations.
"""

import sys
import os
import itertools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.standard_library.itertools_library import itertools_examples


# --- Naive Implementations for Validation ---


def naive_permutations(items, r=None):
    if r is None:
        r = len(items)
    if r > len(items):
        return []
    if r == 0:
        return [()]

    result = []
    for i in range(len(items)):
        first = items[i]
        rest = items[:i] + items[i + 1 :]
        for p in naive_permutations(rest, r - 1):
            result.append((first,) + p)
    return result


def naive_combinations(items, r):
    if r == 0:
        return [()]
    if not items or r > len(items):
        return []

    first = items[0]
    rest = items[1:]

    combs_with_first = []
    for c in naive_combinations(rest, r - 1):
        combs_with_first.append((first,) + c)

    combs_without_first = naive_combinations(rest, r)

    return combs_with_first + combs_without_first


def naive_product(*pools):
    result = [()]
    for pool in pools:
        result = [x + (y,) for x in result for y in pool]
    return result


def run_test():
    """
    Executes the example function and asserts the correctness of its output
    by comparing it to naive implementations.
    """
    # --- Test example outputs from the content file ---
    results = itertools_examples()

    # The order is guaranteed for itertools, so we can compare directly
    assert results["perms_full"] == [
        ("A", "B", "C"),
        ("A", "C", "B"),
        ("B", "A", "C"),
        ("B", "C", "A"),
        ("C", "A", "B"),
        ("C", "B", "A"),
    ]
    assert results["perms_partial"] == [
        ("A", "B"),
        ("A", "C"),
        ("B", "A"),
        ("B", "C"),
        ("C", "A"),
        ("C", "B"),
    ]
    assert results["combs"] == [("A", "B"), ("A", "C"), ("B", "C")]
    assert results["prod"] == [("x", 1), ("x", 2), ("y", 1), ("y", 2)]

    # --- Stress test against naive implementations ---
    elements = [1, 2, 3, 4]

    # Test permutations
    perms_r2_itertools = sorted(list(itertools.permutations(elements, 2)))
    perms_r2_naive = sorted(naive_permutations(elements, 2))
    assert perms_r2_itertools == perms_r2_naive

    perms_full_itertools = sorted(list(itertools.permutations(elements)))
    perms_full_naive = sorted(naive_permutations(elements))
    assert perms_full_itertools == perms_full_naive

    # Test combinations
    combs_r3_itertools = sorted(list(itertools.combinations(elements, 3)))
    combs_r3_naive = sorted(naive_combinations(elements, 3))
    assert combs_r3_itertools == combs_r3_naive

    # Test product
    pool1 = [1, 2]
    pool2 = ["a", "b"]
    prod_itertools = sorted(list(itertools.product(pool1, pool2)))
    prod_naive = sorted(naive_product(pool1, pool2))
    assert prod_itertools == prod_naive

    print("Standard Library (itertools): All tests passed!")


if __name__ == "__main__":
    run_test()
