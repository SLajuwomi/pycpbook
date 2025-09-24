"""
Author: PyCPBook Community
Source: Various competitive programming resources
Description: A standard template for Python in programming contests.
It provides fast I/O, increased recursion limit, and common helper functions
to accelerate development under time constraints.

Fast I/O:
Standard `input()` can be slow. This template redefines `input` to use
`sys.stdin.readline()`, which is significantly faster for large inputs.
Helper functions like `get_int()` and `get_ints()` are provided for convenience.
For output, printing with `\\n` is generally fast enough, but for a huge number
of output operations, `sys.stdout.write()` can be used.

Recursion Limit:
Python's default recursion limit (often 1000) is too low for problems
involving deep recursion, such as tree/graph traversals on large datasets.
`sys.setrecursionlimit(10**6)` increases this limit to avoid `RecursionError`.

Usage:
Place your problem-solving logic inside the `solve()` function. The main
execution block is set up to call this function. If the problem has multiple
test cases, you can use the commented-out loop in the `main` function.
Time: N/A
Space: N/A
Status: Not applicable (Utility)
"""

import sys
import math
import os

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def get_int():
    """Reads a single integer from a line."""
    return int(input())


def get_ints():
    """Reads a list of space-separated integers from a line."""
    return list(map(int, input().split()))


def get_str():
    """Reads a single string from a line, stripping trailing whitespace."""
    return input().strip()


def get_strs():
    """Reads a list of space-separated strings from a line."""
    return input().strip().split()


def solve():
    """
    This is the main function where the solution logic for a single
    test case should be implemented.
    """
    try:
        n, m = get_ints()
        print(n + m)
    except (IOError, ValueError):
        pass


def main():
    """
    Main execution function.
    Handles multiple test cases if required.
    """
    # t = get_int()
    # for _ in range(t):
    #     solve()
    solve()


if __name__ == "__main__":
    main()
