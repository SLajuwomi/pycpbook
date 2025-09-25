"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the Floyd-Warshall algorithm.
It validates the correctness of the `floyd_warshall` function by comparing its
all-pairs shortest path results against the results of running a single-source
shortest path (SSSP) algorithm from every node.

The test includes three main scenarios:
1.  Graphs with Non-Negative Weights: A random graph with non-negative weights
    is generated. The results from `floyd_warshall` are compared against the
    results of running Dijkstra's algorithm from every node.
2.  Graphs with Negative Weights (No Negative Cycles): A random graph with
    negative weights is generated. The results are compared against running
    the Bellman-Ford algorithm from every node.
3.  Graphs with Negative Cycles: A negative-weight cycle is deliberately
    introduced into a graph. The test asserts that `floyd_warshall` correctly
    reports the presence of this cycle.

This comprehensive testing ensures the algorithm is correct for its primary
use cases.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.floyd_warshall import floyd_warshall
from content.graph.dijkstra import dijkstra
from content.graph.bellman_ford import bellman_ford
from stress_tests.utilities.graph_gen import generate_graph


def run_test():
    """
    Performs a stress test on the Floyd-Warshall implementation.
    """
    ITERATIONS = 50
    MAX_N = 25
    MAX_M_FACTOR = 2.0
    MAX_WEIGHT = 100

    # Test 1: Non-negative weights vs Dijkstra from every node
    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        m = random.randint(0, n * (n - 1))
        adj = generate_graph(
            n, m, directed=True, weighted=True, min_weight=0, max_weight=MAX_WEIGHT
        )
        edges = []
        for u, neighbors in enumerate(adj):
            for v, w in neighbors:
                edges.append((u, v, w))

        dist_fw, has_neg_cycle_fw = floyd_warshall(edges, n)
        assert not has_neg_cycle_fw, "Negative cycle detected with non-negative weights"

        for start_node in range(n):
            dist_dijkstra = dijkstra(adj, start_node, n)
            assert dist_fw[start_node] == dist_dijkstra, (
                f"Floyd-Warshall vs Dijkstra failed (test {i}, start={start_node})!\n"
                f"Expected: {dist_dijkstra}\nGot: {dist_fw[start_node]}"
            )

    # Test 2: Negative weights vs Bellman-Ford from every node
    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        m = random.randint(0, n * (n - 1))
        adj = generate_graph(
            n,
            m,
            directed=True,
            weighted=True,
            min_weight=-MAX_WEIGHT,
            max_weight=MAX_WEIGHT,
        )
        edges = []
        for u, neighbors in enumerate(adj):
            for v, w in neighbors:
                edges.append((u, v, w))

        dist_fw, has_neg_cycle_fw = floyd_warshall(edges, n)

        if not has_neg_cycle_fw:
            for start_node in range(n):
                dist_bf, has_neg_cycle_bf = bellman_ford(edges, start_node, n)
                if not has_neg_cycle_bf:
                    assert dist_fw[start_node] == dist_bf, (
                        f"Floyd-Warshall vs Bellman-Ford failed (test {i}, start={start_node})!\n"
                        f"Expected: {dist_bf}\nGot: {dist_fw[start_node]}"
                    )

    # Test 3: Negative cycle detection
    for i in range(ITERATIONS):
        n = random.randint(3, MAX_N)
        m = random.randint(n, n * (n - 1))
        adj = generate_graph(
            n, m, directed=True, weighted=True, min_weight=1, max_weight=MAX_WEIGHT
        )

        # Introduce a negative cycle
        nodes_in_cycle = random.sample(range(n), 3)
        c1, c2, c3 = nodes_in_cycle
        edges = []
        for u, neighbors in enumerate(adj):
            for v, w in neighbors:
                edges.append((u, v, w))

        edges.append((c1, c2, 1))
        edges.append((c2, c3, 1))
        edges.append((c3, c1, -100))

        _, has_neg_cycle_fw = floyd_warshall(edges, n)
        assert has_neg_cycle_fw, (
            f"Floyd-Warshall failed to detect a negative cycle (test {i})!\n"
            f"Cycle introduced on nodes: {nodes_in_cycle}"
        )

    print("Floyd-Warshall Algorithm: All tests passed!")


if __name__ == "__main__":
    run_test()
