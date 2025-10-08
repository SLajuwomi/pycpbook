"""
Implements a Line Container for the Convex Hull Trick. This data
structure maintains a set of lines of the form `y = mx + c` and allows for
efficiently querying the minimum `y` value for a given `x`. This is a key
component in optimizing certain dynamic programming problems.
This implementation is specialized for the following common case:
- Queries ask for the minimum value.
- The slopes `m` of the lines added are monotonically decreasing.
The lines are stored in a deque, which acts as the lower convex hull. When a
new line is added, we maintain the convexity of the hull by removing any lines
from the back that become redundant. A line becomes redundant if the intersection
point of its neighbors moves left, violating the convexity property. This check
is done using cross-products to avoid floating-point arithmetic.
Queries are performed using a binary search on the hull to find the optimal
line for the given `x`. If the `x` values for queries are also monotonic, the
query time can be improved to amortized $O(1)$ by using a pointer instead of
a binary search.
To adapt for maximum value queries, change the inequalities in `add` and `query`.
To handle monotonically increasing slopes, add lines to the front of the deque
and adjust the `add` method's popping logic accordingly.
because each line is added and removed at most once.
"""


class LineContainer:
    """
    A data structure for the Convex Hull Trick, optimized for minimum queries
    and monotonically decreasing slopes.
    """

    def __init__(self):
        # Each line is stored as a tuple (m, c) representing y = mx + c.
        self.hull = []

    def _is_redundant(self, l1, l2, l3):
        """
        Checks if line l2 is redundant given its neighbors l1 and l3.
        l2 is redundant if the intersection of l1 and l3 is to the left of
        the intersection of l1 and l2.
        Intersection of (m1, c1) and (m2, c2) is x = (c2 - c1) / (m1 - m2).
        We check if (c3-c1)/(m1-m3) <= (c2-c1)/(m1-m2).
        To avoid floating point, we use cross-multiplication.
        Since slopes are decreasing, m1 > m2 > m3, so (m1-m3) and (m1-m2) are positive.
        The inequality becomes (c3-c1)*(m1-m2) <= (c2-c1)*(m1-m3).
        """
        m1, c1 = l1
        m2, c2 = l2
        m3, c3 = l3
        # Note the direction of inequality might change based on max/min query
        # and increasing/decreasing slopes. This is for min query, decr. slopes.
        return (c3 - c1) * (m1 - m2) <= (c2 - c1) * (m1 - m3)

    def add(self, m, c):
        """
        Adds a new line y = mx + c to the container.
        Assumes that m is less than the slope of any previously added line.
        """
        new_line = (m, c)
        while len(self.hull) >= 2 and self._is_redundant(
            self.hull[-2], self.hull[-1], new_line
        ):
            self.hull.pop()
        self.hull.append(new_line)

    def query(self, x):
        """
        Finds the minimum value of y = mx + c for a given x among all lines.
        """
        if not self.hull:
            return float("inf")

        # Binary search for the optimal line.
        # The function `f(i) = m_i * x + c_i` is not monotonic, but the
        # optimal line index is. Specifically, the function `f(i+1) - f(i)`
        # is monotonic. We are looking for the point where the function
        # transitions from decreasing to increasing.
        low, high = 0, len(self.hull) - 1
        res_idx = 0

        while low <= high:
            mid = (low + high) // 2
            # Check if mid is better than mid+1
            if mid + 1 < len(self.hull):
                val_mid = self.hull[mid][0] * x + self.hull[mid][1]
                val_next = self.hull[mid + 1][0] * x + self.hull[mid + 1][1]
                if val_mid > val_next:
                    low = mid + 1
                else:
                    res_idx = mid
                    high = mid - 1
            else:
                res_idx = mid
                high = mid - 1

        m, c = self.hull[res_idx]
        return m * x + c
