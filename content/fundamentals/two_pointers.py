"""
Author: PyCPBook Community
Source: LeetCode, TopCoder
Description: This guide explains the Two Pointers and Sliding Window techniques,
which are powerful for solving array and string problems efficiently.

Two Pointers:
The two-pointers technique involves using two pointers to traverse a data
structure, often an array or string, in a coordinated way. The pointers can
move in various patterns:
1. Converging Pointers: One pointer starts at the beginning and the other at the
   end. They move towards each other until they meet or cross. This is common
   for problems on sorted arrays, like finding a pair with a specific sum.
2. Same-Direction Pointers (Sliding Window): Both pointers start at or near the
   beginning and move in the same direction. One pointer (`right`) expands a
   "window," and the other (`left`) contracts it.

Sliding Window:
This is a specific application of the two-pointers technique. A "window" is a
subsegment of the data (e.g., a subarray or substring) represented by the
indices `[left, right]`. The `right` pointer expands the window, and the `left`
pointer contracts it, typically to maintain a certain property or invariant
within the window. This avoids the re-computation that plagues naive O(N^2)
solutions by only adding/removing one element at a time.

The example below, "Longest Substring with At Most K Distinct Characters," is a
classic sliding window problem. The window `s[left:right+1]` is expanded by
incrementing `right`. If the number of distinct characters in the window exceeds
`k`, the window is contracted from the left by incrementing `left` until the
condition is met again.

Time: $O(N)$, where $N$ is the length of the input string/array, because each
pointer traverses the data structure at most once.
Space: $O(K)$ or $O(\Sigma)$, where $K$ is the number of distinct elements allowed
or $\Sigma$ is the size of the character set, to store the elements in the window.
Status: To be stress-tested.
"""

from collections import defaultdict


def longest_substring_with_k_distinct(s, k):
    """
    Finds the length of the longest substring of s that contains at most k
    distinct characters.

    Args:
        s (str): The input string.
        k (int): The maximum number of distinct characters allowed.

    Returns:
        int: The length of the longest valid substring.
    """
    if k == 0:
        return 0

    n = len(s)
    left = 0
    max_len = 0
    char_counts = defaultdict(int)

    for right in range(n):
        char_counts[s[right]] += 1

        while len(char_counts) > k:
            char_left = s[left]
            char_counts[char_left] -= 1
            if char_counts[char_left] == 0:
                del char_counts[char_left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
