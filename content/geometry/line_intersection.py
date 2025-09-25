"""
Author: PyCPBook Community
Source: Introduction to Algorithms (CLRS), CP-Algorithms
Description: Provides functions for detecting and calculating intersections
between lines and line segments in 2D space. This is a fundamental component
for many geometric algorithms.

The module includes:
- `segments_intersect(p1, q1, p2, q2)`: Determines if two line segments intersect.
  It uses orientation tests to handle the general case where segments cross each
  other. If the orientations of the endpoints of one segment with respect to the
  other segment are different, they intersect. Special handling is required for
  collinear cases, where we check if the segments overlap.
- `line_line_intersection(p1, p2, p3, p4)`: Finds the intersection point of two
  infinite lines defined by pairs of points `(p1, p2)` and `(p3, p4)`. It uses a
  formula based on cross products to solve the system of linear equations
  representing the lines. This method returns `None` if the lines are parallel or
  collinear, as there is no unique intersection point.

All functions rely on the `Point` class and `orientation` primitive from
`content.geometry.point`.
Time: All functions are $O(1)$.
Space: All functions are $O(1)$.
Status: Stress-tested
"""

from content.geometry.point import Point, orientation


def on_segment(p, q, r):
    """
    Given three collinear points p, q, r, the function checks if point q
    lies on line segment 'pr'.
    """
    return (
        q.x <= max(p.x, r.x)
        and q.x >= min(p.x, r.x)
        and q.y <= max(p.y, r.y)
        and q.y >= min(p.y, r.y)
    )


def segments_intersect(p1, q1, p2, q2):
    """
    Checks if line segment 'p1q1' and 'p2q2' intersect.
    """
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != 0 and o2 != 0 and o3 != 0 and o4 != 0:
        if o1 != o2 and o3 != o4:
            return True
        return False

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def line_line_intersection(p1, p2, p3, p4):
    """
    Finds the intersection point of two infinite lines defined by (p1, p2) and (p3, p4).
    Returns the intersection point as a Point object with float coordinates,
    or None if the lines are parallel or collinear.
    """
    v1 = p2 - p1
    v2 = p4 - p3
    denominator = v1.cross(v2)

    if abs(denominator) < 1e-9:
        return None

    t = (p3 - p1).cross(v2) / denominator
    return p1 + v1 * t
