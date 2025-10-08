"""
Implements the Bellman-Ford algorithm for finding the single-source
shortest paths in a weighted graph. Unlike Dijkstra's algorithm, Bellman-Ford
can handle graphs with negative edge weights.
The algorithm works by iteratively relaxing edges. It repeats a relaxation step
$V-1$ times, where $V$ is the number of vertices. In each relaxation step, it
iterates through all edges `(u, v)` and updates the distance to `v` if a shorter
path is found through `u`. After $V-1$ iterations, the shortest paths are
guaranteed to be found, provided there are no negative-weight cycles reachable
from the source.
A final, $V$-th iteration is performed to detect negative-weight cycles. If any
distance can still be improved during this iteration, it means a negative-weight
cycle exists, and the shortest paths are not well-defined (they can be infinitely
small).
This implementation takes an edge list as input, which is a common and convenient
representation for this algorithm.
of edges. The algorithm iterates through all edges $V$ times.
"""


def bellman_ford(edges, start_node, n):
    """
    Finds shortest paths from a start node, handling negative weights and
    detecting negative cycles.

    Args:
        edges (list[tuple[int, int, int]]): A list of all edges in the graph,
            where each tuple is (u, v, weight) for an edge u -> v.
        start_node (int): The node from which to start the search.
        n (int): The total number of nodes in the graph.

    Returns:
        tuple[list[float], bool]: A tuple containing:
            - A list of shortest distances. `float('inf')` for unreachable nodes.
            - A boolean that is True if a negative cycle is detected, False otherwise.
    """
    if not (0 <= start_node < n):
        return [float("inf")] * n, False

    dist = [float("inf")] * n
    dist[start_node] = 0

    for i in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            return dist, True

    return dist, False
