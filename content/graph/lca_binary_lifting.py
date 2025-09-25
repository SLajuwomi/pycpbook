"""
Author: PyCPBook Community
Source: CP-Algorithms, USACO Guide
Description: Implements Lowest Common Ancestor (LCA) queries on a tree using the
binary lifting technique. This method allows for finding the LCA of any two nodes
in logarithmic time after a precomputation step.

The algorithm consists of two main parts:
1.  Precomputation:
    - A Depth-First Search (DFS) is performed from the root of the tree to
      calculate the depth of each node and to determine the immediate parent
      of each node.
    - A table `up[i][j]` is built, where `up[i][j]` stores the `2^j`-th ancestor
      of node `i`. This table is filled using dynamic programming: the `2^j`-th
      ancestor of `i` is the `2^(j-1)`-th ancestor of its `2^(j-1)`-th ancestor.
      `up[i][j] = up[up[i][j-1]][j-1]`.

2.  Querying for LCA(u, v):
    - First, the depths of `u` and `v` are equalized by moving the deeper node
      upwards. This is done efficiently by "lifting" it in jumps of powers of two.
    - If `u` and `v` become the same node, that node is the LCA.
    - Otherwise, `u` and `v` are lifted upwards together, step by step, using the
      largest possible jumps (`2^j`) that keep them below their LCA (i.e.,
      `up[u][j] != up[v][j]`).
    - After this process, `u` and `v` will be direct children of the LCA. The
      LCA is then the parent of `u` (or `v`), which is `up[u][0]`.

Time: Precomputation is $O(N \\log N)$. Each query is $O(\\log N)$.
Space: $O(N \\log N)$ to store the `up` table.
Status: Stress-tested
"""


class LCA:
    def __init__(self, n, adj, root=0):
        self.n = n
        self.adj = adj
        self.max_log = (n).bit_length()
        self.depth = [-1] * n
        self.up = [[-1] * self.max_log for _ in range(n)]
        self._dfs(root, -1, 0)
        self._precompute_ancestors()

    def _dfs(self, u, p, d):
        self.depth[u] = d
        self.up[u][0] = p
        for v in self.adj[u]:
            if v != p:
                self._dfs(v, u, d + 1)

    def _precompute_ancestors(self):
        for j in range(1, self.max_log):
            for i in range(self.n):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]

    def query(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        for j in range(self.max_log - 1, -1, -1):
            if self.depth[u] - (1 << j) >= self.depth[v]:
                u = self.up[u][j]

        if u == v:
            return u

        for j in range(self.max_log - 1, -1, -1):
            if self.up[u][j] != -1 and self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        return self.up[u][0]
