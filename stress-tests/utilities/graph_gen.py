"""
@description
This module provides utility functions for generating various types of random graphs
for use in stress tests. These generators are essential for testing graph
algorithms against a wide range of inputs.

Key functions:
- generate_tree: Creates a random tree with a specified number of nodes.
- generate_dag: Creates a random Directed Acyclic Graph (DAG).
- generate_graph: Creates a general random graph (directed or undirected,
                  weighted or unweighted).

@notes
- Graphs are typically represented as adjacency lists.
- Node indices are 0-based, from 0 to n-1.
"""

import random


def generate_tree(n, weighted=False, min_weight=1, max_weight=100):
    """
    Generates a random tree with n nodes.

    A tree with n nodes has exactly n-1 edges. This function creates a connected
    graph with no cycles by connecting each new node to a random existing node.

    Args:
        n (int): The number of nodes in the tree. Must be >= 1.
        weighted (bool): If True, edges will have random integer weights.
        min_weight (int): Minimum weight for edges if weighted.
        max_weight (int): Maximum weight for edges if weighted.

    Returns:
        list[list]: An adjacency list representation of the tree.
                    If weighted, each entry is a tuple (neighbor, weight).
                    Otherwise, it's just the neighbor index.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[]]

    adj = [[] for _ in range(n)]
    nodes = list(range(n))
    random.shuffle(nodes)  # Randomize node labels to avoid trivial trees

    for i in range(1, n):
        u, v = nodes[i], nodes[random.randint(0, i - 1)]
        if weighted:
            weight = random.randint(min_weight, max_weight)
            adj[u].append((v, weight))
            adj[v].append((u, weight))
        else:
            adj[u].append(v)
            adj[v].append(u)
    return adj


def generate_dag(n, m, weighted=False, min_weight=1, max_weight=100):
    """
    Generates a random Directed Acyclic Graph (DAG) with n nodes and m edges.

    This is achieved by ensuring all edges (u, v) satisfy u < v after nodes
    are topologically sorted (or in this case, simply by index). This guarantees
    no cycles.

    Args:
        n (int): The number of nodes in the DAG.
        m (int): The number of edges in the DAG.
        weighted (bool): If True, edges will have random integer weights.
        min_weight (int): Minimum weight for edges if weighted.
        max_weight (int): Maximum weight for edges if weighted.

    Returns:
        list[list]: An adjacency list representation of the DAG.
    """
    if n == 0:
        return []

    adj = [[] for _ in range(n)]
    edges = set()
    max_edges = n * (n - 1) // 2
    m = min(m, max_edges)

    while len(edges) < m:
        u = random.randint(0, n - 2)
        v = random.randint(u + 1, n - 1)
        if (u, v) not in edges:
            edges.add((u, v))
            if weighted:
                weight = random.randint(min_weight, max_weight)
                adj[u].append((v, weight))
            else:
                adj[u].append(v)
    return adj


def generate_graph(
    n, m, directed=False, weighted=False, self_loops=False, min_weight=1, max_weight=100
):
    """
    Generates a general random graph with n nodes and m edges.

    Args:
        n (int): The number of nodes.
        m (int): The number of edges.
        directed (bool): If True, the graph is directed.
        weighted (bool): If True, edges have random weights.
        self_loops (bool): If True, self-loops (u, u) are allowed.
        min_weight (int): Minimum weight for edges.
        max_weight (int): Maximum weight for edges.

    Returns:
        list[list]: An adjacency list representation of the graph.
    """
    if n == 0:
        return []

    adj = [[] for _ in range(n)]
    edges = set()
    edge_count = 0

    # To avoid an infinite loop for dense graphs, we cap the attempts
    max_attempts = m * 5
    attempts = 0

    while edge_count < m and attempts < max_attempts:
        attempts += 1
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)

        if not self_loops and u == v:
            continue

        # For undirected graphs, store edges canonically (min, max) to detect duplicates
        edge = tuple(sorted((u, v))) if not directed else (u, v)
        if edge in edges:
            continue

        edges.add(edge)
        edge_count += 1

        if weighted:
            weight = random.randint(min_weight, max_weight)
            adj[u].append((v, weight))
            if not directed:
                adj[v].append((u, weight))
        else:
            adj[u].append(v)
            if not directed:
                adj[v].append(u)
    return adj
