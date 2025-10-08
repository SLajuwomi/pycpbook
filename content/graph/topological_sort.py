"""
Implements Topological Sort for a Directed Acyclic Graph (DAG).
A topological sort or topological ordering of a DAG is a linear ordering of its
vertices such that for every directed edge from vertex `u` to vertex `v`, `u`
comes before `v` in the ordering.
This implementation uses Kahn's algorithm, which is BFS-based. The algorithm
proceeds as follows:
1. Compute the in-degree (number of incoming edges) for each vertex.
2. Initialize a queue with all vertices that have an in-degree of 0. These are
   the starting points of the graph.
3. While the queue is not empty, dequeue a vertex `u`. Add `u` to the result list.
4. For each neighbor `v` of `u`, decrement its in-degree. If the in-degree of
   `v` becomes 0, it means all its prerequisites have been met, so enqueue `v`.
5. After the loop, if the number of vertices in the result list is equal to the
   total number of vertices in the graph, the list represents a valid topological
   sort. If the count is less, it indicates that the graph contains at least one
   cycle, and a topological sort is not possible. In such a case, this function
   returns an empty list.
Each vertex is enqueued and dequeued once, and every edge is processed once.
"""

from collections import deque


def topological_sort(adj, n):
    """
    Performs a topological sort on a directed graph.

    Args:
        adj (list[list[int]]): The adjacency list representation of the graph.
        n (int): The total number of nodes in the graph.

    Returns:
        list[int]: A list of nodes in topological order. Returns an empty list
                   if the graph contains a cycle.
    """
    if n == 0:
        return []

    in_degree = [0] * n
    for u in range(n):
        for v in adj[u]:
            in_degree[v] += 1

    q = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []

    while q:
        u = q.popleft()
        topo_order.append(u)

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(topo_order) == n:
        return topo_order
    else:
        # Graph has a cycle
        return []
