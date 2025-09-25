"""
Author: PyCPBook Community
Source: Python official documentation
Description: This guide explains how to use `@functools.cache` for transparently
adding memoization to a function. Memoization is an optimization technique where
the results of expensive function calls are stored and returned for the same
inputs, avoiding redundant computation.

`@functools.cache`:
This decorator wraps a function with a memoizing callable that saves up to the
`maxsize` most recent calls. Because it's a hash-based cache, all arguments
to the function must be hashable.

In competitive programming, this is extremely powerful for simplifying dynamic
programming problems that have a natural recursive structure. A recursive
solution that would normally be too slow due to recomputing the same subproblems
can become efficient by simply adding the `@cache` decorator.

The example below demonstrates this with the Fibonacci sequence. The naive
recursive solution has an exponential time complexity, $O(2^N)$. With `@cache`,
each state `fib(n)` is computed only once, reducing the complexity to linear, $O(N)$,
the same as a standard iterative DP solution.

Time: The decorated function's complexity becomes proportional to the number of
unique states it's called with, rather than the total number of calls.
Space: $O(S)$ where $S$ is the number of unique states (sets of arguments) stored
in the cache.
Status: Stress-tested
"""

import functools


@functools.cache
def fibonacci_with_cache(n):
    """
    Computes the n-th Fibonacci number using recursion with memoization.
    This function is primarily for demonstrating @functools.cache.
    """
    if n < 2:
        return n
    return fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)
