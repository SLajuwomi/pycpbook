"""
Linked lists are node-based sequences where each node holds a value and
references to neighbors. They enable $O(1)$ insertion/removal at ends or at a
known node without shifting elements. This is useful when many insertions and
deletions are required and random access is not needed. In competitive
programming, arrays (lists) are usually faster, but linked lists are important
to understand for interview-style problems and for learning pointer-like
manipulations in Python using object references.

Singly linked list maintains `head` and optionally `tail` with nodes pointing
forward. Doubly linked list maintains both `prev` and `next` pointers for each
node, making deletions of arbitrary nodes simpler. Python uses garbage
collection, so removing references typically frees nodes without manual memory
management.

Complexities (typical):
- Access by index: $O(N)$
- push_front / pop_front: $O(1)$
- push_back / pop_back: $O(1)$ if `tail` maintained, else $O(N)$
- find by value: $O(N)$
- insert after known node: $O(1)$, after value: $O(N)$ to find + $O(1)$ insert
- delete by value: $O(N)$ to find + $O(1)$ unlink

Classic patterns:
- Reverse in-place in $O(N)$ using three-pointer technique
- Middle node using fast/slow pointers; returns index $\lfloor N/2 \rfloor$
- Cycle detection using Floyd’s algorithm in $O(N)$ and $O(1)$ space

Python specifics:
- Objects are referenced; pointers are simulated by storing object references
- No pointer arithmetic; operations rewire `next`/`prev` fields
- Avoid negative indexing expectations; traversal is explicit
"""


class NodeS:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, val):
        node = NodeS(val)
        node.next = self.head
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def push_back(self, val):
        node = NodeS(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return None
        v = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return v

    def pop_back(self):
        if self.size == 0:
            return None
        if self.size == 1:
            return self.pop_front()
        prev = self.head
        while prev.next is not self.tail:
            prev = prev.next
        v = self.tail.val
        prev.next = None
        self.tail = prev
        self.size -= 1
        return v

    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur
            cur = cur.next
        return None

    def insert_after_value(self, target, val):
        cur = self.head
        while cur and cur.val != target:
            cur = cur.next
        if not cur:
            return False
        node = NodeS(val)
        node.next = cur.next
        cur.next = node
        if cur is self.tail:
            self.tail = node
        self.size += 1
        return True

    def delete_value(self, val):
        if self.size == 0:
            return False
        if self.head.val == val:
            self.pop_front()
            return True
        prev = self.head
        cur = self.head.next
        while cur and cur.val != val:
            prev = cur
            cur = cur.next
        if not cur:
            return False
        prev.next = cur.next
        if cur is self.tail:
            self.tail = prev
        self.size -= 1
        return True

    def reverse(self):
        prev = None
        cur = self.head
        self.tail = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
        if self.head is None:
            self.tail = None

    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def to_list(self):
        res = []
        cur = self.head
        cnt = 0
        while cur and cnt < self.size:
            res.append(cur.val)
            cur = cur.next
            cnt += 1
        return res

    @classmethod
    def from_list(cls, arr):
        ll = cls()
        for v in arr:
            ll.push_back(v)
        return ll


class NodeD:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, val):
        node = NodeD(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def push_back(self, val):
        node = NodeD(val)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return None
        v = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return v

    def pop_back(self):
        if self.size == 0:
            return None
        v = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        self.size -= 1
        if self.size == 0:
            self.head = None
        return v

    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur
            cur = cur.next
        return None

    def insert_after_value(self, target, val):
        cur = self.head
        while cur and cur.val != target:
            cur = cur.next
        if not cur:
            return False
        node = NodeD(val)
        node.prev = cur
        node.next = cur.next
        if cur.next:
            cur.next.prev = node
        cur.next = node
        if cur is self.tail:
            self.tail = node
        self.size += 1
        return True

    def delete_value(self, val):
        cur = self.head
        while cur and cur.val != val:
            cur = cur.next
        if not cur:
            return False
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.head = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev
        self.size -= 1
        return True

    def to_list(self):
        res = []
        cur = self.head
        cnt = 0
        while cur and cnt < self.size:
            res.append(cur.val)
            cur = cur.next
            cnt += 1
        return res

    @classmethod
    def from_list(cls, arr):
        ll = cls()
        for v in arr:
            ll.push_back(v)
        return ll


