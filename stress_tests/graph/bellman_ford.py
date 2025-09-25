"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the Bellman-Ford algorithm.
It validates the correctness of the `bellman_ford` function by comparing its
results against a simpler, but much slower, naive shortest path algorithm.
It also specifically tests the negative cycle detection capability.

The test includes two main scenarios:
1.  Graphs without Negative Cycles: A random weighted graph is generated,
    potentially with negative edge weights but guaranteed to have no negative
    cycles. The results from `bellman_ford` are compared against a naive
    implementation that repeatedly relaxes all edges until no more changes
    occur.
2.  Graphs with Negative Cycles: A random graph is generated, and then a
    negative-weight cycle is deliberately introduced. The test asserts that
    the `bellman_ford` function correctly reports the presence of a negative
    cycle.

This ensures that the Bellman-Ford implementation is correct for its primary
use cases: finding shortest paths in graphs with negative weights and detecting
negative cycles.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.bellman_ford import bellman_ford
from stress_tests.utilities.graph_gen import generate_graph


def naive_sssp(edges, start_node, n):
    """
    A very simple, but correct, shortest path algorithm for validation.
    It repeatedly relaxes edges until no distances change. It does not
    efficiently detect negative cycles but will converge to correct distances
    if none exist.
    """
    dist = [float("inf")] * n
    if not (0 <= start_node < n):
        return dist
    dist[start_node] = 0

    for _ in range(n):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


def run_test():
    """
    Performs a stress test on the Bellman-Ford implementation.
    """
    ITERATIONS = 200
    MAX_N = 30
    MAX_M_FACTOR = 2.0
    MAX_WEIGHT = 100

    # Test on graphs without negative cycles
    for i in range(ITERATIONS):
        n = random.randint(1, MAX_N)
        max_m = int(n * (n - 1) * MAX_M_FACTOR) if n > 1 else 0
        m = random.randint(0, max_m)

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

        start_node = random.randint(0, n - 1)

        dist_bf, has_neg_cycle = bellman_ford(edges, start_node, n)

        if not has_neg_cycle:
            dist_naive = naive_sssp(edges, start_node, n)
            assert dist_bf == dist_naive, (
                f"Bellman-Ford failed on graph without negative cycle (test {i})!\n"
                f"Graph (n={n}, m={m}, start={start_node}): {edges}\n"
                f"Expected (Naive): {dist_naive}\n"
                f"Got (Bellman-Ford): {dist_bf}"
            )

    # Test on graphs with negative cycles
    for i in range(ITERATIONS):
        n = random.randint(3, MAX_N)
        max_m = int(n * (n - 1) * MAX_M_FACTOR) if n > 1 else 0
        m = random.randint(n, max_m)

        adj = generate_graph(
            n, m, directed=True, weighted=True, min_weight=1, max_weight=MAX_WEIGHT
        )

        nodes_in_cycle = random.sample(range(n), 3)
        c1, c2, c3 = nodes_in_cycle
        adj[c1].append((c2, 1))
        adj[c2].append((c3, 1))
        adj[c3].append((c1, -100))

        edges = []
        for u, neighbors in enumerate(adj):
            for v, w in neighbors:
                edges.append((u, v, w))

        start_node = random.randint(0, n - 1)

        cycle_in_graph = False
        for start in range(n):
            _, detected = bellman_ford(edges, start, n)
            if detected:
                cycle_in_graph = True
                break

        assert cycle_in_graph, (
            f"Bellman-Ford failed to detect a negative cycle (test {i})!\n"
            f"Graph (n={n}, m={m}): {edges}\n"
            f"Cycle introduced on nodes: {nodes_in_cycle}"
        )

    print("Bellman-Ford Algorithm: All tests passed!")


if __name__ == "__main__":
    run_test()
