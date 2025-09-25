"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the Lowest Common Ancestor (LCA)
algorithm using binary lifting. It validates the correctness of the `LCA` class
by comparing its query results against a simple, but much slower, naive LCA
finding algorithm.

The test operates as follows:
1.  A random tree is generated using the `generate_tree` utility.
2.  A random root for the tree is selected.
3.  The `LCA` class is instantiated, which performs the $O(N \\log N)$
    precomputation.
4.  A naive LCA function is defined. This function works by first finding the
    path from the root to each of the two query nodes, and then finding the
    last common vertex in these two paths. This is slow ($O(N)$ per query) but
    unambiguously correct.
5.  For a large number of iterations, two random nodes `u` and `v` are chosen.
6.  The LCA is computed using both the optimized `LCA.query(u, v)` and the
    `naive_lca(u, v)`.
7.  The results are asserted to be identical. If they ever differ, the test
    fails, providing the context of the failure.
"""

import sys
import os
import random
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.lca_binary_lifting import LCA
from stress_tests.utilities.graph_gen import generate_tree


def get_path_to_node(adj, root, target_node, n):
    """Helper to find the path from root to a target node using BFS."""
    q = deque([(root, [root])])
    visited = {root}
    while q:
        curr, path = q.popleft()
        if curr == target_node:
            return path
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                q.append((neighbor, new_path))
    return []


def naive_lca(adj, root, u, v, n):
    """
    A naive O(N) implementation of LCA for validation.
    Finds paths from root to u and v, then finds their last common node.
    """
    if u == v:
        return u
    path_u = get_path_to_node(adj, root, u, n)
    path_v = get_path_to_node(adj, root, v, n)

    lca_node = root
    for i in range(min(len(path_u), len(path_v))):
        if path_u[i] == path_v[i]:
            lca_node = path_u[i]
        else:
            break
    return lca_node


def run_test():
    """
    Performs a stress test on the LCA implementation.
    """
    ITERATIONS = 50
    MAX_N = 100
    QUERIES_PER_ITERATION = 100

    for i in range(ITERATIONS):
        n = random.randint(2, MAX_N)
        adj_unweighted = generate_tree(n)
        root = random.randint(0, n - 1)

        # The LCA class expects an adjacency list where adj[u] is a list of neighbors
        lca_solver = LCA(n, adj_unweighted, root)

        for _ in range(QUERIES_PER_ITERATION):
            u, v = random.sample(range(n), 2)

            res_optimized = lca_solver.query(u, v)
            res_naive = naive_lca(adj_unweighted, root, u, v, n)

            assert res_optimized == res_naive, (
                f"LCA query failed on iteration {i} for nodes ({u}, {v})!\n"
                f"Tree (n={n}, root={root}): {adj_unweighted}\n"
                f"Expected (Naive): {res_naive}\n"
                f"Got (Optimized): {res_optimized}"
            )

    print("Lowest Common Ancestor (Binary Lifting): All tests passed!")


if __name__ == "__main__":
    run_test()
