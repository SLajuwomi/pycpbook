"""
@description
This script is a unit-style stress test for the foundational Point class and
its associated geometric primitives. It validates the correctness of each
operation by asserting its output against known, pre-calculated results for
a variety of test cases.

The test covers:
- Vector arithmetic (addition, subtraction, scalar multiplication/division).
- Dot product and cross product.
- Squared distance calculation.
- Comparison operators (equality and less-than for sorting).
- The `orientation` function for collinear, clockwise, and counter-clockwise cases.

This ensures the fundamental building blocks for all other geometry algorithms
are reliable and correct.
"""

import sys
import os
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.geometry.point import Point, orientation


def run_test():
    p1 = Point(1, 2)
    p2 = Point(4, 6)

    # Test arithmetic
    assert p1 + p2 == Point(5, 8)
    assert p2 - p1 == Point(3, 4)
    assert p1 * 3 == Point(3, 6)
    assert p2 / 2 == Point(2, 3)

    # Test products
    assert p1.dot(p2) == 1 * 4 + 2 * 6 == 16
    assert p1.cross(p2) == 1 * 6 - 2 * 4 == -2

    # Test distance
    assert (p2 - p1).dot(p2 - p1) == p1.dist_sq(p2)
    assert p1.dist_sq(p2) == 3 * 3 + 4 * 4 == 25

    # Test comparison
    assert p1 == Point(1, 2)
    assert not (p1 == p2)
    assert p1 < p2
    assert Point(1, 5) < Point(2, 3)
    assert not (Point(2, 3) < Point(1, 5))
    assert Point(1, 3) < Point(1, 5)

    # Test orientation
    o = Point(0, 0)
    p_x_axis = Point(5, 0)
    p_y_axis = Point(0, 5)
    p_collinear = Point(10, 0)
    p_ccw = Point(5, 5)
    p_cw = Point(5, -5)

    # Collinear
    assert orientation(o, p_x_axis, p_collinear) == 0
    # Counter-clockwise
    assert orientation(o, p_x_axis, p_ccw) == 1
    # Clockwise
    assert orientation(o, p_x_axis, p_cw) == -1

    print("Geometry Point Class and Primitives: All tests passed!")


if __name__ == "__main__":
    run_test()
