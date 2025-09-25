"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for Dijkstra's algorithm. It validates
the correctness of the `dijkstra` function by comparing its results against a
simpler, known-correct algorithm.

The test includes two main scenarios:
1.  Unweighted Graphs: A random unweighted graph is generated. Dijkstra's
    algorithm is run with all edge weights as 1. The results are compared
    against a standard Breadth-First Search (BFS), which is guaranteed to find
    the shortest paths in an unweighted graph.
2.  Weighted Graphs with Non-Negative Weights: A random weighted graph with
    only non-negative weights is generated. The results from Dijkstra's are
    compared against the Bellman-Ford algorithm. While Bellman-Ford is slower,
    it is correct for this case and serves as a reliable ground truth.

This dual-scenario approach ensures that Dijkstra's implementation is correct
for both the special case of unweighted graphs and the general case of
non-negatively weighted graphs.
"""

import sys
import os
import random
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.dijkstra import dijkstra
from content.graph.bellman_ford import bellman_ford
from stress_tests.utilities.graph_gen import generate_graph


def bfs_shortest_path(adj, start_node, n):
    """
    Calculates shortest paths in an unweighted graph using BFS.
    """
    if not (0 <= start_node < n):
        return [float("inf")] * n
    dist = [float("inf")] * n
    dist[start_node] = 0
    q = deque([start_node])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == float("inf"):
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def run_test():
    """
    Performs a stress test on the Dijkstra implementation.
    """
    ITERATIONS = 200
    MAX_N = 50
    MAX_M_FACTOR = 2.0
    MAX_WEIGHT = 100

    # Test against BFS on unweighted graphs
    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        max_m = int(n * (n - 1) * MAX_M_FACTOR) if n > 1 else 0
        m = random.randint(0, max_m)
        is_directed = random.choice([True, False])

        adj_unweighted = generate_graph(n, m, directed=is_directed)
        start_node = random.randint(0, n - 1)

        adj_weighted = [[(v, 1) for v in neighbors] for neighbors in adj_unweighted]

        dist_dijkstra = dijkstra(adj_weighted, start_node, n)
        dist_bfs = bfs_shortest_path(adj_unweighted, start_node, n)

        assert dist_dijkstra == dist_bfs, (
            f"Dijkstra failed on unweighted graph test {i}!\n"
            f"Graph (n={n}, m={m}, directed={is_directed}, start={start_node}): {adj_unweighted}\n"
            f"Expected (BFS): {dist_bfs}\n"
            f"Got (Dijkstra): {dist_dijkstra}"
        )

    # Test against Bellman-Ford on weighted graphs (non-negative weights)
    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        max_m = int(n * (n - 1) * MAX_M_FACTOR) if n > 1 else 0
        m = random.randint(0, max_m)
        is_directed = random.choice([True, False])

        adj_weighted = generate_graph(
            n,
            m,
            directed=is_directed,
            weighted=True,
            min_weight=0,
            max_weight=MAX_WEIGHT,
        )
        start_node = random.randint(0, n - 1)

        edges = []
        for u, neighbors in enumerate(adj_weighted):
            for v, w in neighbors:
                edges.append((u, v, w))

        dist_dijkstra = dijkstra(adj_weighted, start_node, n)
        dist_bf, has_neg_cycle = bellman_ford(edges, start_node, n)

        assert (
            not has_neg_cycle
        ), "Test setup error: generated a negative cycle with non-negative weights."
        assert dist_dijkstra == dist_bf, (
            f"Dijkstra failed on weighted graph test {i}!\n"
            f"Graph (n={n}, m={m}, directed={is_directed}, start={start_node}): {adj_weighted}\n"
            f"Expected (Bellman-Ford): {dist_bf}\n"
            f"Got (Dijkstra): {dist_dijkstra}"
        )

    print("Dijkstra's Algorithm: All tests passed!")


if __name__ == "__main__":
    run_test()
