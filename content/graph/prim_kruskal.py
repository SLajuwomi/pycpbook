"""
This file implements two classic greedy algorithms for finding the
Minimum Spanning Tree (MST) of an undirected, weighted graph: Kruskal's algorithm
and Prim's algorithm. An MST is a subset of the edges of a connected,
edge-weighted undirected graph that connects all the vertices together, without
any cycles and with the minimum possible total edge weight.
Kruskal's Algorithm:
This algorithm treats the graph as a forest and each node as an individual tree.
It sorts all the edges by weight in non-decreasing order. Then, it iterates
through the sorted edges, adding an edge to the MST if and only if it does not
form a cycle with the edges already added. A Union-Find data structure is used
to efficiently detect cycles. The algorithm terminates when V-1 edges have been
added to the MST (for a connected graph).
Prim's Algorithm:
This algorithm grows the MST from an arbitrary starting vertex. It maintains a
set of vertices already in the MST. At each step, it finds the minimum-weight
edge that connects a vertex in the MST to a vertex outside the MST and adds this
edge and vertex to the tree. A priority queue is used to efficiently select this
minimum-weight edge.
- Kruskal's: $O(E \\log E)$ or $O(E \\log V)$, dominated by sorting the edges.
- Prim's: $O(E \\log V)$ using a binary heap as a priority queue.
- Kruskal's: $O(V + E)$ for the edge list and Union-Find structure.
- Prim's: $O(V + E)$ for the adjacency list, priority queue, and visited array.
"""

import heapq
import sys
import os

# Add content directory to path to import the solution
sys.path.append(
    os.path.join(os.path.dirname(__file__), "../../content/data_structures")
)
from union_find import UnionFind


def kruskal(edges, n):
    """
    Finds the MST of a graph using Kruskal's algorithm.

    Args:
        edges (list[tuple[int, int, int]]): A list of all edges in the graph,
            where each tuple is (u, v, weight).
        n (int): The total number of nodes in the graph.

    Returns:
        tuple[int, list[tuple[int, int, int]]]: A tuple containing:
            - The total weight of the MST.
            - A list of edges (u, v, weight) that form the MST.
            Returns (inf, []) if the graph is not connected and cannot form a single MST.
    """
    if n == 0:
        return 0, []

    sorted_edges = sorted([(w, u, v) for u, v, w in edges])
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    for weight, u, v in sorted_edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break

    if len(mst_edges) < n - 1:
        # This indicates the graph is not connected.
        # The result is a minimum spanning forest.
        pass

    return mst_weight, mst_edges


def prim(adj, n, start_node=0):
    """
    Finds the MST of a graph using Prim's algorithm.

    Args:
        adj (list[list[tuple[int, int]]]): The adjacency list representation of
            the graph. adj[u] contains tuples (v, weight) for edges u -> v.
        n (int): The total number of nodes in the graph.
        start_node (int): The node to start building the MST from.

    Returns:
        tuple[int, list[tuple[int, int, int]]]: A tuple containing:
            - The total weight of the MST.
            - A list of edges (u, v, weight) that form the MST.
            Returns (inf, []) if the graph is not connected.
    """
    if n == 0:
        return 0, []
    if not (0 <= start_node < n):
        return float("inf"), []

    visited = [False] * n
    pq = [(0, start_node, -1)]  # (weight, current_node, previous_node)
    mst_weight = 0
    mst_edges = []
    edges_count = 0

    while pq and edges_count < n:
        weight, u, prev = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        mst_weight += weight
        if prev != -1:
            mst_edges.append((prev, u, weight))
        edges_count += 1

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v, u))

    if edges_count < n:
        # This indicates the graph is not connected.
        return float("inf"), []

    return mst_weight, mst_edges
