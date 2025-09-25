"""
Author: PyCPBook Community
Source: Introduction to Algorithms (CLRS)
Description: Implements the Floyd-Warshall algorithm for finding all-pairs
shortest paths in a weighted directed graph. This algorithm can handle graphs
with negative edge weights.

The algorithm is based on a dynamic programming approach. It iteratively considers
each vertex `k` and updates the shortest path between all pairs of vertices `(i, j)`
to see if a path through `k` is shorter. The core recurrence is:
`dist(i, j) = min(dist(i, j), dist(i, k) + dist(k, j))`

After running the algorithm with all vertices `k` from 0 to `V-1`, the resulting
distance matrix contains the shortest paths between all pairs of vertices.

A key feature of Floyd-Warshall is its ability to detect negative-weight cycles.
If, after the algorithm completes, the distance from any vertex `i` to itself
(`dist[i][i]`) is negative, it indicates that there is a negative-weight cycle
reachable from `i`.

This implementation takes an edge list as input, builds an adjacency matrix,
runs the algorithm, and then checks for negative cycles.

Time: $O(V^3)$, where $V$ is the number of vertices. The three nested loops
dominate the runtime.
Space: $O(V^2)$ to store the distance matrix.
Status: Stress-tested
"""


def floyd_warshall(edges, n):
    """
    Finds all-pairs shortest paths in a graph using the Floyd-Warshall algorithm.

    Args:
        edges (list[tuple[int, int, int]]): A list of all edges in the graph,
            where each tuple is (u, v, weight) for an edge u -> v.
        n (int): The total number of nodes in the graph.

    Returns:
        tuple[list[list[float]], bool]: A tuple containing:
            - A 2D list of shortest distances. `dist[i][j]` is the shortest
              distance from node `i` to node `j`. `float('inf')` for unreachable pairs.
            - A boolean that is True if a negative cycle is detected, False otherwise.
    """
    if n == 0:
        return [], False

    dist = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    has_negative_cycle = False
    for i in range(n):
        if dist[i][i] < 0:
            has_negative_cycle = True
            break

    return dist, has_negative_cycle
