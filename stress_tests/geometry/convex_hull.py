"""
@description
This script is a stress test for the Convex Hull algorithm. It validates the
correctness of the `convex_hull` function (which uses the Monotone Chain
algorithm) by comparing its results against a naive, but correct, implementation
of the Gift Wrapping (Jarvis March) algorithm.

The test operates as follows:
1.  A `naive_convex_hull` function is implemented using the Gift Wrapping
    algorithm, which finds hull points one by one by selecting the point with
    the smallest polar angle relative to the current point. This is slow
    (O(NH), where H is the number of points on the hull) but easy to verify.
2.  For a large number of iterations, a set of random 2D points is generated.
3.  The convex hull is computed using both the optimized `convex_hull` function
    and the `naive_convex_hull` function.
4.  Since the order of vertices in the resulting hulls might differ (e.g.,
    different starting points), the lists of points are sorted lexicographically
    to create a canonical representation for comparison.
5.  The script asserts that the two sorted lists of hull vertices are identical.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.geometry.point import Point, orientation
from content.geometry.convex_hull import convex_hull


def naive_convex_hull(points):
    """
    A naive O(NH) implementation of Convex Hull using Jarvis March (Gift Wrapping).
    """
    n = len(points)
    if n <= 2:
        return sorted(points)

    # Find the leftmost point
    start_idx = 0
    for i in range(1, n):
        if points[i].x < points[start_idx].x:
            start_idx = i
        elif points[i].x == points[start_idx].x and points[i].y < points[start_idx].y:
            start_idx = i

    hull = []
    p_idx = start_idx
    while True:
        hull.append(points[p_idx])
        q_idx = (p_idx + 1) % n
        for i in range(n):
            orient = orientation(points[p_idx], points[i], points[q_idx])
            if orient == -1:
                q_idx = i
            elif orient == 0:
                dx_i = points[i].x - points[p_idx].x
                dy_i = points[i].y - points[p_idx].y
                dx_q = points[q_idx].x - points[p_idx].x
                dy_q = points[q_idx].y - points[p_idx].y
                if dx_i * dx_i + dy_i * dy_i > dx_q * dx_q + dy_q * dy_q:
                    q_idx = i
        p_idx = q_idx
        if p_idx == start_idx:
            break
    return sorted(hull)


def run_test():
    """
    Performs a stress test on the convex_hull implementation.
    """
    ITERATIONS = 200
    MAX_N = 100
    MAX_COORD = 1000

    for i in range(ITERATIONS):
        n = random.randint(3, MAX_N)
        points = []
        for _ in range(n):
            x = random.randint(-MAX_COORD, MAX_COORD)
            y = random.randint(-MAX_COORD, MAX_COORD)
            points.append(Point(x, y))

        # Remove duplicate points to simplify comparison
        points = list(set((p.x, p.y) for p in points))
        points = [Point(x, y) for x, y in points]
        if len(points) < 3:
            continue

        res_optimized = convex_hull(points)
        res_naive = naive_convex_hull(points)

        # Sort both results for canonical comparison
        sorted_optimized = sorted(res_optimized)
        sorted_naive = sorted(res_naive)

        assert len(sorted_optimized) == len(sorted_naive), (
            f"Convex hull failed on iteration {i}: Mismatch in hull size.\n"
            f"Expected size: {len(sorted_naive)}, Got size: {len(sorted_optimized)}"
        )

        assert all(
            p_opt == p_naive for p_opt, p_naive in zip(sorted_optimized, sorted_naive)
        ), (
            f"Convex hull failed on iteration {i}: Mismatch in hull points.\n"
            f"Input points: {[(p.x, p.y) for p in points]}\n"
            f"Expected (Naive): {[(p.x, p.y) for p in sorted_naive]}\n"
            f"Got (Optimized): {[(p.x, p.y) for p in sorted_optimized]}"
        )

    print("Convex Hull: All tests passed!")


if __name__ == "__main__":
    run_test()
