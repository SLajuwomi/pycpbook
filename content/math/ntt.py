"""
Implements the Number Theoretic Transform (NTT) for fast
polynomial multiplication over a finite field. NTT is an adaptation of the
Fast Fourier Transform (FFT) for modular arithmetic, avoiding floating-point
precision issues. It is commonly used in problems involving polynomial
convolution, such as multiplying large numbers or finding the number of ways
to form a sum.
The algorithm works by:
1.  Choosing a prime modulus `MOD` of the form `c * 2^k + 1` and a primitive
    root `ROOT` of `MOD`.
2.  Evaluating the input polynomials at the powers of `ROOT` (the "roots of unity").
    This is the forward NTT, which transforms the polynomials from coefficient
    representation to point-value representation in $O(N \\log N)$ time.
3.  Multiplying the resulting point-value representations element-wise in $O(N)$ time.
4.  Interpolating the resulting polynomial back to coefficient representation using
    the inverse NTT in $O(N \\log N)$ time.
This implementation uses the prime `MOD = 998244353`, which is a standard choice
in competitive programming.
"""

from content.math.modular_arithmetic import power

MOD = 998244353
ROOT = 3
ROOT_PW = 1 << 23
ROOT_INV = power(ROOT, MOD - 2, MOD)


def ntt(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = power(ROOT_INV if invert else ROOT, (MOD - 1) // length, MOD)
        i = 0
        while i < n:
            w = 1
            for j in range(length // 2):
                u = a[i + j]
                v = (a[i + j + length // 2] * w) % MOD
                a[i + j] = (u + v) % MOD
                a[i + j + length // 2] = (u - v + MOD) % MOD
                w = (w * wlen) % MOD
            i += length
        length <<= 1

    if invert:
        n_inv = power(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = (a[i] * n_inv) % MOD


def multiply(a, b):
    if not a or not b:
        return []

    res_len = len(a) + len(b) - 1
    n = 1
    while n < res_len:
        n <<= 1

    fa = a[:] + [0] * (n - len(a))
    fb = b[:] + [0] * (n - len(b))

    ntt(fa, False)
    ntt(fb, False)

    for i in range(n):
        fa[i] = (fa[i] * fb[i]) % MOD

    ntt(fa, True)

    return fa[:res_len]
