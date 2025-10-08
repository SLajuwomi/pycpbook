"""
Implements Manacher's algorithm for finding the longest palindromic
substring in a given string in linear time. Standard naive approaches take
$O(N^2)$ or $O(N^3)$ time.
The algorithm cleverly handles both odd and even length palindromes by
transforming the input string. A special character (e.g., '#') is inserted
between each character and at the ends. For example, "aba" becomes "#a#b#a#"
and "abba" becomes "#a#b#b#a#". In this new string, every palindrome, regardless
of its original length, is of odd length and has a distinct center.
The core of the algorithm is to compute an array `p`, where `p[i]` stores the
radius of the palindrome centered at index `i` in the transformed string.
It does this efficiently by maintaining the center `c` and right boundary `r`
of the palindrome that extends furthest to the right. When computing `p[i]`,
it uses the information from the mirror position `i_mirror = 2*c - i` to get an
initial guess for `p[i]`. It then expands from this guess, avoiding redundant
character comparisons. This optimization is what brings the complexity down to
linear time.
After computing the `p` array, the maximum value in `p` corresponds to the
radius of the longest palindromic substring. From this radius and its center,
the original substring can be reconstructed.
"""


def manacher(s):
    """
    Finds the longest palindromic substring in a string using Manacher's algorithm.

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindromic substring found in `s`. If there are
             multiple of the same maximum length, it returns the first one found.
    """
    if not s:
        return ""

    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n
    center, right = 0, 0
    max_len, max_center = 0, 0

    for i in range(n):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        while (
            i - (p[i] + 1) >= 0
            and i + (p[i] + 1) < n
            and t[i - (p[i] + 1)] == t[i + (p[i] + 1)]
        ):
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

        if p[i] > max_len:
            max_len = p[i]
            max_center = i

    start = (max_center - max_len) // 2
    end = start + max_len
    return s[start:end]
