"""
Implements a 2D Fenwick Tree (Binary Indexed Tree). This data
structure extends the 1D Fenwick Tree to support point updates and prefix
rectangle sum queries on a 2D grid.
The primary operations are:
1.  add(r, c, delta): Adds `delta` to the element at grid cell (r, c).
2.  query(r, c): Computes the sum of the rectangle from (0, 0) to (r-1, c-1).
A 2D Fenwick Tree can be conceptualized as a Fenwick Tree where each element is
itself another Fenwick Tree. The `add` and `query` operations therefore involve
traversing the tree structure in both dimensions, resulting in a time complexity
that is the product of the logarithmic complexities of each dimension.
The `query_range` method uses the principle of inclusion-exclusion on the prefix
rectangle sums to calculate the sum of any arbitrary sub-rectangle. Given a
rectangle defined by top-left (r1, c1) and bottom-right (r2-1, c2-1), the sum is:
Sum(r2, c2) - Sum(r1, c2) - Sum(r2, c1) + Sum(r1, c1),
where Sum(r, c) is the prefix sum from (0,0) to (r-1, c-1).
"""


class FenwickTree2D:
    """
    A class that implements a 2D Fenwick Tree using 0-based indexing.
    """

    def __init__(self, rows, cols):
        """
        Initializes the 2D Fenwick Tree for a grid of a given size.
        All elements are initially zero.

        Args:
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
        """
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * cols for _ in range(rows)]

    def add(self, r, c, delta):
        """
        Adds a delta value to the element at grid cell (r, c).

        Args:
            r (int): The 0-based row index of the element to update.
            c (int): The 0-based column index of the element to update.
            delta (int): The value to add.
        """
        i = r
        while i < self.rows:
            j = c
            while j < self.cols:
                self.tree[i][j] += delta
                j |= j + 1
            i |= i + 1

    def query(self, r, c):
        """
        Computes the prefix sum of the rectangle from (0, 0) to (r-1, c-1).

        Args:
            r (int): The 0-based exclusive row bound of the query rectangle.
            c (int): The 0-based exclusive column bound of the query rectangle.

        Returns:
            int: The sum of the elements in the rectangle [0..r-1, 0..c-1].
        """
        total_sum = 0
        i = r - 1
        while i >= 0:
            j = c - 1
            while j >= 0:
                total_sum += self.tree[i][j]
                j = (j & (j + 1)) - 1
            i = (i & (i + 1)) - 1
        return total_sum

    def query_range(self, r1, c1, r2, c2):
        """
        Computes the sum of the rectangle from (r1, c1) to (r2-1, c2-1).

        Args:
            r1, c1 (int): The 0-based inclusive top-left coordinates.
            r2, c2 (int): The 0-based exclusive bottom-right coordinates.

        Returns:
            int: The sum of elements in the specified rectangular range.
        """
        if r1 >= r2 or c1 >= c2:
            return 0

        total = self.query(r2, c2)
        total -= self.query(r1, c2)
        total -= self.query(r2, c1)
        total += self.query(r1, c1)
        return total
