"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the Eulerian path/cycle finding
algorithm. It validates the correctness of the `find_euler_path` function by
generating random graphs that are guaranteed to have an Eulerian cycle, finding
the path, and then verifying that the path is a valid Eulerian cycle.

The test operates as follows:
1.  A random undirected graph guaranteed to have an Eulerian cycle is generated.
    This is done by first creating a random tree to ensure connectivity, then
    adding random edges, and finally "fixing" the graph by adding edges between
    pairs of odd-degree vertices until all vertices have an even degree.
2.  The `find_euler_path` function is called on the generated graph.
3.  The script asserts that a path was found.
4.  The returned path is rigorously verified:
    a. It must start and end at the same node (since it's a cycle).
    b. The number of edges in the path must equal the number of edges in the graph.
    c. Every edge in the path must correspond to an edge in the original graph,
       and every edge from the original graph must be used exactly once. This is
       checked using a multiset of edges.

This process ensures the implementation correctly identifies and constructs
Eulerian paths.
"""

import sys
import os
import random
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.euler_path import find_euler_path
from stress_tests.utilities.graph_gen import generate_tree


def generate_undirected_eulerian_graph(n, extra_edges):
    """
    Generates a random connected undirected graph with an Eulerian cycle.
    """
    adj = [[] for _ in range(n)]
    if n > 1:
        tree_adj = generate_tree(n)
        for u, neighbors in enumerate(tree_adj):
            for v in neighbors:
                adj[u].append(v)

    for _ in range(extra_edges):
        if n > 1:
            u, v = random.sample(range(n), 2)
            adj[u].append(v)
            adj[v].append(u)

    degrees = [len(neighbors) for neighbors in adj]
    odd_nodes = [i for i, d in enumerate(degrees) if d % 2 != 0]
    random.shuffle(odd_nodes)

    for i in range(0, len(odd_nodes) - 1, 2):
        u = odd_nodes[i]
        v = odd_nodes[i + 1]
        adj[u].append(v)
        adj[v].append(u)

    return adj


def run_test():
    """
    Performs a stress test on the find_euler_path implementation.
    """
    ITERATIONS = 200
    MAX_N = 50
    MAX_EXTRA_EDGES = 25

    for i in range(ITERATIONS):
        n = random.randint(2, MAX_N)
        extra_edges = random.randint(0, MAX_EXTRA_EDGES)

        adj = generate_undirected_eulerian_graph(n, extra_edges)

        num_edges = sum(len(neighbors) for neighbors in adj) // 2

        path = find_euler_path(adj, n, directed=False)

        assert path is not None, (
            f"Euler path not found for a valid Eulerian graph (test {i})!\n"
            f"Graph (n={n}): {adj}"
        )

        assert path[0] == path[-1], (
            f"Path is not a cycle (test {i})!\n"
            f"Start: {path[0]}, End: {path[-1]}\nPath: {path}"
        )

        assert len(path) == num_edges + 1, (
            f"Path length is incorrect (test {i})!\n"
            f"Expected {num_edges + 1} nodes, got {len(path)}\nPath: {path}"
        )

        edge_counts = Counter()
        for u, neighbors in enumerate(adj):
            for v in neighbors:
                if u < v:
                    edge_counts[(u, v)] += 1

        for j in range(len(path) - 1):
            u, v = sorted((path[j], path[j + 1]))
            edge = (u, v)
            assert edge_counts[edge] > 0, (
                f"Path contains a non-existent edge {edge} (test {i})!\n"
                f"Path: {path}"
            )
            edge_counts[edge] -= 1

        for edge, count in edge_counts.items():
            assert count == 0, (
                f"Edge {edge} was not used in the path (test {i})!\n"
                f"Remaining counts: {edge_counts}"
            )

    print("Euler Path/Cycle: All tests passed!")


if __name__ == "__main__":
    run_test()
