"""
Author: PyCPBook Community
Source: Based on common implementations in competitive programming resources
Description: Implements the Union-Find data structure, also known as
Disjoint Set Union (DSU). It is used to keep track of a partition of a set
of elements into a number of disjoint, non-overlapping subsets. The two primary
operations are finding the representative (or root) of a set and merging two sets.

This implementation includes two key optimizations:
1.  Path Compression: During a `find` operation, it makes every node on the
    path from the query node to the root point directly to the root. This
    dramatically flattens the tree structure.
2.  Union by Size: During a `union` operation, it always attaches the root of
    the smaller tree to the root of the larger tree. This helps in keeping
    the trees shallow, which speeds up future `find` operations.

The combination of these two techniques makes the amortized time complexity
of both `find` and `union` operations nearly constant.
Time: $O(\\alpha(N))$ on average for both find and union operations, where $\\alpha$
is the extremely slow-growing inverse Ackermann function. For all practical
purposes, this is considered constant time.
Space: $O(N)$ to store the parent and size arrays for N elements.
Status: Stress-tested
"""


class UnionFind:
    """
    A class that implements the Union-Find data structure with path compression
    and union by size optimizations.
    """

    def __init__(self, n):
        """
        Initializes the Union-Find structure for n elements, where each element
        is initially in its own set.
        Args:
            n (int): The number of elements.
        """
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        """
        Finds the representative (root) of the set containing element i.
        Applies path compression along the way.
        Args:
            i (int): The element to find.
        Returns:
            int: The representative of the set containing i.
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Merges the sets containing elements i and j.
        Applies union by size.
        Args:
            i (int): An element in the first set.
            j (int): An element in the second set.
        Returns:
            bool: True if the sets were merged, False if they were already in the same set.
        """
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False
