"""
@description
This script is a correctness test for the `math` library examples provided in
`content/standard_library/math_library.py`. It verifies that the demonstrations
of key math functions produce the expected, correct results.
"""

import sys
import os
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.standard_library.math_library import math_examples


def run_test():
    """
    Executes the example function and asserts the correctness of its output.
    """
    results = math_examples()

    # --- Verify GCD ---
    assert results["gcd_val"] == 6

    # --- Verify Ceil and Floor ---
    assert results["ceil_val"] == 5
    assert results["floor_val"] == 4

    # --- Verify Square Roots ---
    assert results["sqrt_val"] == 5.0
    assert results["isqrt_val"] == 5

    # --- Verify Logarithm ---
    assert results["log2_val"] == 4.0

    # --- Verify Infinity ---
    assert results["infinity"] == float("inf")
    assert results["infinity"] > 10**100

    print("Standard Library (math): All examples are correct!")


if __name__ == "__main__":
    run_test()
