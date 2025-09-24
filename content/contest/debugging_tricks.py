"""
Author: PyCPBook Community
Source: Collective experience from competitive programmers.
Description: This section outlines common debugging techniques and tricks
useful in a competitive programming context. Since standard debuggers are
often unavailable or too slow on online judges, these methods are invaluable.

1. Debug Printing to stderr:
   - The most common technique is to print variable states at different points
     in the code.
   - Always print to standard error (`sys.stderr`) instead of standard output
     (`sys.stdout`). The online judge ignores `stderr`, so your debug messages
     won't interfere with the actual output and cause a "Wrong Answer" verdict.
   - Example: `print(f"DEBUG: Current value of x is {x}", file=sys.stderr)`

2. Test with Edge Cases:
   - Before submitting, always test your code with edge cases.
   - Minimum constraints: e.g., N=0, N=1, empty list.
   - Maximum constraints: e.g., N=10^5. (Check for TLE - Time Limit Exceeded).
   - Special values: e.g., zeros, negative numbers, duplicates.
   - A single off-by-one error can often be caught by testing N=1 or N=2.

3. Assertions:
   - Use `assert` to check for invariants in your code. An invariant is a
     condition that should always be true at a certain point.
   - For example, if a variable `idx` should always be non-negative, you
     can add `assert idx >= 0`.
   - If the assertion fails, your program will crash with an `AssertionError`,
     immediately showing you where the logic went wrong.
   - Assertions are automatically disabled in Python's optimized mode (`python -O`),
     so they have no performance penalty on the judge if it runs in that mode.

4. Naive Solution Comparison:
   - If you have a complex, optimized algorithm, write a simple, brute-force
     (naive) solution that is obviously correct but slow.
   - Generate a large number of small, random test cases.
   - Run both your optimized solution and the naive solution on each test case
     and assert that their outputs are identical.
   - If they differ, print the failing test case. This is the core idea behind
     the stress tests used in this project.

5. Rubber Duck Debugging:
   - Explain your code, line by line, to someone else or even an inanimate
     object (like a rubber duck).
   - The act of verbalizing your logic often helps you spot the flaw yourself.
Time: N/A
Space: N/A
Status: Not applicable (Informational)
"""

import sys


def example_debug_print():
    """
    A simple example demonstrating how to print debug information
    to stderr without affecting the program's actual output.
    """
    data = [10, 20, 30]

    # This is the actual output that the judge will see.
    print("Processing started.")

    total = 0
    for i, item in enumerate(data):
        # This is a debug message. It goes to stderr and is ignored by the judge.
        print(f"DEBUG: Processing item {i} with value {item}", file=sys.stderr)
        total += item

    # This is the final output.
    print(f"The final total is: {total}")
