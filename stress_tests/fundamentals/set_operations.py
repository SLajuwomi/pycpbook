import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from content.fundamentals.set_operations import (
    set_union,
    set_intersection,
    set_difference,
    set_symmetric_difference,
    is_subset,
    is_superset,
    is_disjoint,
    inplace_update_union,
    inplace_update_intersection,
    inplace_update_difference,
    inplace_update_symmetric_difference,
    freeze,
)


def run_random_tests():
    random.seed(0)
    for _ in range(3000):
        a = set(random.randint(-50, 50) for _ in range(random.randint(0, 30)))
        b = set(random.randint(-50, 50) for _ in range(random.randint(0, 30)))

        assert set_union(a, b) == (a | b)
        assert set_intersection(a, b) == (a & b)
        assert set_difference(a, b) == (a - b)
        assert set_symmetric_difference(a, b) == (a ^ b)

        assert is_subset(a, b) == (a <= b)
        assert is_superset(a, b) == (a >= b)
        assert is_disjoint(a, b) == a.isdisjoint(b)

        x = set(a)
        y = set(b)
        xid = id(x)
        inplace_update_union(x, y)
        assert id(x) == xid and x == (a | b)

        x = set(a)
        y = set(b)
        xid = id(x)
        inplace_update_intersection(x, y)
        assert id(x) == xid and x == (a & b)

        x = set(a)
        y = set(b)
        xid = id(x)
        inplace_update_difference(x, y)
        assert id(x) == xid and x == (a - b)

        x = set(a)
        y = set(b)
        xid = id(x)
        inplace_update_symmetric_difference(x, y)
        assert id(x) == xid and x == (a ^ b)

        fa = freeze(a)
        fb = freeze(b)
        assert isinstance(fa, frozenset) and isinstance(fb, frozenset)
        assert fa | fb == frozenset(a | b)
        assert fa & fb == frozenset(a & b)
        assert fa - fb == frozenset(a - b)
        assert fa ^ fb == frozenset(a ^ b)


def run_test():
    run_random_tests()
    print("Set Operations: All tests passed!")


if __name__ == "__main__":
    run_test()


