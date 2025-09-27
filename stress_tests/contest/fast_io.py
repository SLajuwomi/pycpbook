"""
@description
This script is a correctness test for the fast I/O examples provided in
`content/contest/fast_io.py`. It ensures that the example code snippets are
syntactically correct and produce the expected results.

This is not a "stress test" in the traditional sense but a validation script
to prevent errors in the educational content of the notebook. It uses
`io.StringIO` to simulate `sys.stdin`.
"""

import sys
import os
import io

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.contest.fast_io import (
    get_ints_from_line,
    process_all_lines,
    iterate_over_stdin,
)


def run_test():
    """
    Executes the example functions and asserts the correctness of their output
    by simulating stdin.
    """
    original_stdin = sys.stdin

    try:
        # Test get_ints_from_line
        simulated_input_1 = "10 20 30\n"
        sys.stdin = io.StringIO(simulated_input_1)
        result_1 = get_ints_from_line()
        assert result_1 == [
            10,
            20,
            30,
        ], f"get_ints_from_line failed. Expected [10, 20, 30], Got {result_1}"

        # Test process_all_lines
        simulated_input_2 = "1 a b\n2 c d\n3 e f\n"
        sys.stdin = io.StringIO(simulated_input_2)
        result_2 = process_all_lines()
        assert result_2 == 6, f"process_all_lines failed. Expected 6, Got {result_2}"

        # Test iterate_over_stdin
        simulated_input_3 = "1 2 3\n4 5\n6\n"
        sys.stdin = io.StringIO(simulated_input_3)
        result_3 = iterate_over_stdin()
        assert result_3 == 21, f"iterate_over_stdin failed. Expected 21, Got {result_3}"

    finally:
        # Restore original stdin to avoid side effects
        sys.stdin = original_stdin

    print("Fast I/O: All examples are correct!")


if __name__ == "__main__":
    run_test()
