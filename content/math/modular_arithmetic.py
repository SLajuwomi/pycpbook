"""
This module provides essential functions for modular arithmetic,
a cornerstone of number theory in competitive programming. It includes
modular exponentiation, the Extended Euclidean Algorithm, and modular
multiplicative inverse.
Modular Exponentiation:
The `power` function computes $(base^{exp}) \\pmod{mod}$ efficiently using the
binary exponentiation (also known as exponentiation by squaring) method. This
avoids the massive intermediate numbers that would result from calculating
$base^{exp}$ directly. The time complexity is logarithmic in the exponent.
Extended Euclidean Algorithm:
The `extended_gcd` function computes the greatest common divisor (GCD) of two
integers `a` and `b`. In addition, it finds two integer coefficients, `x` and `y`,
that satisfy Bezout's identity: $a \\cdot x + b \\cdot y = \\gcd(a, b)$. This is
fundamental for many number-theoretic calculations.
Modular Multiplicative Inverse:
The `mod_inverse` function finds a number `x` such that $(a \\cdot x) \\equiv 1 \\pmod{m}$.
This `x` is the modular multiplicative inverse of `a` modulo `m`. An inverse
exists if and only if `a` and `m` are coprime (i.e., $\\gcd(a, m) = 1$). This
implementation uses the Extended Euclidean Algorithm. From $a \\cdot x + m \\cdot y = 1$,
taking the equation modulo `m` gives $a \\cdot x \\equiv 1 \\pmod{m}$. Thus, the
coefficient `x` is the desired inverse.
- `power`: $O(\\\\log(exp))$
- `extended_gcd`: $O(\\\\log(\\\\min(a, b)))$
- `mod_inverse`: $O(\\\\log m)$
- All functions use $O(1)$ extra space for iterative versions.
"""


def power(base, exp, mod):
    """
    Computes (base^exp) % mod using binary exponentiation.
    """
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res


def extended_gcd(a, b):
    """
    Returns (gcd, x, y) such that a*x + b*y = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    """
    Computes the modular multiplicative inverse of a modulo m.
    Returns None if the inverse does not exist.
    """
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    else:
        return (x % m + m) % m
