"""
Implements functions to calculate the area and centroid of a simple
(non-self-intersecting) polygon. The area is calculated using the Shoelace
formula, which computes the signed area based on the cross products of adjacent
vertices. The absolute value of this result gives the geometric area. The centroid
calculation uses a related formula derived from the shoelace principle. Both
functions assume the polygon vertices are provided in a consistent order
(either clockwise or counter-clockwise).
"""

from content.geometry.point import Point


def polygon_area(vertices):
    """
    Calculates the area of a simple polygon using the Shoelace formula.

    Args:
        vertices (list[Point]): A list of Point objects representing the
                                vertices of the polygon in order.

    Returns:
        float: The area of the polygon.
    """
    n = len(vertices)
    if n < 3:
        return 0.0

    area = 0.0
    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        area += p1.cross(p2)

    return abs(area) / 2.0


def polygon_centroid(vertices):
    """
    Calculates the centroid of a simple polygon.

    Args:
        vertices (list[Point]): A list of Point objects representing the
                                vertices of the polygon in order.

    Returns:
        Point | None: A Point object representing the centroid, or None if the
                      polygon's area is zero.
    """
    n = len(vertices)
    if n < 3:
        return None

    signed_area = 0.0
    centroid_x = 0.0
    centroid_y = 0.0

    for i in range(n):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % n]
        cross_product = p1.cross(p2)

        signed_area += cross_product
        centroid_x += (p1.x + p2.x) * cross_product
        centroid_y += (p1.y + p2.y) * cross_product

    if abs(signed_area) < 1e-9:
        return None

    area = signed_area / 2.0
    centroid_x /= 6.0 * area
    centroid_y /= 6.0 * area

    return Point(centroid_x, centroid_y)
