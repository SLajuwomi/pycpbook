"""
Author: PyCPBook Community
Source: Various competitive programming resources
Description: A standard template for Python in programming contests. It provides
fast I/O, an increased recursion limit, and common helper functions to accelerate
development under time constraints.

Fast I/O:
This template redefines `input` to use `sys.stdin.readline()` for performance.
For a detailed guide on various fast I/O patterns and their usage, please refer
to the "Fast I/O" section in this chapter.

Recursion Limit:
Python's default recursion limit (often 1000) is too low for problems that
involve deep recursion. `sys.setrecursionlimit(10**6)` increases this limit to
avoid `RecursionError` on large test cases.

Usage:
Place problem-solving logic inside the `solve()` function. The main execution
block is set up to call this function, with a commented-out loop for handling
multiple test cases.
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
