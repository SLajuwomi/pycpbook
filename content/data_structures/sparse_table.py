"""
Author: PyCPBook Community
Source: CP-Algorithms, USACO Guide
Description: Implements a Sparse Table for fast Range Minimum Queries (RMQ).
This data structure is ideal for answering range queries on a static array
for idempotent functions like min, max, or gcd.

The core idea is to precompute the answers for all ranges that have a length
that is a power of two. The table `st[k][i]` stores the minimum value in the
range `[i, i + 2^k - 1]`. This precomputation takes $O(N \\log N)$ time.

Once the table is built, a query for any arbitrary range `[l, r]` can be
answered in $O(1)$ time. This is achieved by finding the largest power of two,
`2^k`, that is less than or equal to the range length `r - l + 1`. The query
then returns the minimum of two overlapping ranges: `[l, l + 2^k - 1]` and
`[r - 2^k + 1, r]`. Because `min` is an idempotent function, the overlap
does not affect the result.

This implementation is for range minimum, but can be easily adapted for range
maximum by changing `min` to `max`.

Time: Precomputation is $O(N \\log N)$. Each query is $O(1)$.
Space: $O(N \\log N)$ to store the sparse table.
Status: Stress-tested
"""

import math


class SparseTable:
    """
    A class that implements a Sparse Table for efficient Range Minimum Queries.
    This implementation assumes 0-based indexing for the input array and queries.
    """

    def __init__(self, arr):
        """
        Initializes the Sparse Table from an input array.

        Args:
            arr (list[int]): The static list of numbers to be queried.
        """
        self.n = len(arr)
        if self.n == 0:
            return

        self.max_log = self.n.bit_length() - 1
        self.st = [[0] * self.n for _ in range(self.max_log + 1)]
        self.st[0] = list(arr)

        for k in range(1, self.max_log + 1):
            for i in range(self.n - (1 << k) + 1):
                self.st[k][i] = min(
                    self.st[k - 1][i], self.st[k - 1][i + (1 << (k - 1))]
                )

        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i >> 1] + 1

    def query(self, l, r):
        """
        Queries the minimum value in the inclusive range [l, r].

        Args:
            l (int): The 0-based inclusive starting index of the range.
            r (int): The 0-based inclusive ending index of the range.

        Returns:
            int: The minimum value in the range [l, r]. Returns infinity
                 if the table is empty or the range is invalid.
        """
        if self.n == 0 or l > r:
            return float("inf")

        length = r - l + 1
        k = self.log_table[length]
        return min(self.st[k][l], self.st[k][r - (1 << k) + 1])
