"""
Author: PyCPBook Community
Source: CP-Algorithms, USACO Guide
Description: Implements an algorithm to find the maximum matching in a bipartite
graph. A bipartite graph is one whose vertices can be divided into two disjoint
and independent sets, U and V, such that every edge connects a vertex in U to
one in V. A matching is a set of edges without common vertices. The goal is to
find a matching with the maximum possible number of edges.

This implementation uses the augmenting path algorithm, a common approach based on
Ford-Fulkerson. It works by repeatedly finding "augmenting paths" in the graph.
An augmenting path is a path that starts from an unmatched vertex in the left
partition (U), ends at an unmatched vertex in the right partition (V), and
alternates between edges that are not in the current matching and edges that are.

The algorithm proceeds as follows:
1.  Initialize an empty matching.
2.  For each vertex `u` in the left partition U:
    a. Try to find an augmenting path starting from `u` using a Depth-First
       Search (DFS).
    b. The DFS explores neighbors `v` of `u`. If `v` is unmatched, we have found
       an augmenting path of length 1. We match `u` with `v`.
    c. If `v` is already matched with some vertex `u'`, the DFS recursively
       tries to find an alternative match for `u'`. If it succeeds, we can then
       match `u` with `v`.
3.  If an augmenting path is found, the size of the matching increases by one.
    The edges in the matching are updated by "flipping" the status of edges
    along the path.
4.  The process continues until no more augmenting paths can be found. The size
    of the resulting matching is the maximum possible.

Time: $O(E \\cdot V)$, where $V = |U| + |V|$ is the total number of vertices and
$E$ is the number of edges. For each vertex in U, we may perform a DFS that
traverses the entire graph.
Space: $O(V)$ to store the matching and visited arrays for the DFS.
Status: Stress-tested
"""


def bipartite_matching(adj, n1, n2):
    """
    Finds the maximum matching in a bipartite graph.

    Args:
        adj (list[list[int]]): Adjacency list for the left partition.
            `adj[u]` contains a list of neighbors of node `u` (from the left set)
            in the right set. Nodes in the left set are indexed 0 to n1-1.
            Nodes in the right set are indexed 0 to n2-1.
        n1 (int): The number of vertices in the left partition.
        n2 (int): The number of vertices in the right partition.

    Returns:
        int: The size of the maximum matching.
    """
    match_right = [-1] * n2
    matching_size = 0

    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_right[v] < 0 or dfs(match_right[v], visited):
                    match_right[v] = u
                    return True
        return False

    for u in range(n1):
        visited = [False] * n2
        if dfs(u, visited):
            matching_size += 1

    return matching_size
