"""
Author: PyCPBook Community
Source: Self-written for PyCPBook project
Description: This script is a stress test for the Minimum Spanning Tree (MST)
algorithms: Prim's and Kruskal's. It validates their correctness by comparing
their outputs on randomly generated, weighted, undirected graphs.

The core testing strategy is as follows:
1.  Generate a random, connected, weighted, undirected graph. To guarantee
    connectivity, a random tree is first generated, and then additional random
    edges are added to create cycles.
2.  Prepare the graph data in two formats: an adjacency list for Prim's
    algorithm and an edge list for Kruskal's algorithm.
3.  Run both `prim` and `kruskal` on the same graph.
4.  Assert that the total weight of the MST calculated by both algorithms is
    identical. Since the MST weight for a given graph is unique (even if the
    set of edges in the MST is not), this is a very strong correctness check.

This process is repeated for many iterations with varying graph sizes to ensure
both implementations are robust and reliable.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.graph.prim_kruskal import prim, kruskal
from stress_tests.utilities.graph_gen import generate_tree


def run_test():
    """
    Performs a stress test on the Prim's and Kruskal's MST implementations.
    """
    ITERATIONS = 200
    MAX_N = 50
    MAX_EXTRA_EDGES = 25
    MAX_WEIGHT = 1000

    for i in range(ITERATIONS):
        n = random.randint(2, MAX_N)

        # 1. Generate a connected graph
        # Start with a tree to guarantee connectivity
        adj = generate_tree(n, weighted=True, min_weight=1, max_weight=MAX_WEIGHT)
        edges = set()
        for u, neighbors in enumerate(adj):
            for v, w in neighbors:
                if u < v:
                    edges.add((u, v, w))

        # Add extra edges to create cycles
        num_extra_edges = random.randint(0, MAX_EXTRA_EDGES)
        for _ in range(num_extra_edges):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u != v:
                # Check if edge already exists
                edge_exists = False
                for neighbor, _ in adj[u]:
                    if neighbor == v:
                        edge_exists = True
                        break
                if not edge_exists:
                    w = random.randint(1, MAX_WEIGHT)
                    adj[u].append((v, w))
                    adj[v].append((u, w))
                    edges.add(tuple(sorted((u, v))) + (w,))

        edge_list = list(edges)

        # 2. Run both algorithms
        mst_weight_prim, _ = prim(adj, n)
        mst_weight_kruskal, _ = kruskal(edge_list, n)

        # 3. Assert that the total weights are equal
        assert mst_weight_prim == mst_weight_kruskal, (
            f"MST weight mismatch on iteration {i} for a graph with {n} nodes!\n"
            f"Prim's result: {mst_weight_prim}\n"
            f"Kruskal's result: {mst_weight_kruskal}\n"
            f"Graph edges: {edge_list}"
        )

    print("MST Algorithms (Prim's & Kruskal's): All tests passed!")


if __name__ == "__main__":
    run_test()
