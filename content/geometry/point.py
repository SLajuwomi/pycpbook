"""
Author: PyCPBook Community
Source: KACTL, CP-Algorithms, standard geometry texts
Description: Implements a foundational Point class for 2D geometry problems.
The class supports standard vector operations through overloaded operators,
making geometric calculations intuitive and clean. It can handle both integer
and floating-point coordinates.

Operations supported:
- Addition/Subtraction: `p1 + p2`, `p1 - p2`
- Scalar Multiplication/Division: `p * scalar`, `p / scalar`
- Dot Product: `p1.dot(p2)`
- Cross Product: `p1.cross(p2)` (returns the 2D magnitude)
- Squared Euclidean Distance: `p1.dist_sq(p2)`
- Comparison: `p1 == p2`, `p1 < p2` (lexicographical)

A standalone `orientation` function is also provided to determine the
orientation of three ordered points (collinear, clockwise, or counter-clockwise),
which is a fundamental primitive for many geometric algorithms.
Time: All Point methods and the `orientation` function are $O(1)$.
Space: $O(1)$ per Point object.
Status: Stress-tested
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def dist_sq(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return dx * dx + dy * dy


def orientation(p, q, r):
    """
    Determines the orientation of the ordered triplet (p, q, r).

    Returns:
        int: > 0 for counter-clockwise, < 0 for clockwise, 0 for collinear.
    """
    val = (q.x - p.x) * (r.y - q.y) - (q.y - p.y) * (r.x - q.x)
    if val == 0:
        return 0
    return 1 if val > 0 else -1
