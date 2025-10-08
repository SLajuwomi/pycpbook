"""
Sets in Python provide $O(1)$ average-time membership and support expressive
algebra via operators. This section covers the core operations used most often
in problem solving: union, intersection, difference, and symmetric difference,
along with subset/superset/disjointness relations, in-place updates, basic
construction patterns, and a note on `frozenset`.

Key operations (A and B are sets):
- Union: `A | B` combines elements from both
- Intersection: `A & B` keeps common elements
- Difference: `A - B` removes elements of B from A
- Symmetric difference: `A ^ B` keeps elements in exactly one of A, B

Relations:
- Subset: `A <= B` ($A$ is subset of $B$)
- Superset: `A >= B` ($A$ is superset of $B$)
- Disjointness: `A.isdisjoint(B)`

In-place updates (mutate the left operand):
- `A |= B`, `A &= B`, `A -= B`, `A ^= B`
  Method forms: `update`, `intersection_update`, `difference_update`, `symmetric_difference_update`.

Construction patterns:
- Literal: `{1, 2, 3}`
- From iterable: `set(iterable)`
- Comprehension: `{f(x) for x in xs if cond(x)}`

`frozenset` is an immutable set, hashable and usable as dict/set keys. It
supports the same non in-place operations as `set`.

Complexity notes:
- Membership and add/remove are average $O(1)$ with good hashing
- Set operations scale with operand sizes; e.g., union is roughly linear in total elements
- Elements must be hashable; unhashable types (like lists) cannot be members
"""


def set_union(a, b):
    return a | b


def set_intersection(a, b):
    return a & b


def set_difference(a, b):
    return a - b


def set_symmetric_difference(a, b):
    return a ^ b


def is_subset(a, b):
    return a <= b


def is_superset(a, b):
    return a >= b


def is_disjoint(a, b):
    return a.isdisjoint(b)


def inplace_update_union(a, b):
    a |= b
    return a


def inplace_update_intersection(a, b):
    a &= b
    return a


def inplace_update_difference(a, b):
    a -= b
    return a


def inplace_update_symmetric_difference(a, b):
    a ^= b
    return a


def freeze(iterable):
    return frozenset(iterable)


