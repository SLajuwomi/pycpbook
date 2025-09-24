"""
@description
This module provides utility functions for generating random geometric shapes,
specifically polygons, for use in stress tests of geometry algorithms.

Key functions:
- generate_simple_polygon: Creates a random simple (non-self-intersecting)
                           polygon with a given number of vertices.
"""

import random
import math


def generate_simple_polygon(n, max_coord_val=1000):
    """
    Generates a random simple (non-self-intersecting) polygon with n vertices.

    The method works by generating points in polar coordinates from a central
    origin and then converting them to Cartesian coordinates. By generating points
    with random angles and radii and then sorting by angle, we ensure that
    connecting the vertices in order will not create any self-intersections.

    Args:
        n (int): The number of vertices in the polygon. Must be >= 3.
        max_coord_val (int): The approximate maximum absolute value for the
                             x and y coordinates of the vertices.

    Returns:
        list[tuple[int, int]]: A list of (x, y) tuples representing the vertices
                               of the polygon in order.
    """
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    center_x = random.uniform(-max_coord_val / 4, max_coord_val / 4)
    center_y = random.uniform(-max_coord_val / 4, max_coord_val / 4)

    points = []

    # Generate random angles and radii
    angles = sorted([random.uniform(0, 2 * math.pi) for _ in range(n)])
    min_radius = max_coord_val / 5
    max_radius = max_coord_val / 2

    for angle in angles:
        radius = random.uniform(min_radius, max_radius)

        # Add some jitter to the radius to make shapes less star-like
        radius *= 1 + random.uniform(-0.2, 0.2)

        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        points.append((x, y))

    return points
