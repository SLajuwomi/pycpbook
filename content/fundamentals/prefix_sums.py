"""
Author: PyCPBook Community
Source: CP-Algorithms, TopCoder tutorials
Description: Implements 1D and 2D prefix sum arrays for fast range sum queries.
Prefix sums (also known as summed-area tables in 2D) allow for the sum of any
contiguous sub-array or sub-rectangle to be calculated in constant time after an
initial linear-time precomputation.

1D Prefix Sums:
Given an array `A`, its prefix sum array `P` is defined such that `P[i]` is the
sum of all elements from `A[0]` to `A[i-1]`. The sum of a range `[l, r-1]` can
then be calculated in $O(1)$ as `P[r] - P[l]`.

2D Prefix Sums:
This extends the concept to a 2D grid. The prefix sum `P[i][j]` stores the sum
of the rectangle from `(0, 0)` to `(i-1, j-1)`. The sum of an arbitrary
rectangle defined by its top-left corner `(r1, c1)` and bottom-right corner
`(r2-1, c2-1)` is calculated using the principle of inclusion-exclusion:
`sum = P[r2][c2] - P[r1][c2] - P[r2][c1] + P[r1][c1]`.

Time:
- 1D: $O(N)$ for precomputation, $O(1)$ for each range query.
- 2D: $O(R \\cdot C)$ for precomputation, $O(1)$ for each range query.
Space:
- 1D: $O(N)$ to store the prefix sum array.
- 2D: $O(R \\cdot C)$ to store the prefix sum grid.
Status: To be stress-tested
"""


def build_prefix_sum_1d(arr):
    """
    Builds a 1D prefix sum array and returns a query function.

    Args:
        arr (list[int]): The input 1D array.

    Returns:
        function: A function `query(left, right)` that returns the sum of
                  the elements in the range [left, right-1] in O(1).
    """
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    def query(left, right):
        """
        Queries the sum of the range [left, right-1].
        `left` is inclusive, `right` is exclusive.
        """
        if not (0 <= left <= right <= n):
            return 0
        return prefix_sum[right] - prefix_sum[left]

    return query


def build_prefix_sum_2d(grid):
    """
    Builds a 2D prefix sum array and returns a query function.

    Args:
        grid (list[list[int]]): The input 2D grid.

    Returns:
        function: A function `query(r1, c1, r2, c2)` that returns the sum of
                  the elements in the rectangle from (r1, c1) to (r2-1, c2-1) in O(1).
    """
    if not grid or not grid[0]:
        return lambda r1, c1, r2, c2: 0

    rows, cols = len(grid), len(grid[0])
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

    for r in range(rows):
        for c in range(cols):
            prefix_sum[r + 1][c + 1] = (
                grid[r][c]
                + prefix_sum[r][c + 1]
                + prefix_sum[r + 1][c]
                - prefix_sum[r][c]
            )

    def query(r1, c1, r2, c2):
        """
        Queries the sum of the rectangle from (r1, c1) to (r2-1, c2-1).
        `r1, c1` are inclusive top-left coordinates.
        `r2, c2` are exclusive bottom-right coordinates.
        """
        if not (0 <= r1 <= r2 <= rows and 0 <= c1 <= c2 <= cols):
            return 0
        return (
            prefix_sum[r2][c2]
            - prefix_sum[r1][c2]
            - prefix_sum[r2][c1]
            + prefix_sum[r1][c1]
        )

    return query
