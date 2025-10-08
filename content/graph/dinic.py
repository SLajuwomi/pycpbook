"""
Implements Dinic's algorithm for computing the maximum flow in a
flow network from a source `s` to a sink `t`. Dinic's is one of the most
efficient algorithms for this problem.
The algorithm operates in phases. In each phase, it does the following:
1.  Build a "level graph" using a Breadth-First Search (BFS) from the source `s`
    on the residual graph. The level of a vertex is its shortest distance from `s`.
    The level graph only contains edges `(u, v)` where `level[v] == level[u] + 1`.
    If the sink `t` is not reachable from `s` in the residual graph, the algorithm
    terminates.
2.  Find a "blocking flow" in the level graph using a Depth-First Search (DFS)
    from `s`. A blocking flow is a flow where every path from `s` to `t` in the
    level graph has at least one saturated edge. The DFS pushes as much flow as
    possible along paths from `s` to `t`. Pointers are used to avoid re-exploring
    dead-end paths within the same phase.
3.  Add the blocking flow found in the phase to the total maximum flow.
The process is repeated until the sink is no longer reachable from the source.
such as $O(E \\sqrt{V})$ for bipartite matching and $O(E \\min(V^{2/3}, E^{1/2}))$
for unit-capacity networks.
"""

from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [-1] * n
        self.ptr = [0] * n
        self.inf = float("inf")

    def add_edge(self, u, v, cap):
        # Forward edge
        self.graph[u].append([v, cap, len(self.graph[v])])
        # Backward edge
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def _bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for i in range(len(self.graph[u])):
                v, cap, rev = self.graph[u][i]
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1

    def _dfs(self, u, t, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed

        while self.ptr[u] < len(self.graph[u]):
            edge_idx = self.ptr[u]
            v, cap, rev_idx = self.graph[u][edge_idx]

            if self.level[v] != self.level[u] + 1 or cap == 0:
                self.ptr[u] += 1
                continue

            tr = self._dfs(v, t, min(pushed, cap))
            if tr == 0:
                self.ptr[u] += 1
                continue

            self.graph[u][edge_idx][1] -= tr
            self.graph[v][rev_idx][1] += tr
            return tr
        return 0

    def max_flow(self, s, t):
        if s == t:
            return 0
        total_flow = 0
        while self._bfs(s, t):
            self.ptr = [0] * self.n
            pushed = self._dfs(s, t, self.inf)
            while pushed > 0:
                total_flow += pushed
                pushed = self._dfs(s, t, self.inf)
        return total_flow
