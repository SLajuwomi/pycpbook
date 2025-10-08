"""
Implements a string hashing class using the polynomial rolling hash
technique. This allows for efficient comparison of substrings. After an initial
$O(N)$ precomputation on a string of length $N$, the hash of any substring can be
calculated in $O(1)$ time.
The hash of a string $s = s_0s_1...s_{k-1}$ is defined as:
$H(s) = (s_0 p^0 + s_1 p^1 + ... + s_{k-1} p^{k-1}) \\mod m$
where `p` is a base and `m` is a large prime modulus.
To prevent collisions, especially against adversarial test cases, this
implementation uses two key techniques:
1.  Randomized Base: The base `p` is chosen randomly at runtime. It should be
    larger than the size of the character set.
2.  Multiple Moduli: Hashing is performed with two different large prime moduli
    (`m1`, `m2`). Two substrings are considered equal only if their hash values
    match for both moduli. This drastically reduces the probability of collisions.
The `query(l, r)` method calculates the hash of the substring `s[l...r-1]` by
using precomputed prefix hashes and powers of `p`.
"""

import random


class StringHasher:
    def __init__(self, s):
        self.s = s
        self.n = len(s)

        self.m1 = 10**9 + 7
        self.m2 = 10**9 + 9

        self.p = random.randint(257, self.m1 - 1)

        self.p_powers1 = [1] * (self.n + 1)
        self.p_powers2 = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.p_powers1[i] = (self.p_powers1[i - 1] * self.p) % self.m1
            self.p_powers2[i] = (self.p_powers2[i - 1] * self.p) % self.m2

        self.h1 = [0] * (self.n + 1)
        self.h2 = [0] * (self.n + 1)
        for i in range(self.n):
            self.h1[i + 1] = (self.h1[i] * self.p + ord(self.s[i])) % self.m1
            self.h2[i + 1] = (self.h2[i] * self.p + ord(self.s[i])) % self.m2

    def query(self, l, r):
        """
        Computes the hash of the substring s[l...r-1].

        Args:
            l (int): The 0-based inclusive starting index.
            r (int): The 0-based exclusive ending index.

        Returns:
            tuple[int, int]: A tuple containing the two hash values for the substring.
        """
        if l >= r:
            return 0, 0

        len_sub = r - l
        hash1 = (
            self.h1[r] - (self.h1[l] * self.p_powers1[len_sub]) % self.m1 + self.m1
        ) % self.m1
        hash2 = (
            self.h2[r] - (self.h2[l] * self.p_powers2[len_sub]) % self.m2 + self.m2
        ) % self.m2
        return hash1, hash2
