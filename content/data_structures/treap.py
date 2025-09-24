"""
Author: PyCPBook Community
Source: KACTL, CP-Algorithms
Description: Implements a Treap, a randomized balanced binary search tree.
A Treap is a data structure that combines the properties of a binary search tree
and a heap. Each node in the Treap has both a key and a randomly assigned priority.
The keys follow the binary search tree property (left child's key < parent's key < right child's key),
while the priorities follow the max-heap property (parent's priority > children's priorities).

The random assignment of priorities ensures that, with high probability, the tree
remains balanced, leading to logarithmic time complexity for standard operations.
This implementation uses `split` and `merge` operations, which are a clean and
powerful way to handle insertions and deletions.

- `split(key)`: Splits the tree into two separate trees: one containing all keys
  less than `key`, and another containing all keys greater than or equal to `key`.
- `merge(left, right)`: Merges two trees, `left` and `right`, under the assumption
  that all keys in `left` are smaller than all keys in `right`.

Using these, `insert` and `delete` can be implemented elegantly.

Time: $O(\\log N)$ on average for `insert`, `delete`, and `search` operations,
where $N$ is the number of nodes in the Treap. The performance depends on the
randomness of the priorities.
Space: $O(N)$ to store the nodes of the Treap.
Status: Stress-tested
"""

import random


class Node:
    """
    Represents a single node in the Treap.
    Each node contains a key, a randomly generated priority, and left/right children.
    """

    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None


def _split(t, key):
    """
    Splits the tree rooted at `t` into two trees based on `key`.
    Returns a tuple (left_tree, right_tree), where left_tree contains all keys
    from `t` that are less than `key`, and right_tree contains all keys that are
    greater than or equal to `key`.
    """
    if not t:
        return None, None
    if t.key < key:
        l, r = _split(t.right, key)
        t.right = l
        return t, r
    else:
        l, r = _split(t.left, key)
        t.left = r
        return l, t


def _merge(t1, t2):
    """
    Merges two trees `t1` and `t2`.
    Assumes all keys in `t1` are less than all keys in `t2`.
    The merge is performed based on node priorities to maintain the heap property.
    """
    if not t1:
        return t2
    if not t2:
        return t1
    if t1.priority > t2.priority:
        t1.right = _merge(t1.right, t2)
        return t1
    else:
        t2.left = _merge(t1, t2.left)
        return t2


class Treap:
    """
    The Treap class providing a public API for balanced BST operations.
    """

    def __init__(self):
        """Initializes an empty Treap."""
        self.root = None

    def search(self, key):
        """
        Searches for a key in the Treap.
        Returns True if the key is found, otherwise False.
        """
        node = self.root
        while node:
            if node.key == key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, key):
        """
        Inserts a key into the Treap. If the key already exists, the tree is unchanged.
        """
        if self.search(key):
            return  # Don't insert duplicates

        new_node = Node(key)
        l, r = _split(self.root, key)
        # l has keys < key, r has keys >= key.
        # Merge new_node with r first, then merge l with the result.
        self.root = _merge(l, _merge(new_node, r))

    def delete(self, key):
        """
        Deletes a key from the Treap. If the key is not found, the tree is unchanged.
        """
        if not self.search(key):
            return

        # Split to isolate the node to be deleted.
        l, r = _split(self.root, key)  # l has keys < key, r has keys >= key
        _, r_prime = _split(r, key + 1)  # r_prime has keys > key

        # Merge the remaining parts back together.
        self.root = _merge(l, r_prime)
