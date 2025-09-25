"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the maximum bipartite matching
algorithm. It validates its correctness by comparing the result with the
maximum flow in a corresponding flow network, a classic and powerful validation
technique based on the max-flow min-cut theorem.

The test operates as follows:
1.  A random bipartite graph is generated with `n1` vertices on the left, `n2`
    on the right, and a random number of edges.
2.  A flow network is constructed from this bipartite graph:
    a. A source `s` and a sink `t` are created.
    b. For each vertex `u` on the left, an edge `s -> u` with capacity 1 is added.
    c. For each vertex `v` on the right, an edge `v -> t` with capacity 1 is added.
    d. For each edge `(u, v)` in the original bipartite graph, a directed edge
       `u -> v` with capacity 1 is added.
3.  The `bipartite_matching` function is called on the original graph.
4.  The `Dinic` max-flow algorithm is run on the constructed flow network from `s` to `t`.
5.  The script asserts that the size of the maximum matching is equal to the
    value of the maximum flow. This equivalence is a well-known theorem.

This process is repeated for many iterations to ensure the matching algorithm is
correct across a wide variety of graph structures.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.bipartite_matching import bipartite_matching
from content.graph.dinic import Dinic


def generate_bipartite_graph(n1, n2, m):
    """Generates a random bipartite graph."""
    adj = [[] for _ in range(n1)]
    edges = set()
    max_edges = n1 * n2
    m = min(m, max_edges)

    while len(edges) < m:
        u = random.randint(0, n1 - 1)
        v = random.randint(0, n2 - 1)
        if (u, v) not in edges:
            edges.add((u, v))
            adj[u].append(v)
    return adj


def run_test():
    """
    Performs a stress test on the bipartite_matching implementation.
    """
    ITERATIONS = 200
    MAX_N1 = 30
    MAX_N2 = 30
    MAX_M_FACTOR = 1.5

    for i in range(ITERATIONS):
        n1 = random.randint(1, MAX_N1)
        n2 = random.randint(1, MAX_N2)
        max_m = int(n1 * n2 * MAX_M_FACTOR)
        m = random.randint(0, max_m)

        adj = generate_bipartite_graph(n1, n2, m)

        # --- Solve using Bipartite Matching ---
        matching_size = bipartite_matching(adj, n1, n2)

        # --- Solve using Max Flow (Dinic's) ---
        source = n1 + n2
        sink = n1 + n2 + 1
        dinic_solver = Dinic(n1 + n2 + 2)

        # Edges from source to left partition
        for u in range(n1):
            dinic_solver.add_edge(source, u, 1)

        # Edges from left to right partition
        for u in range(n1):
            for v in adj[u]:
                dinic_solver.add_edge(u, v + n1, 1)

        # Edges from right partition to sink
        for v in range(n2):
            dinic_solver.add_edge(v + n1, sink, 1)

        max_flow_val = dinic_solver.max_flow(source, sink)

        assert matching_size == max_flow_val, (
            f"Bipartite matching mismatch on iteration {i}!\n"
            f"Graph (n1={n1}, n2={n2}, m={m}): {adj}\n"
            f"Expected (Max Flow): {max_flow_val}\n"
            f"Got (Matching): {matching_size}"
        )

    print("Bipartite Matching: All tests passed!")


if __name__ == "__main__":
    run_test()
