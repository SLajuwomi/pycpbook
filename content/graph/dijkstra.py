"""
Implements Dijkstra's algorithm for finding the single-source
shortest paths in a weighted graph with non-negative edge weights.
Dijkstra's algorithm maintains a set of visited vertices and finds the shortest
path from a source vertex to all other vertices in the graph. It uses a priority
queue to greedily select the unvisited vertex with the smallest distance from
the source.
The algorithm proceeds as follows:
1. Initialize a distances array with infinity for all vertices except the source,
   which is set to 0.
2. Initialize a priority queue and add the source vertex with a distance of 0.
3. While the priority queue is not empty, extract the vertex `u` with the
   smallest distance.
4. If `u` has already been processed with a shorter path, skip it.
5. For each neighbor `v` of `u`, calculate the distance through `u`. If this
   new path is shorter than the known distance to `v`, update the distance and
   add `v` to the priority queue with its new, shorter distance.
This implementation uses Python's `heapq` module as a min-priority queue.
The graph is represented by an adjacency list where each entry is a tuple
(neighbor, weight).
of edges. The log factor comes from the priority queue operations.
priority queue.
"""

import heapq


def dijkstra(adj, start_node, n):
    """
    Finds the shortest paths from a start node to all other nodes in a graph.

    Args:
        adj (list[list[tuple[int, int]]]): The adjacency list representation of
            the graph. adj[u] contains tuples (v, weight) for edges u -> v.
        start_node (int): The node from which to start the search.
        n (int): The total number of nodes in the graph.

    Returns:
        list[float]: A list of shortest distances from the start_node to each
                     node. `float('inf')` indicates an unreachable node.
    """
    if not (0 <= start_node < n):
        return [float("inf")] * n

    dist = [float("inf")] * n
    dist[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist
