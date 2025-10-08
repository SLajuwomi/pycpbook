"""
Implements the Knuth-Morris-Pratt (KMP) algorithm for efficient
string searching. KMP finds all occurrences of a pattern `P` within a text `T`
in linear time.
The core of the KMP algorithm is the precomputation of a "prefix function" or
Longest Proper Prefix Suffix (LPS) array for the pattern. The LPS array, `lps`,
for a pattern of length `M` stores at each index `i` the length of the longest
proper prefix of `P[0...i]` that is also a suffix of `P[0...i]`. A "proper"
prefix is one that is not equal to the entire string.
Example: For pattern `P = "ababa"`, the LPS array is `[0, 0, 1, 2, 3]`.
- `lps[0]` is always 0.
- `lps[1]` ("ab"): No proper prefix is a suffix. Length is 0.
- `lps[2]` ("aba"): "a" is both a prefix and a suffix. Length is 1.
- `lps[3]` ("abab"): "ab" is both a prefix and a suffix. Length is 2.
- `lps[4]` ("ababa"): "aba" is both a prefix and a suffix. Length is 3.
During the search, when a mismatch occurs between the text and the pattern at
`text[i]` and `pattern[j]`, the LPS array tells us how many characters of the
pattern we can shift without re-checking previously matched characters.
Specifically, if a mismatch occurs at `pattern[j]`, we know that the prefix
`pattern[0...j-1]` matched the text. The value `lps[j-1]` gives the length of
the longest prefix of `pattern[0...j-1]` that is also a suffix. This means we
can shift the pattern and continue the comparison from `pattern[lps[j-1]]`
without losing any potential matches.
the pattern. $O(M)$ for building the LPS array and $O(N)$ for the search.
"""


def compute_lps(pattern):
    """
    Computes the Longest Proper Prefix Suffix (LPS) array for the KMP algorithm.

    Args:
        pattern (str): The pattern string.

    Returns:
        list[int]: The LPS array for the pattern.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    Finds all occurrences of a pattern in a text using the KMP algorithm.

    Args:
        text (str): The text to search within.
        pattern (str): The pattern to search for.

    Returns:
        list[int]: A list of 0-based starting indices of all occurrences
                   of the pattern in the text.
    """
    n = len(text)
    m = len(pattern)
    if m == 0:
        return list(range(n + 1))
    if n == 0 or m > n:
        return []

    lps = compute_lps(pattern)
    occurrences = []
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences
