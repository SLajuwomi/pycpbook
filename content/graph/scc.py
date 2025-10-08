"""
Implements Tarjan's algorithm for finding Strongly Connected
Components (SCCs) in a directed graph. An SCC is a maximal subgraph where for
any two vertices u and v in the subgraph, there is a path from u to v and a
path from v to u.
Tarjan's algorithm performs a single Depth-First Search (DFS) from an arbitrary
start node. It maintains two key values for each vertex `u`:
1. `disc[u]`: The discovery time of `u`, which is the time (a counter) when `u`
   is first visited.
2. `low[u]`: The "low-link" value of `u`, which is the lowest discovery time
   reachable from `u` (including itself) through its DFS subtree, possibly
   including one back-edge.
The algorithm also uses a stack to keep track of the nodes in the current
exploration path. A node `u` is the root of an SCC if its discovery time is
equal to its low-link value (`disc[u] == low[u]`). When such a node is found,
all nodes in its SCC are on the top of the stack and can be popped off until
`u` is reached. These popped nodes form one complete SCC.
edges, because the algorithm is based on a single DFS traversal.
the recursion depth of the DFS.
"""


def find_sccs(adj, n):
    """
    Finds all Strongly Connected Components of a directed graph using Tarjan's algorithm.

    Args:
        adj (list[list[int]]): The adjacency list representation of the graph.
        n (int): The total number of nodes in the graph.

    Returns:
        list[list[int]]: A list of lists, where each inner list contains the
                         nodes of a single Strongly Connected Component.
    """
    if n == 0:
        return []

    disc = [-1] * n
    low = [-1] * n
    on_stack = [False] * n
    stack = []
    time = 0
    sccs = []

    def tarjan_dfs(u):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if disc[v] == -1:
                tarjan_dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])

        if low[u] == disc[u]:
            component = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                component.append(node)
                if node == u:
                    break
            sccs.append(component)

    for i in range(n):
        if disc[i] == -1:
            tarjan_dfs(i)

    return sccs
