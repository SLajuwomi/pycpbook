"""
@description
This script is a correctness test for the polygon area and centroid calculation
functions. It validates the `polygon_area` and `polygon_centroid` functions
by testing them against simple geometric shapes with known, verifiable properties.

The test uses a curated set of test cases:
1.  A square: A simple case to test basic functionality.
2.  A right triangle: To test with non-axis-aligned edges.
3.  An L-shaped polygon: A non-convex shape to test the robustness of the formulas.

For each shape, the expected area and centroid coordinates are pre-calculated.
The script asserts that the output of the functions matches these expected
values within a small tolerance (epsilon) to handle floating-point arithmetic.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.geometry.point import Point
from content.geometry.polygon_area import polygon_area, polygon_centroid


def run_test():
    """
    Performs a correctness test on the polygon area and centroid functions.
    """
    EPS = 1e-9

    # --- Test Case 1: Square ---
    # Vertices: (0,0), (10,0), (10,10), (0,10)
    # Expected Area: 100
    # Expected Centroid: (5, 5)
    square_vertices = [Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)]
    area = polygon_area(square_vertices)
    centroid = polygon_centroid(square_vertices)
    assert abs(area - 100.0) < EPS, f"Square area failed. Expected 100, Got {area}"
    assert centroid is not None
    assert (
        abs(centroid.x - 5.0) < EPS and abs(centroid.y - 5.0) < EPS
    ), f"Square centroid failed. Expected (5, 5), Got {centroid}"

    # --- Test Case 2: Triangle ---
    # Vertices: (0,0), (10,0), (5,10)
    # Expected Area: 0.5 * 10 * 10 = 50
    # Expected Centroid: ((0+10+5)/3, (0+0+10)/3) = (5, 10/3)
    triangle_vertices = [Point(0, 0), Point(10, 0), Point(5, 10)]
    area = polygon_area(triangle_vertices)
    centroid = polygon_centroid(triangle_vertices)
    assert abs(area - 50.0) < EPS, f"Triangle area failed. Expected 50, Got {area}"
    assert centroid is not None
    expected_cx, expected_cy = 5.0, 10.0 / 3.0
    assert (
        abs(centroid.x - expected_cx) < EPS and abs(centroid.y - expected_cy) < EPS
    ), f"Triangle centroid failed. Expected ({expected_cx}, {expected_cy}), Got {centroid}"

    # --- Test Case 3: L-shaped Polygon (non-convex) ---
    # Vertices: (0,0), (2,0), (2,1), (1,1), (1,2), (0,2)
    # Expected Area: 3
    # Expected Centroid: (5/6, 5/6)
    l_shape_vertices = [
        Point(0, 0),
        Point(2, 0),
        Point(2, 1),
        Point(1, 1),
        Point(1, 2),
        Point(0, 2),
    ]
    area = polygon_area(l_shape_vertices)
    centroid = polygon_centroid(l_shape_vertices)
    assert abs(area - 3.0) < EPS, f"L-shape area failed. Expected 3, Got {area}"
    assert centroid is not None
    expected_cxy = 5.0 / 6.0
    assert (
        abs(centroid.x - expected_cxy) < EPS and abs(centroid.y - expected_cxy) < EPS
    ), f"L-shape centroid failed. Expected ({expected_cxy}, {expected_cxy}), Got {centroid}"

    # --- Test Case 4: Clockwise order ---
    # Same square as before, but in clockwise order. Area should be the same.
    square_vertices_cw = [Point(0, 0), Point(0, 10), Point(10, 10), Point(10, 0)]
    area = polygon_area(square_vertices_cw)
    centroid = polygon_centroid(square_vertices_cw)
    assert (
        abs(area - 100.0) < EPS
    ), f"Clockwise square area failed. Expected 100, Got {area}"
    assert centroid is not None
    assert (
        abs(centroid.x - 5.0) < EPS and abs(centroid.y - 5.0) < EPS
    ), f"Clockwise square centroid failed. Expected (5, 5), Got {centroid}"

    print("Polygon Area and Centroid: All tests passed!")


if __name__ == "__main__":
    run_test()
