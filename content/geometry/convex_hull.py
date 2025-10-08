"""
Implements the Monotone Chain algorithm (also known as Andrew's
algorithm) to find the convex hull of a set of 2D points. The convex hull is
the smallest convex polygon that contains all the given points.
The algorithm works as follows:
1.  Sort all points lexicographically (first by x-coordinate, then by y-coordinate).
    This step takes $O(N \\log N)$ time.
2.  Build the lower hull of the polygon. Iterate through the sorted points and
    maintain a list representing the lower hull. For each point, check if adding it
    to the hull would create a non-left (i.e., clockwise or collinear) turn with
    the previous two points on the hull. If it does, pop the last point from the
    hull until the turn becomes counter-clockwise. This ensures the convexity of
    the lower hull.
3.  Build the upper hull in a similar manner, but by iterating through the sorted
    points in reverse order.
4.  Combine the lower and upper hulls to form the complete convex hull. The
    endpoints (the lexicographically smallest and largest points) will be
    included in both hulls, so they must be removed from one to avoid duplication.
This implementation relies on the `Point` class and `orientation` primitive from
the `content.geometry.point` module.
"""

from content.geometry.point import Point, orientation


def convex_hull(points):
    """
    Computes the convex hull of a set of points using the Monotone Chain algorithm.

    Args:
        points (list[Point]): A list of Point objects.

    Returns:
        list[Point]: A list of Point objects representing the vertices of the
                     convex hull in counter-clockwise order. Returns an empty
                     list if fewer than 3 points are provided.
    """
    n = len(points)
    if n <= 2:
        return points

    # Sort points lexicographically
    points.sort()

    # Build lower hull
    lower_hull = []
    for p in points:
        while (
            len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], p) <= 0
        ):
            lower_hull.pop()
        lower_hull.append(p)

    # Build upper hull
    upper_hull = []
    for p in reversed(points):
        while (
            len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) <= 0
        ):
            upper_hull.pop()
        upper_hull.append(p)

    # Combine the hulls, removing duplicate start/end points
    return lower_hull[:-1] + upper_hull[:-1]
