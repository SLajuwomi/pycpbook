"""
@description
This script is a correctness test for the `@functools.cache` example provided
in `content/standard_library/functools_library.py`. It validates that the
memoized recursive Fibonacci function produces the correct results by comparing
it against a simple, efficient iterative implementation.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.standard_library.functools_library import fibonacci_with_cache


def naive_fibonacci_iterative(n):
    """
    A simple, correct iterative DP solution for Fibonacci for validation.
    """
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def run_test():
    """
    Verifies the correctness of the cached recursive solution against an
    iterative one.
    """
    # Test a range of Fibonacci numbers
    for i in range(50):
        res_cached = fibonacci_with_cache(i)
        res_iterative = naive_fibonacci_iterative(i)
        assert res_cached == res_iterative, (
            f"Fibonacci test failed for n={i}!\n"
            f"Expected (Iterative): {res_iterative}, Got (Cached): {res_cached}"
        )

    # Specific known values
    assert fibonacci_with_cache(0) == 0
    assert fibonacci_with_cache(1) == 1
    assert fibonacci_with_cache(10) == 55
    assert fibonacci_with_cache(20) == 6765

    print("Standard Library (functools): All tests passed!")


if __name__ == "__main__":
    run_test()
