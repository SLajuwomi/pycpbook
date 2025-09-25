"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the topological sort algorithm.
It validates the correctness of the `topological_sort` function by generating
random Directed Acyclic Graphs (DAGs) and verifying that the output is a valid
topological ordering.

The test operates as follows:
1. A large number of iterations are run. In each iteration, a random DAG is
   generated using the `generate_dag` utility.
2. The `topological_sort` function is called on the generated graph.
3. The script asserts two conditions for the output:
   a. The length of the returned list must be equal to the number of nodes in
      the graph, as a DAG must have a valid topological sort.
   b. The ordering must be correct. For every directed edge `u -> v` in the
      graph, `u` must appear before `v` in the sorted list. This is checked
      by mapping each node to its position in the output list and comparing
      the positions for each edge.
4. If any assertion fails, the test stops and prints the failing test case.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.topological_sort import topological_sort
from stress_tests.utilities.graph_gen import generate_dag


def is_valid_topological_sort(adj, n, order):
    """
    Checks if a given list is a valid topological sort for a DAG.
    """
    if len(order) != n:
        return False

    pos = {node: i for i, node in enumerate(order)}

    for u in range(n):
        for v in adj[u]:
            if pos[u] > pos[v]:
                return False
    return True


def run_test():
    """
    Performs a stress test on the topological_sort implementation.
    """
    ITERATIONS = 500
    MAX_N = 100
    MAX_M_FACTOR = 1.5

    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        max_m = int(n * (n - 1) / 2 * MAX_M_FACTOR) if n > 1 else 0
        m = random.randint(0, max_m)

        adj = generate_dag(n, m)

        order = topological_sort(adj, n)

        assert len(order) == n, (
            f"Topological sort failed on iteration {i} for a DAG!\n"
            f"Graph (n={n}, m={m}): {adj}\n"
            f"Expected a list of length {n}, but got {len(order)}.\n"
            f"This might indicate a cycle was incorrectly detected."
        )

        assert is_valid_topological_sort(adj, n, order), (
            f"Invalid topological order on iteration {i}!\n"
            f"Graph (n={n}, m={m}): {adj}\n"
            f"Generated order: {order}"
        )

    print("Topological Sort: All tests passed!")


if __name__ == "__main__":
    run_test()
