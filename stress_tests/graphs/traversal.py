"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the graph traversal algorithms
(BFS and DFS) located in `content/graph/traversal.py`. Its purpose is to
validate the correctness of the optimized `bfs` and `dfs` functions by
comparing their results against a simple, unambiguously correct naive
implementation.

The test operates as follows:
1. A large number of iterations are run. In each iteration, a random graph is
   generated using the `generate_graph` utility, with random parameters for the
   number of nodes, number of edges, and directedness.
2. A random starting node is selected for the traversal.
3. The `bfs` and `dfs` functions are called to get the set of visited nodes.
4. A `naive_reachable_nodes` function, which serves as the ground truth, is
   also called to find all reachable nodes.
5. The script asserts that the set of nodes visited by both `bfs` and `dfs` is
   identical to the set of nodes found by the naive method. If any discrepancy
   is found, the test fails and prints the failing test case.

Time: N/A (This is a test script, not a library algorithm.)
Space: N/A
Status: Not applicable (Test script)
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.traversal import bfs, dfs
from stress_tests.utilities.graph_gen import generate_graph


def naive_reachable_nodes(adj, start_node, n):
    """
    A simple, correct implementation to find all reachable nodes from a start node.
    This serves as the ground truth for validation.
    """
    if not (0 <= start_node < n):
        return set()

    stack = [start_node]
    visited = {start_node}
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return visited


def run_test():
    """
    Performs a stress test on the BFS and DFS implementations.
    """
    ITERATIONS = 500
    MAX_N = 100
    MAX_M_FACTOR = 1.5

    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        # Ensure m can be larger than n for denser graphs
        max_m = int(n * (n - 1) / 2 * MAX_M_FACTOR) if n > 1 else 0
        m = random.randint(0, max_m)
        is_directed = random.choice([True, False])

        adj = generate_graph(n, m, directed=is_directed)

        start_node = random.randint(0, n - 1)

        # Run all three traversal methods
        visited_bfs = bfs(adj, start_node, n)
        visited_dfs = dfs(adj, start_node, n)
        reachable_naive = naive_reachable_nodes(adj, start_node, n)

        # The set of visited nodes should be identical for all methods
        set_visited_bfs = set(visited_bfs)
        set_visited_dfs = set(visited_dfs)

        assert set_visited_bfs == reachable_naive, (
            f"BFS failed on iteration {i} for start_node {start_node}!\n"
            f"Graph (n={n}, m={m}, directed={is_directed}): {adj}\n"
            f"Expected reachable nodes: {sorted(list(reachable_naive))}\n"
            f"Got from BFS: {sorted(list(set_visited_bfs))}"
        )

        assert set_visited_dfs == reachable_naive, (
            f"DFS failed on iteration {i} for start_node {start_node}!\n"
            f"Graph (n={n}, m={m}, directed={is_directed}): {adj}\n"
            f"Expected reachable nodes: {sorted(list(reachable_naive))}\n"
            f"Got from DFS: {sorted(list(set_visited_dfs))}"
        )

    print("Graph Traversal (BFS & DFS): All tests passed!")


if __name__ == "__main__":
    run_test()
