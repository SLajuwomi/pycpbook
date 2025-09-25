"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for Dinic's maximum flow algorithm.
It validates the correctness of the `Dinic` class by comparing its results
against a simpler, but slower, max-flow algorithm: Edmonds-Karp.

The test operates as follows:
1.  A naive implementation of the Edmonds-Karp algorithm is provided. It works
    by repeatedly finding any augmenting path in the residual graph using BFS
    and pushing flow along it.
2.  A random directed graph with random edge capacities is generated.
3.  A random source `s` and sink `t` are chosen.
4.  The `Dinic` class and the naive Edmonds-Karp solver are both used to
    compute the maximum flow from `s` to `t` on the same graph.
5.  The results are asserted to be identical. If they differ, the test fails
    and prints the details of the failing graph and parameters.

This process is repeated for many iterations with varying graph sizes and
structures to ensure the robust correctness of the Dinic's implementation.
"""

import sys
import os
import random
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.dinic import Dinic
from stress_tests.utilities.graph_gen import generate_graph


class EdmondsKarp:
    """
    A naive implementation of the Edmonds-Karp algorithm for max flow.
    This serves as the ground truth for validating the Dinic's implementation.
    Time complexity is O(V * E^2).
    """

    def __init__(self, n):
        self.n = n
        self.capacity = [[0] * n for _ in range(n)]
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[u][v] = cap

    def _bfs(self, s, t, parent):
        visited = [False] * self.n
        q = deque([s])
        visited[s] = True
        parent[s] = -1

        while q:
            u = q.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.capacity[u][v] > 0:
                    q.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def max_flow(self, s, t):
        parent = [0] * self.n
        max_flow_val = 0

        while self._bfs(s, t, parent):
            path_flow = float("inf")
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = parent[v]

            v = t
            while v != s:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                v = parent[v]

            max_flow_val += path_flow

        return max_flow_val


def run_test():
    """
    Performs a stress test on the Dinic's max flow implementation.
    """
    ITERATIONS = 100
    MAX_N = 25
    MAX_M_FACTOR = 2.0
    MAX_CAPACITY = 100

    for i in range(ITERATIONS):
        n = random.randint(2, MAX_N)
        max_m = int(n * (n - 1) * MAX_M_FACTOR)
        m = random.randint(1, max_m)

        adj = generate_graph(
            n, m, directed=True, weighted=True, min_weight=1, max_weight=MAX_CAPACITY
        )

        s, t = random.sample(range(n), 2)

        dinic_solver = Dinic(n)
        ek_solver = EdmondsKarp(n)

        edges = []
        for u, neighbors in enumerate(adj):
            for v, cap in neighbors:
                dinic_solver.add_edge(u, v, cap)
                ek_solver.add_edge(u, v, cap)
                edges.append((u, v, cap))

        flow_dinic = dinic_solver.max_flow(s, t)
        flow_ek = ek_solver.max_flow(s, t)

        assert flow_dinic == flow_ek, (
            f"Max flow mismatch on iteration {i}!\n"
            f"Graph (n={n}, m={len(edges)}, s={s}, t={t}): {edges}\n"
            f"Expected (Edmonds-Karp): {flow_ek}\n"
            f"Got (Dinic): {flow_dinic}"
        )

    print("Dinic's Maximum Flow Algorithm: All tests passed!")


if __name__ == "__main__":
    run_test()
