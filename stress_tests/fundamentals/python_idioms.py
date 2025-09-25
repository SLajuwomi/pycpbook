"""
@description
This script is a correctness test for the Python idioms examples provided in
`content/fundamentals/python_idioms.py`. It ensures that all the example
code snippets are syntactically correct and produce the expected results.

This is not a "stress test" in the traditional sense but a validation script
to prevent errors in the educational content of the notebook.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.python_idioms import python_idioms_examples


def run_test():
    """
    Executes the example function and asserts the correctness of its output.
    """
    results = python_idioms_examples()

    # Verify list comprehensions
    assert results["squares"] == [0, 1, 4, 9, 16]
    assert results["even_squares"] == [0, 4, 16, 36, 64]

    # Verify set and dict comprehensions
    assert results["unique_squares"] == {1, 4}
    assert results["square_map"] == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    # Verify sorting
    assert results["sorted_by_second"] == [(3, 2), (1, 5), (2, 8)]

    # Verify string manipulations
    assert results["words"] == ["this", "is", "a", "sentence"]
    assert results["rejoined"] == "this-is-a-sentence"
    assert results["reversed_sentence"] == "ecnetnes a si siht"

    # Verify conversions
    assert results["ord_a"] == 97
    assert results["chr_97"] == "a"
    assert results["num_int"] == 123
    assert results["back_to_str"] == "123"

    print("Python Idioms: All examples are correct!")


if __name__ == "__main__":
    run_test()
