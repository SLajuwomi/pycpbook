"""
Implements a standard, unbalanced Binary Search Tree (BST). A BST is
a rooted binary tree data structure whose internal nodes each store a key greater
than all keys in the node's left subtree and less than those in its right subtree.
This data structure provides efficient average-case time complexity for search,
insert, and delete operations. However, its primary drawback is that these
operations can degrade to $O(N)$ in the worst case if the tree becomes unbalanced
(e.g., when inserting elements in sorted order, the tree becomes a linked list).
This implementation serves as a foundational example and a good contrast to the
balanced BSTs (like Treaps) also included in this notebook, which guarantee
$O(\log N)$ performance.
The `delete` operation handles the three standard cases:
1. The node to be deleted is a leaf (no children).
2. The node has one child.
3. The node has two children (in which case it's replaced by its in-order successor).
Average case for `search`, `insert`, `delete` is $O(\log N)$.
Worst case is $O(N)$. Space complexity is $O(N)$ to store the nodes of the tree.
"""


class Node:
    """Represents a single node in the Binary Search Tree."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """A standard (unbalanced) Binary Search Tree implementation."""

    def __init__(self):
        self.root = None

    def search(self, key):
        """Searches for a key in the BST."""
        return self._search_recursive(self.root, key) is not None

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def insert(self, key):
        """Inserts a key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def delete(self, key):
        """Deletes a key from the BST."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the in-order successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
