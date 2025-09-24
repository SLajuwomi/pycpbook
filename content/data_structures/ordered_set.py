"""
Author: PyCPBook Community
Source: KACTL, CP-Algorithms (adapted from Treap)
Description: Implements an Ordered Set data structure using a randomized
balanced binary search tree (Treap). An Ordered Set supports all the standard
operations of a balanced BST (insert, delete, search) and two additional
powerful operations:
1. `find_by_order(k)`: Finds the k-th smallest element in the set (0-indexed).
2. `order_of_key(key)`: Finds the number of elements in the set that are
   strictly smaller than the given key (i.e., its rank).

To achieve this, each node in the underlying Treap is augmented to store the
size of the subtree rooted at that node. This `size` information is updated
during insertions and deletions. The ordered set operations then use these
sizes to navigate the tree efficiently. For example, to find the k-th element,
we can compare `k` with the size of the left subtree to decide whether to go
left, right, or stop at the current node.

The implementation is based on the elegant `split` and `merge` operations,
which are modified to maintain the subtree size property.

Time: $O(\\log N)$ on average for `insert`, `delete`, `search`,
`find_by_order`, and `order_of_key` operations, where $N$ is the number of
elements in the set.
Space: $O(N)$ to store the nodes of the set.
Status: Stress-tested
"""

import random


class Node:
    """Represents a single node in the Ordered Set's underlying Treap."""

    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.size = 1
        self.left = None
        self.right = None


def _get_size(t):
    return t.size if t else 0


def _update_size(t):
    if t:
        t.size = 1 + _get_size(t.left) + _get_size(t.right)


def _split(t, key):
    """
    Splits the tree `t` into two trees: one with keys < `key` (l)
    and one with keys >= `key` (r).
    """
    if not t:
        return None, None
    if t.key < key:
        l, r = _split(t.right, key)
        t.right = l
        _update_size(t)
        return t, r
    else:
        l, r = _split(t.left, key)
        t.left = r
        _update_size(t)
        return l, t


def _merge(t1, t2):
    """Merges two trees `t1` and `t2`, assuming keys in `t1` < keys in `t2`."""
    if not t1:
        return t2
    if not t2:
        return t1
    if t1.priority > t2.priority:
        t1.right = _merge(t1.right, t2)
        _update_size(t1)
        return t1
    else:
        t2.left = _merge(t1, t2.left)
        _update_size(t2)
        return t2


class OrderedSet:
    """
    An Ordered Set implementation using a Treap.
    Supports finding the k-th element and the rank of an element.
    """

    def __init__(self):
        self.root = None

    def search(self, key):
        node = self.root
        while node:
            if node.key == key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def insert(self, key):
        if self.search(key):
            return
        new_node = Node(key)
        l, r = _split(self.root, key)
        self.root = _merge(_merge(l, new_node), r)

    def delete(self, key):
        if not self.search(key):
            return
        l, r = _split(self.root, key)
        _, r_prime = _split(r, key + 1)
        self.root = _merge(l, r_prime)

    def find_by_order(self, k):
        """Finds the k-th smallest element (0-indexed)."""
        node = self.root
        while node:
            left_size = _get_size(node.left)
            if left_size == k:
                return node.key
            elif k < left_size:
                node = node.left
            else:
                k -= left_size + 1
                node = node.right
        return None

    def order_of_key(self, key):
        """Finds the number of elements strictly smaller than key."""
        count = 0
        node = self.root
        while node:
            if key == node.key:
                count += _get_size(node.left)
                break
            elif key < node.key:
                node = node.left
            else:
                count += _get_size(node.left) + 1
                node = node.right
        return count

    def __len__(self):
        return _get_size(self.root)
