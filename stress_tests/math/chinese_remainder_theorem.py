"""
@description
This script is a stress test for the Chinese Remainder Theorem (CRT) solver.
It validates the correctness of the `chinese_remainder_theorem` function by
generating random systems of congruences that are guaranteed to have a solution,
solving them, and then verifying that the solution satisfies all original
congruences.

The test workflow is as follows:
1.  A random solution `x` is chosen, along with a set of random moduli.
2.  A system of congruences `res \equiv x (mod m_i)` is created by calculating
    `a_i = x % m_i` for each modulus `m_i`. This guarantees that `x` is a
    valid solution.
3.  The `chinese_remainder_theorem` function is called to solve this system.
4.  The test asserts that a solution `(res, lcm)` is found.
5.  It then verifies that the returned `res` satisfies all original congruences,
    i.e., `res % m_i == a_i` for all `i`.
6.  It also includes specific test cases for systems with no solution.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.math.chinese_remainder_theorem import chinese_remainder_theorem


def run_test():
    """
    Performs a stress test on the Chinese Remainder Theorem implementation.
    """
    ITERATIONS = 5000
    MAX_MODULUS = 1000
    MAX_NUM_EQUATIONS = 10

    for i in range(ITERATIONS):
        num_equations = random.randint(2, MAX_NUM_EQUATIONS)
        moduli = [random.randint(2, MAX_MODULUS) for _ in range(num_equations)]

        # To guarantee a solution exists, we generate it first.
        # The LCM of moduli can be large, so we generate a solution
        # within a reasonable range.
        max_solution_val = 1
        for m in moduli:
            max_solution_val *= m

        true_solution = random.randint(0, min(max_solution_val, 10**18))
        remainders = [true_solution % m for m in moduli]

        result = chinese_remainder_theorem(remainders, moduli)

        assert result is not None, (
            f"CRT failed to find a solution on iteration {i} when one exists!\n"
            f"Remainders: {remainders}\nModuli: {moduli}\n"
            f"True solution was based on {true_solution}"
        )

        res, lcm = result
        for j in range(num_equations):
            assert res % moduli[j] == remainders[j], (
                f"CRT solution is incorrect on iteration {i} for congruence {j}!\n"
                f"x = {res} (mod {lcm})\n"
                f"Expected {remainders[j]} (mod {moduli[j]}), got {res % moduli[j]}"
            )

    # Test cases with no solution
    unsolvable_cases = [
        ([0, 1], [2, 2]),
        ([1, 2], [3, 6]),
        ([3, 4], [4, 6]),
    ]

    for remainders, moduli in unsolvable_cases:
        result = chinese_remainder_theorem(remainders, moduli)
        assert result is None, (
            f"CRT found a solution for an unsolvable system!\n"
            f"Remainders: {remainders}\nModuli: {moduli}\n"
            f"Got: {result}"
        )

    print("Chinese Remainder Theorem: All tests passed!")


if __name__ == "__main__":
    run_test()
