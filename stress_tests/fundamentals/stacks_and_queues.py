"""
@description
This script is a correctness test for the stack and queue examples provided in
`content/fundamentals/stacks_and_queues.py`. It ensures that the example
code snippets are syntactically correct and produce the expected results,
validating the educational content.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.stacks_and_queues import stack_and_queue_examples


def run_test():
    """
    Executes the example function and asserts the correctness of its output.
    """
    results = stack_and_queue_examples()

    # --- Verify Stack Behavior ---
    # Initial: [] -> append(10) -> [10] -> append(20) -> [10, 20] -> append(30) -> [10, 20, 30]
    # pop() -> 30, stack is [10, 20]
    # pop() -> 20, stack is [10]
    assert results["final_stack"] == [10]
    assert results["popped_from_stack"] == [30, 20]

    # --- Verify Queue Behavior ---
    # Initial: [] -> append(10) -> [10] -> append(20) -> [10, 20] -> append(30) -> [10, 20, 30]
    # popleft() -> 10, queue is [20, 30]
    # popleft() -> 20, queue is [30]
    assert results["final_queue"] == [30]
    assert results["popped_from_queue"] == [10, 20]

    print("Stacks and Queues: All examples are correct!")


if __name__ == "__main__":
    run_test()
