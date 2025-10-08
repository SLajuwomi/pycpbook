"""
Implements Hierholzer's algorithm to find an Eulerian path or cycle
in a graph. An Eulerian path visits every edge of a graph exactly once. An
Eulerian cycle is an Eulerian path that starts and ends at the same vertex.
The existence of an Eulerian path/cycle depends on the degrees of the vertices:
For an undirected graph:
- An Eulerian cycle exists if and only if every vertex has an even degree, and
  all vertices with a non-zero degree belong to a single connected component.
- An Eulerian path exists if and only if there are zero or two vertices of odd
  degree, and all vertices with a non-zero degree belong to a single component.
  If there are two odd-degree vertices, the path must start at one and end at
  the other.
For a directed graph:
- An Eulerian cycle exists if and only if for every vertex, the in-degree equals
  the out-degree, and the graph is strongly connected (ignoring isolated vertices).
- An Eulerian path exists if and only if at most one vertex has
  `out-degree - in-degree = 1` (the start), at most one vertex has
  `in-degree - out-degree = 1` (the end), every other vertex has equal in- and
  out-degrees, and the underlying undirected graph is connected.
Hierholzer's algorithm finds the path by starting a traversal from a valid
starting node. It follows edges until it gets stuck, and then backtracks, forming
the path in reverse. This implementation uses an iterative approach with a stack.
"""

from collections import Counter


def find_euler_path(adj, n, directed=False):
    """
    Finds an Eulerian path or cycle in a graph.

    Args:
        adj (list[list[int]]): The adjacency list representation of the graph.
            Handles multigraphs if neighbors are repeated.
        n (int): The total number of nodes in the graph.
        directed (bool): True if the graph is directed, False otherwise.

    Returns:
        list[int] | None: A list of nodes representing the Eulerian path,
                          or None if no such path exists.
    """
    if n == 0:
        return []

    num_edges = 0
    if directed:
        in_degree = [0] * n
        out_degree = [0] * n
        for u in range(n):
            out_degree[u] = len(adj[u])
            num_edges += len(adj[u])
            for v in adj[u]:
                in_degree[v] += 1

        start_node, end_node_count = -1, 0
        for i in range(n):
            if out_degree[i] - in_degree[i] == 1:
                if start_node != -1:
                    return None
                start_node = i
            elif in_degree[i] - out_degree[i] == 1:
                end_node_count += 1
                if end_node_count > 1:
                    return None
            elif in_degree[i] != out_degree[i]:
                return None

        if start_node == -1:
            for i in range(n):
                if out_degree[i] > 0:
                    start_node = i
                    break
            if start_node == -1:
                return [0] if n > 0 else []

    else:
        degree = [0] * n
        for u in range(n):
            degree[u] = len(adj[u])
            num_edges += len(adj[u])
        num_edges //= 2

        odd_degree_nodes = [i for i, d in enumerate(degree) if d % 2 != 0]
        if len(odd_degree_nodes) > 2:
            return None

        start_node = -1
        if odd_degree_nodes:
            start_node = odd_degree_nodes[0]
        else:
            for i in range(n):
                if degree[i] > 0:
                    start_node = i
                    break
            if start_node == -1:
                return [0] if n > 0 else []

    adj_counts = [Counter(neighbors) for neighbors in adj]
    path = []
    stack = [start_node]

    while stack:
        u = stack[-1]
        if adj_counts[u]:
            v = next(iter(adj_counts[u]))
            adj_counts[u][v] -= 1
            if adj_counts[u][v] == 0:
                del adj_counts[u][v]

            if not directed:
                adj_counts[v][u] -= 1
                if adj_counts[v][u] == 0:
                    del adj_counts[v][u]

            stack.append(v)
        else:
            path.append(stack.pop())

    path.reverse()

    if len(path) == num_edges + 1:
        return path
    else:
        return None
