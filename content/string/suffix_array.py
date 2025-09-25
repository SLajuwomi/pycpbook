"""
Author: PyCPBook Community
Source: CP-Algorithms, GeeksForGeeks
Description: Implements the construction of a Suffix Array and a Longest Common
Prefix (LCP) Array. A suffix array is a sorted array of all suffixes of a given
string. The LCP array stores the length of the longest common prefix between
adjacent suffixes in the sorted suffix array.

Suffix Array Construction ($O(N \\log^2 N)$):
The algorithm works by repeatedly sorting the suffixes based on prefixes of
increasing lengths that are powers of two.
1.  Initially, suffixes are sorted based on their first character.
2.  In the k-th iteration, suffixes are sorted based on their first $2^k$
    characters. This is done efficiently by using the ranks from the previous
    iteration. Each suffix `s[i:]` is represented by a pair of ranks: the rank
    of its first $2^{k-1}$ characters and the rank of the next $2^{k-1}$
    characters (starting at `s[i + 2^{k-1}:]`).
3.  This process continues for $\\log N$ iterations, with each sort taking
    $O(N \\log N)$ time, leading to an overall complexity of $O(N \\log^2 N)$.

LCP Array Construction (Kasai's Algorithm, $O(N)$):
After the suffix array `sa` is built, the LCP array can be constructed in linear
time using Kasai's algorithm. The algorithm utilizes the observation that the LCP
of two suffixes `s[i:]` and `s[j:]` is related to the LCP of `s[i-1:]` and `s[j-1:]`.
It processes the suffixes in their original order in the string, not the sorted
order, which allows it to compute the LCP values efficiently.

Time: $O(N \\log^2 N)$ for building the suffix array and $O(N)$ for the LCP array.
Total time complexity is dominated by the suffix array construction.
Space: $O(N)$ to store the suffix array, LCP array, and auxiliary arrays for sorting.
Status: Stress-tested
"""


def build_suffix_array(s):
    """
    Builds the suffix array for a string using an O(N log^2 N) sorting-based approach.

    Args:
        s (str): The input string.

    Returns:
        list[int]: The suffix array, containing starting indices of suffixes in
                   lexicographically sorted order.
    """
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    k = 1
    while k < n:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        for i in range(1, n):
            prev, curr = sa[i - 1], sa[i]
            r_prev = (rank[prev], rank[prev + k] if prev + k < n else -1)
            r_curr = (rank[curr], rank[curr + k] if curr + k < n else -1)
            if r_curr == r_prev:
                new_rank[curr] = new_rank[prev]
            else:
                new_rank[curr] = new_rank[prev] + 1
        rank = new_rank
        if rank[sa[-1]] == n - 1:
            break
        k *= 2
    return sa


def build_lcp_array(s, sa):
    """
    Builds the LCP array using Kasai's algorithm in O(N) time.

    Args:
        s (str): The input string.
        sa (list[int]): The suffix array for the string `s`.

    Returns:
        list[int]: The LCP array. `lcp[i]` is the LCP of suffixes `sa[i-1]` and `sa[i]`.
                   `lcp[0]` is conventionally 0.
    """
    n = len(s)
    if n == 0:
        return []

    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i

    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        if h > 0:
            h -= 1
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[rank[i]] = h
    return lcp
