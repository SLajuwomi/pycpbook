"""
@description
This script is a stress test for the modular arithmetic utility functions.
It validates the correctness of `power`, `extended_gcd`, and `mod_inverse`
by comparing their results against known properties and Python's built-in
functions over a large number of randomized inputs.

The test covers:
1. `power(base, exp, mod)`: Compared against Python's built-in `pow(base, exp, mod)`.
2. `extended_gcd(a, b)`: Verifies that the returned `g`, `x`, `y` satisfy the
   Bézout's identity `a*x + b*y = g` and that `g` is indeed `gcd(a, b)`.
3. `mod_inverse(a, m)`: Verifies that if an inverse `inv_a` is found, the
   property `(a * inv_a) % m == 1` holds. It also checks that an inverse is
   only found when `gcd(a, m) == 1`.
"""

import sys
import os
import random
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.math.modular_arithmetic import power, extended_gcd, mod_inverse


def run_test():
    """
    Performs a stress test on the modular arithmetic implementations.
    """
    ITERATIONS = 5000
    MAX_VAL = 10**9

    # --- Test modular exponentiation ---
    for _ in range(ITERATIONS):
        base = random.randint(0, MAX_VAL)
        exp = random.randint(0, MAX_VAL)
        mod = random.randint(1, MAX_VAL)

        res_optimized = power(base, exp, mod)
        res_builtin = pow(base, exp, mod)

        assert res_optimized == res_builtin, (
            f"power({base}, {exp}, {mod}) failed!\n"
            f"Expected: {res_builtin}, Got: {res_optimized}"
        )

    # --- Test Extended Euclidean Algorithm ---
    for _ in range(ITERATIONS):
        a = random.randint(0, MAX_VAL)
        b = random.randint(0, MAX_VAL)

        g_optimized, x, y = extended_gcd(a, b)
        g_builtin = math.gcd(a, b)

        assert g_optimized == g_builtin, (
            f"extended_gcd({a}, {b}) returned incorrect GCD!\n"
            f"Expected: {g_builtin}, Got: {g_optimized}"
        )

        assert a * x + b * y == g_optimized, (
            f"extended_gcd({a}, {b}) failed Bezout's identity!\n"
            f"a*x + b*y = {a}*{x} + {b}*{y} = {a*x + b*y}\n"
            f"Expected GCD: {g_optimized}"
        )

    # --- Test Modular Inverse ---
    for _ in range(ITERATIONS):
        a = random.randint(1, MAX_VAL)
        m = random.randint(2, MAX_VAL)

        is_coprime = math.gcd(a, m) == 1
        inv_a = mod_inverse(a, m)

        if is_coprime:
            assert (
                inv_a is not None
            ), f"mod_inverse({a}, {m}) failed to find an inverse for coprime inputs!\n"
            assert (a * inv_a) % m == 1, (
                f"mod_inverse({a}, {m}) returned incorrect inverse {inv_a}!\n"
                f"({a} * {inv_a}) % {m} = {(a * inv_a) % m}, expected 1"
            )
        else:
            assert (
                inv_a is None
            ), f"mod_inverse({a}, {m}) found an inverse {inv_a} for non-coprime inputs!\n"

    print("Modular Arithmetic: All tests passed!")


if __name__ == "__main__":
    run_test()
