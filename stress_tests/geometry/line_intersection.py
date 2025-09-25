"""
@description
This script serves as a correctness test for the line and segment intersection
functions. Unlike typical stress tests that use randomized data against a naive
solution, this script uses a curated set of specific, known test cases to
validate the geometric primitives across a wide range of scenarios and edge cases.

The test validates both `segments_intersect` and `line_line_intersection` functions.

For `segments_intersect`, it checks:
- General crossing intersections.
- T-junctions, where one segment's endpoint lies on another.
- Collinear cases: overlapping, disjoint, and touching.
- Non-intersecting cases: parallel, and cases where the infinite lines
  intersect but the segments themselves do not.

For `line_line_intersection`, it checks:
- A standard intersection case with a known result.
- Parallel and collinear lines, which should not have a unique intersection.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.geometry.point import Point
from content.geometry.line_intersection import (
    segments_intersect,
    line_line_intersection,
)


def run_test():
    """
    Performs a correctness test on the intersection functions.
    """
    # --- Test segments_intersect ---
    # Case 1: General intersection
    p1, q1 = Point(0, 0), Point(10, 10)
    p2, q2 = Point(0, 10), Point(10, 0)
    assert segments_intersect(p1, q1, p2, q2)

    # Case 2: No intersection (lines intersect but segments do not)
    p1, q1 = Point(10, 10), Point(20, 20)
    p2, q2 = Point(0, 10), Point(10, 0)
    assert not segments_intersect(p1, q1, p2, q2)

    # Case 3: T-junction
    p1, q1 = Point(0, 0), Point(10, 0)
    p2, q2 = Point(5, 5), Point(5, -5)
    assert segments_intersect(p1, q1, p2, q2)

    # Case 4: Parallel lines, no intersection
    p1, q1 = Point(0, 0), Point(10, 0)
    p2, q2 = Point(0, 5), Point(10, 5)
    assert not segments_intersect(p1, q1, p2, q2)

    # Case 5: Collinear and overlapping
    p1, q1 = Point(0, 0), Point(10, 0)
    p2, q2 = Point(5, 0), Point(15, 0)
    assert segments_intersect(p1, q1, p2, q2)

    # Case 6: Collinear and disjoint
    p1, q1 = Point(0, 0), Point(10, 0)
    p2, q2 = Point(11, 0), Point(20, 0)
    assert not segments_intersect(p1, q1, p2, q2)

    # Case 7: Collinear and touching at an endpoint
    p1, q1 = Point(0, 0), Point(10, 0)
    p2, q2 = Point(10, 0), Point(20, 0)
    assert segments_intersect(p1, q1, p2, q2)

    # Case 8: One segment is a point on the other segment
    p1, q1 = Point(0, 0), Point(10, 0)
    p2, q2 = Point(5, 0), Point(5, 0)
    assert segments_intersect(p1, q1, p2, q2)

    # --- Test line_line_intersection ---
    EPS = 1e-9
    # Case 1: General intersection
    p1, p2 = Point(0, 0), Point(2, 2)
    p3, p4 = Point(0, 2), Point(2, 0)
    intersection = line_line_intersection(p1, p2, p3, p4)
    assert intersection is not None
    assert abs(intersection.x - 1.0) < EPS
    assert abs(intersection.y - 1.0) < EPS

    # Case 2: Parallel lines
    p1, p2 = Point(0, 0), Point(1, 1)
    p3, p4 = Point(0, 1), Point(1, 2)
    assert line_line_intersection(p1, p2, p3, p4) is None

    # Case 3: Collinear lines
    p1, p2 = Point(0, 0), Point(1, 1)
    p3, p4 = Point(2, 2), Point(3, 3)
    assert line_line_intersection(p1, p2, p3, p4) is None

    print("Line/Segment Intersection: All tests passed!")


if __name__ == "__main__":
    run_test()
