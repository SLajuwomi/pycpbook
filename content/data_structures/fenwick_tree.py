"""
Implements a 1D Fenwick Tree, also known as a Binary Indexed Tree (BIT).
This data structure is used to efficiently calculate prefix sums (or any other
associative and invertible operation) on an array while supporting point updates.
A Fenwick Tree of size N allows for two main operations, both in logarithmic time:
1.  add(idx, delta): Adds `delta` to the element at index `idx`.
2.  query(right): Computes the sum of the elements in the range [0, right).
The core idea is that any integer can be represented as a sum of powers of two.
Similarly, a prefix sum can be represented as a sum of sums over certain
sub-ranges, where the size of these sub-ranges are powers of two. The tree
stores these precomputed sub-range sums.
This implementation is 0-indexed for user-facing operations, which is a common
convention in Python. The internal logic is adapted to work with this indexing.
- To find the next index to update in `add`, we use `idx |= idx + 1`.
- To find the next index to sum in `query`, we use `idx = (idx & (idx + 1)) - 1`.
"""


class FenwickTree:
    """
    A class that implements a 1D Fenwick Tree (Binary Indexed Tree).
    This implementation uses 0-based indexing for its public methods.
    """

    def __init__(self, size):
        """
        Initializes the Fenwick Tree for an array of a given size.
        All elements are initially zero.

        Args:
            size (int): The number of elements the tree will support.
        """
        self.tree = [0] * size

    def add(self, idx, delta):
        """
        Adds a delta value to the element at a specific index.
        This operation updates all prefix sums that include this index.

        Args:
            idx (int): The 0-based index of the element to update.
            delta (int): The value to add to the element at `idx`.
        """
        while idx < len(self.tree):
            self.tree[idx] += delta
            idx |= idx + 1

    def query(self, right):
        """
        Computes the prefix sum of elements up to (but not including) `right`.
        This is the sum of the range [0, right-1].

        Args:
            right (int): The 0-based exclusive upper bound of the query range.

        Returns:
            int: The sum of elements in the prefix `[0, right-1]`.
        """
        idx = right - 1
        total_sum = 0
        while idx >= 0:
            total_sum += self.tree[idx]
            idx = (idx & (idx + 1)) - 1
        return total_sum

    def query_range(self, left, right):
        """
        Computes the sum of elements in the range [left, right-1].

        Args:
            left (int): The 0-based inclusive lower bound of the query range.
            right (int): The 0-based exclusive upper bound of the query range.

        Returns:
            int: The sum of elements in the specified range.
        """
        if left >= right:
            return 0
        return self.query(right) - self.query(left)
