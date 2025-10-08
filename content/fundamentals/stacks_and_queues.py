"""
This guide explains how to implement and use stacks and queues,
two of the most fundamental linear data structures in computer science, using
Python's built-in features.
Stack (LIFO - Last-In, First-Out):
A stack is a data structure that follows the LIFO principle. The last element
added to the stack is the first one to be removed. Think of it like a stack of
plates: you add a new plate to the top and also remove a plate from the top.
In Python, a standard `list` can be used as a stack.
- `append()`: Pushes a new element onto the top of the stack. This is an
  amortized $O(1)$ operation.
- `pop()`: Removes and returns the top element of the stack. This is an $O(1)$
  operation.
Queue (FIFO - First-In, First-Out):
A queue is a data structure that follows the FIFO principle. The first element
added to the queue is the first one to be removed, like a checkout line at a
store. While a Python `list` can be used as a queue with `append()` and `pop(0)`,
this is inefficient because `pop(0)` takes $O(N)$ time, as all subsequent
elements must be shifted.
The correct and efficient way to implement a queue is using `collections.deque`
(double-ended queue).
- `append()`: Adds an element to the right end (back) of the queue in $O(1)$.
- `popleft()`: Removes and returns the element from the left end (front) of the
  queue in $O(1)$.
`deque` is highly optimized for appends and pops from both ends.
"""

from collections import deque


def stack_and_queue_examples():
    """
    Demonstrates the usage of stacks (with lists) and queues (with deque).
    This function is primarily for inclusion in the notebook and is called
    by the stress test to ensure correctness.
    """
    # --- Stack Example (LIFO) ---
    stack = []
    stack.append(10)  # Stack: [10]
    stack.append(20)  # Stack: [10, 20]
    stack.append(30)  # Stack: [10, 20, 30]

    popped_from_stack = []
    popped_from_stack.append(stack.pop())  # Returns 30, Stack: [10, 20]
    popped_from_stack.append(stack.pop())  # Returns 20, Stack: [10]

    # --- Queue Example (FIFO) ---
    queue = deque()
    queue.append(10)  # Queue: deque([10])
    queue.append(20)  # Queue: deque([10, 20])
    queue.append(30)  # Queue: deque([10, 20, 30])

    popped_from_queue = []
    popped_from_queue.append(queue.popleft())  # Returns 10, Queue: deque([20, 30])
    popped_from_queue.append(queue.popleft())  # Returns 20, Queue: deque([30])

    return {
        "final_stack": stack,
        "popped_from_stack": popped_from_stack,
        "final_queue": list(queue),  # Convert to list for easy comparison
        "popped_from_queue": popped_from_queue,
    }
