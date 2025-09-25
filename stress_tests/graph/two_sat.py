"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the 2-Satisfiability (2-SAT) solver.
It validates the correctness of the `TwoSAT` class by generating random 2-CNF
formulas and, if the solver finds a solution, verifying that the proposed
assignment satisfies all clauses.

The test operates as follows:
1.  For a number of iterations, generate a random number of variables `n` and
    clauses `m`.
2.  Create `m` random clauses, where each literal is a random variable from 1 to `n`
    or its negation.
3.  Instantiate the `TwoSAT` solver and add all generated clauses.
4.  Call the `solve()` method.
5.  If the solver returns `satisfiable = True` and an assignment, this script
    verifies the solution. It iterates through every original clause and checks
    if the assignment makes the clause true. If any clause is false under the
    assignment, the test fails.
6.  If the solver returns `satisfiable = False`, the test passes for that
    iteration, as verifying unsatisfiability naively is complex. The main goal
    is to ensure that when a solution is provided, it is always correct.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.two_sat import TwoSAT


def run_test():
    """
    Performs a stress test on the TwoSAT implementation.
    """
    ITERATIONS = 200
    MAX_N = 50
    MAX_M_FACTOR = 2.0

    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        max_m = int(n * MAX_M_FACTOR)
        m = random.randint(1, max_m)

        clauses = []
        for _ in range(m):
            u = random.randint(1, n) * random.choice([-1, 1])
            v = random.randint(1, n) * random.choice([-1, 1])
            clauses.append((u, v))

        solver = TwoSAT(n)
        for u, v in clauses:
            solver.add_clause(u, v)

        satisfiable, assignment = solver.solve()

        if satisfiable:
            assert (
                assignment is not None
            ), f"Solver returned satisfiable but no assignment (test {i})"
            assert len(assignment) == n, f"Assignment length mismatch (test {i})"

            for u, v in clauses:
                u_abs, v_abs = abs(u), abs(v)

                term1_val = (
                    assignment[u_abs - 1] if u > 0 else not assignment[u_abs - 1]
                )
                term2_val = (
                    assignment[v_abs - 1] if v > 0 else not assignment[v_abs - 1]
                )

                assert term1_val or term2_val, (
                    f"Assignment failed to satisfy clause ({u}, {v}) (test {i})!\n"
                    f"n={n}, m={m}\n"
                    f"Clauses: {clauses}\n"
                    f"Assignment: {assignment}"
                )

    print("2-SAT Algorithm: All tests passed!")


if __name__ == "__main__":
    run_test()
