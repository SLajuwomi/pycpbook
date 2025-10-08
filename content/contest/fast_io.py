"""
This guide provides a comprehensive overview of fast I/O techniques
in Python for competitive programming. Standard `input()` can be too slow for
problems with large inputs, leading to Time Limit Exceeded (TLE) verdicts.
Using the `sys` module provides a much faster alternative.

1. The `sys.stdin` Object:
   - `sys.stdin` is a file object representing standard input. You can read from it
     like you would from a file. This is more efficient than the built-in `input()`
     function, which performs extra processing on each line.

2. Reading a Single Line: `sys.stdin.readline()`
   - This is the most common replacement for `input()`. It reads one line from
     standard input, including the trailing newline character (`\\\\n`).
   - You almost always need to strip this newline using `.strip()`.
   - Example: `line = sys.stdin.readline().strip()`

3. Reading All Lines: `sys.stdin.readlines()`
   - This function reads all lines from standard input until EOF (End-of-File)
     and returns them as a list of strings.
   - This is useful when the entire input fits into memory and can be processed
     at once. Each string in the list retains its trailing newline.

4. Reading the Entire Stream: `sys.stdin.read()`
   - This function reads the entire input stream until EOF and returns it as a
     single string. This can be useful for problems with non-line-based input.

5. Iterating over `sys.stdin`:
   - Since `sys.stdin` is an iterator, you can loop over it directly. This is an
     elegant way to process input line by line when the number of lines is not
     given beforehand.
   - Example: `for line in sys.stdin: process(line.strip())`

6. Using `next(sys.stdin)`:
   - This allows you to consume lines from the iterator one at a time, which can
     be cleaner than mixing `readline()` with a `for` loop.
   - Example: `n = int(next(sys.stdin))`
   - Example: `data = [int(x) for x in next(sys.stdin).split()]`

Common Parsing Patterns:
The functions below demonstrate how to wrap these techniques into convenient
helpers, similar to those in `template.py`.
Time: N/A
Space: N/A
Status: Not applicable (Informational)
"""

import sys


def get_ints_from_line():
    """
    Reads a line of space-separated values and parses them into a list of integers.
    This is a common helper function.
    """
    return list(map(int, sys.stdin.readline().split()))


def process_all_lines():
    """
    Demonstrates reading all lines at once and processing them.
    This example calculates the sum of the first integer on each line.
    """
    lines = sys.stdin.readlines()
    total = 0
    for line in lines:
        if line.strip():
            total += int(line.split()[0])
    return total


def iterate_over_stdin():
    """
    Demonstrates processing input by iterating over sys.stdin, which reads
    line by line until EOF.
    """
    total = 0
    for line in sys.stdin:
        if line.strip():
            total += sum(map(int, line.split()))
    return total


def demonstrate_usage_conceptual():
    """
    This function is for inclusion in the notebook as a clear example and
    is not meant to be executed directly as part of a test. It shows a common
    contest pattern: reading a count `N`, followed by `N` lines of data.
    """
    try:
        # Read N, the number of lines to follow
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)

        # Read N lines into a matrix
        matrix = []
        for _ in range(n):
            row = list(map(int, sys.stdin.readline().split()))
            matrix.append(row)

        # In a real problem, you would process the matrix here.
        # For demonstration, we just show it was read.
        # print("Matrix received:", matrix)

    except (IOError, ValueError):
        # Handle potential empty input or parsing errors gracefully.
        pass
