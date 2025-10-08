"""
Implements the Z-algorithm, which computes the Z-array for a given
string `s` of length `N`. The Z-array `z` is an array of length `N` where `z[i]`
is the length of the longest common prefix (LCP) between the original string `s`
and the suffix of `s` starting at index `i`. By convention, `z[0]` is usually
set to 0 or `N`; here it is set to 0.
The algorithm computes the Z-array in linear time. It does this by maintaining
the bounds of the rightmost substring that is also a prefix of `s`. This is
called the "Z-box", denoted by `[l, r]`.
The algorithm iterates from `i = 1` to `N-1`:
1. If `i` is outside the current Z-box (`i > r`), it computes `z[i]` naively by
   comparing characters from the start of the string and from index `i`. It then
   updates the Z-box `[l, r]` if a new rightmost one is found.
2. If `i` is inside the current Z-box (`i <= r`), it can use previously computed
   Z-values to initialize `z[i]`. Let `k = i - l`. `z[i]` can be at least
   `min(z[k], r - i + 1)`.
   - If `z[k] < r - i + 1`, then `z[i]` is exactly `z[k]`, and the Z-box does not
     change.
   - If `z[k] >= r - i + 1`, it means `z[i]` might be even longer. The algorithm
     then continues comparing characters from `r+1` onwards to extend the match
     and updates the Z-box `[l, r]`.
The Z-algorithm is very powerful for pattern matching. To find a pattern `P` in
a text `T`, one can compute the Z-array for the concatenated string `P + '$' + T`,
where `$` is a character not in `P` or `T`. Any `z[i]` equal to the length of `P`
indicates an occurrence of `P` in `T`.
"""


def z_function(s):
    """
    Computes the Z-array for a given string.

    Args:
        s (str): The input string.

    Returns:
        list[int]: The Z-array for the string `s`.
    """
    n = len(s)
    if n == 0:
        return []

    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z
