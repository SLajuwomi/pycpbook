"""
Author: PyCPBook Community
Source: Introduction to Algorithms (CLRS)
Description: This file implements Breadth-First Search (BFS) and Depth-First Search (DFS),
the two most fundamental graph traversal algorithms.

Breadth-First Search (BFS):
BFS explores a graph layer by layer from a starting source node. It finds all
nodes at a distance of 1 from the source, then all nodes at a distance of 2,
and so on. It's guaranteed to find the shortest path from the source to any
other node in an unweighted graph. The algorithm proceeds as follows:
1. Initialize a queue and add the `start_node` to it.
2. Initialize a `visited` array or set to keep track of visited nodes, marking
   the `start_node` as visited.
3. While the queue is not empty, dequeue a node `u`.
4. For each neighbor `v` of `u`, if `v` has not been visited, mark `v` as
   visited and enqueue it.
5. Repeat until the queue is empty. The collection of dequeued nodes forms the
   traversal order.

Depth-First Search (DFS):
DFS explores a graph by traversing as far as possible along each branch before
backtracking. It's commonly used for tasks like cycle detection, topological
sorting, and finding connected components. The iterative algorithm is as follows:
1. Initialize a stack and push the `start_node` onto it.
2. Initialize a `visited` array or set, marking the `start_node` as visited.
3. While the stack is not empty, pop a node `u`.
4. For each neighbor `v` of `u`, if `v` has not been visited, mark `v` as
   visited and push it onto the stack.
5. Repeat until the stack is empty. The collection of popped nodes forms the
   traversal order.

Time: $O(V + E)$ for both BFS and DFS, where $V$ is the number of vertices and
$E$ is the number of edges. Each vertex and edge is visited exactly once.
Space: $O(V)$ in the worst case for storing the queue (BFS) or stack (DFS),
and the visited array.
Status: Stress-tested
"""

from collections import deque


def bfs(adj, start_node, n):
    """
    Performs a Breadth-First Search on a graph.

    Args:
        adj (list[list[int]]): The adjacency list representation of the graph.
        start_node (int): The node from which to start the traversal.
        n (int): The total number of nodes in the graph.

    Returns:
        list[int]: A list of nodes in the order they were visited.
    """
    if not (0 <= start_node < n):
        return []

    q = deque([start_node])
    visited = [False] * n
    visited[start_node] = True
    traversal_order = []

    while q:
        u = q.popleft()
        traversal_order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return traversal_order


def dfs(adj, start_node, n):
    """
    Performs a Depth-First Search on a graph.

    Args:
        adj (list[list[int]]): The adjacency list representation of the graph.
        start_node (int): The node from which to start the traversal.
        n (int): The total number of nodes in the graph.

    Returns:
        list[int]: A list of nodes in the order they were visited.
    """
    if not (0 <= start_node < n):
        return []

    stack = [start_node]
    visited = [False] * n
    # Mark as visited when pushed to stack to avoid re-adding
    visited[start_node] = True
    traversal_order = []

    # This loop produces a traversal order different from the recursive one.
    # To get a more standard pre-order traversal iteratively, we need a slight change.

    # Reset for a more standard iterative DFS traversal order
    visited = [False] * n
    stack = [start_node]

    while stack:
        u = stack.pop()

        if not visited[u]:
            visited[u] = True
            traversal_order.append(u)

            # Add neighbors to the stack in reverse order to process them in lexicographical order
            for v in reversed(adj[u]):
                if not visited[v]:
                    stack.append(v)

    return traversal_order
