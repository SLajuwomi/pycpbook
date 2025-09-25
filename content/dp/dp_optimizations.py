"""
Author: PyCPBook Community
Source: CP-Algorithms, USACO Guide
Description: This file explains and demonstrates several advanced dynamic programming
optimizations. The primary focus is the Convex Hull Trick, with conceptual
explanations for Knuth-Yao Speedup and Divide and Conquer Optimization.

Convex Hull Trick (CHT):
This optimization applies to DP recurrences of the form:
`dp[i] = min_{j<i} (dp[j] + b[j] * a[i])` (or similar).
For a fixed `i`, each `j` defines a line `y = m*x + c`, where `m = b[j]`, `x = a[i]`,
and `c = dp[j]`. The problem then becomes finding the minimum value among a set of
lines for a given x-coordinate `a[i]`. A `LineContainer` data structure is used to
maintain the lower envelope (convex hull) of these lines, allowing for efficient
queries. The example below solves a problem with the recurrence
`dp[i] = C + min_{j<i} (dp[j] + (p[i] - p[j])^2)`, which can be rearranged into
the required line form. This works efficiently if the slopes of the lines being
added are monotonic.

Knuth-Yao Speedup:
This optimization applies to recurrences of the form
`dp[i][j] = C[i][j] + min_{i<=k<j} (dp[i][k] + dp[k+1][j])`, such as in the
optimal binary search tree problem. It can be used if the cost function `C`
satisfies the quadrangle inequality (`C[a][c] + C[b][d] <= C[a][d] + C[b][c]`
for `a <= b <= c <= d`). The key insight is that the optimal splitting point `k`
for `dp[i][j]`, denoted `opt[i][j]`, is monotonic: `opt[i][j-1] <= opt[i][j] <= opt[i+1][j]`.
This property allows us to reduce the search space for `k` from `O(j-i)` to
`opt[i+1][j] - opt[i][j-1]`, improving the total time complexity from $O(N^3)$ to $O(N^2)$.

Divide and Conquer Optimization:
This technique applies to recurrences of the form `dp[i][j] = min_{0<=k<j} (dp[i-1][k] + C[k][j])`.
A naive computation would take $O(N^2)$ for each `i`, leading to $O(K*N^2)$ total
time for `K` states. The optimization is based on the observation that if the
cost function `C` has certain properties (often related to the quadrangle inequality),
the optimal choice of `k` for `dp[i][j]` is monotonic with `j`. We can compute all
`dp[i][j]` values for a fixed `i` and `j` in a range `[l, r]` by first finding the
optimal `k` for the midpoint `mid = (l+r)/2`. Then, recursively, the optimal `k` for
the left half `[l, mid-1]` must be in a smaller range, and similarly for the
right half. This divide and conquer approach computes all `dp[i][j]` for a fixed `i`
in $O(N \\log N)$ time.

Time: Varies by optimization. CHT: $O(N \\log N)$ or $O(N)$ amortized.
Space: Varies.
Status: Conceptual (Knuth-Yao, D&C), Stress-tested (CHT example).
"""

import sys
import os

# The stress test runner adds the project root to the path.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from content.data_structures.line_container import LineContainer


def convex_hull_trick_example(p, C):
    """
    Solves an example problem using the Convex Hull Trick.
    Problem: Given n points on a line with increasing coordinates p[0]...p[n-1],
    find the minimum cost to travel from point 0 to point n-1. The cost of
    jumping from point i to point j is (p[j] - p[i])^2 + C.

    DP recurrence: dp[i] = min_{j<i} (dp[j] + (p[i] - p[j])^2 + C)
    This can be rewritten as:
    dp[i] = p[i]^2 + C + min_{j<i} (-2*p[j]*p[i] + dp[j] + p[j]^2)
    This fits the form y = mx + c, where:
    - x = p[i]
    - m_j = -2 * p[j]
    - c_j = dp[j] + p[j]^2
    Since p is increasing, the slopes m_j are decreasing, matching the
    `LineContainer`'s requirement.

    Args:
        p (list[int]): A list of increasing integer coordinates.
        C (int): A constant cost for each jump.

    Returns:
        int: The minimum cost to reach the last point.
    """
    n = len(p)
    if n <= 1:
        return 0

    dp = [0] * n
    lc = LineContainer()

    # Base case: dp[0] = 0. Add the first line to the container.
    # m_0 = -2*p[0], c_0 = dp[0] + p[0]^2 = p[0]^2
    lc.add(-2 * p[0], p[0] ** 2)

    for i in range(1, n):
        # Query for the minimum value at x = p[i]
        min_val = lc.query(p[i])
        dp[i] = p[i] ** 2 + C + min_val

        # Add the new line corresponding to state i to the container
        # m_i = -2*p[i], c_i = dp[i] + p[i]^2
        lc.add(-2 * p[i], dp[i] + p[i] ** 2)

    return dp[n - 1]
