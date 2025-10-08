"""
Implements a Segment Tree with lazy propagation. This powerful
data structure is designed to handle range updates and range queries efficiently.
While a standard Segment Tree can perform range queries in $O(\\log N)$ time,
updates are limited to single points. Lazy propagation extends this capability
to allow range updates (e.g., adding a value to all elements in a range)
to also be performed in $O(\\log N)$ time.
The core idea is to postpone updates to tree nodes and apply them only when
necessary. When an update is requested for a range `[l, r]`, we traverse the
tree. If a node's range is fully contained within `[l, r]`, instead of updating
all its children, we store the pending update value in a `lazy` array for that
node and update the node's main value. We then stop traversing down that path.
This pending update is "pushed" down to its children only when a future query
or update needs to access one of the children.
This implementation supports range addition updates and range sum queries.
The logic can be adapted for other associative operations like range minimum/maximum
and range assignment.
The initial `build` operation takes $O(N)$ time.
to be safe for a complete binary tree representation.
"""


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.arr = arr
        self._build(1, 0, self.n - 1)

    def _build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            self._build(2 * v, tl, tm)
            self._build(2 * v + 1, tm + 1, tr)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def _push(self, v, tl, tr):
        if self.lazy[v] == 0:
            return

        range_len = tr - tl + 1
        self.tree[v] += self.lazy[v] * range_len

        if tl != tr:
            self.lazy[2 * v] += self.lazy[v]
            self.lazy[2 * v + 1] += self.lazy[v]

        self.lazy[v] = 0

    def _update(self, v, tl, tr, l, r, addval):
        self._push(v, tl, tr)
        if l > r:
            return
        if l == tl and r == tr:
            self.lazy[v] += addval
            self._push(v, tl, tr)
        else:
            tm = (tl + tr) // 2
            self._update(2 * v, tl, tm, l, min(r, tm), addval)
            self._update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, addval)

            # After children are updated, update self based on pushed children
            self._push(2 * v, tl, tm)
            self._push(2 * v + 1, tm + 1, tr)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def _query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        self._push(v, tl, tr)
        if l == tl and r == tr:
            return self.tree[v]

        tm = (tl + tr) // 2
        left_sum = self._query(2 * v, tl, tm, l, min(r, tm))
        right_sum = self._query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)
        return left_sum + right_sum

    def update(self, l, r, addval):
        # Updates range [l, r] (inclusive)
        if l > r:
            return
        self._update(1, 0, self.n - 1, l, r, addval)

    def query(self, l, r):
        # Queries range [l, r] (inclusive)
        if l > r:
            return 0
        return self._query(1, 0, self.n - 1, l, r)
