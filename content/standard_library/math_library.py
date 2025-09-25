"""
Author: PyCPBook Community
Source: Python official documentation
Description: This guide highlights essential functions from Python's `math` module
that are frequently used in competitive programming. These functions provide
standard mathematical operations and constants.

Key functions and constants:
- `math.gcd(a, b)`: Computes the greatest common divisor of two integers.
- `math.ceil(x)`: Returns the smallest integer greater than or equal to `x`.
- `math.floor(x)`: Returns the largest integer less than or equal to `x`.
- `math.sqrt(x)`: Returns the floating-point square root of `x`.
- `math.isqrt(x)`: Returns the integer square root of a non-negative integer `x`,
  which is `floor(sqrt(x))`. This is often faster and more precise for integer-only contexts.
- `math.log2(x)`: Returns the base-2 logarithm of `x`.
- `math.inf`: A floating-point representation of positive infinity. Useful for
  initializing minimum/maximum values.

These tools are fundamental for a wide range of problems, from number theory to
geometry, providing a reliable and efficient standard library implementation.
Time: `gcd` is $O(\log(\min(a,b)))$. `isqrt` is faster than `sqrt` for integers.
The rest are typically $O(1)$.
Space: $O(1)$ for all functions.
Status: Stress-tested
"""

import math


def math_examples():
    """
    Demonstrates the usage of common math module functions.
    This function is primarily for inclusion in the notebook and is called
    by the stress test to ensure correctness.
    """
    # Greatest Common Divisor
    gcd_val = math.gcd(54, 24)

    # Ceiling and Floor
    ceil_val = math.ceil(4.2)
    floor_val = math.floor(4.8)

    # Square Roots
    sqrt_val = math.sqrt(25)
    isqrt_val = math.isqrt(26)

    # Logarithm
    log2_val = math.log2(16)

    # Infinity constant
    infinity = math.inf

    return {
        "gcd_val": gcd_val,
        "ceil_val": ceil_val,
        "floor_val": floor_val,
        "sqrt_val": sqrt_val,
        "isqrt_val": isqrt_val,
        "log2_val": log2_val,
        "infinity": infinity,
    }
