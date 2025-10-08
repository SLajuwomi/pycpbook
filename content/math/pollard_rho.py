"""
Implements Pollard's Rho algorithm for integer factorization, combined with Miller-Rabin primality test for a complete factorization routine.
Pollard's Rho is a probabilistic algorithm to find a non-trivial factor of a composite number `n`. It's particularly efficient at finding small factors. The algorithm uses Floyd's cycle-detection algorithm on a sequence of pseudorandom numbers modulo `n`, defined by $x_{i+1} = (x_i^2 + c) \\\\mod n$. A factor is likely found when `\\\\text{gcd}(|x_j - x_i|, n) > 1`.
The `factorize` function returns a sorted list of prime factors of a given number `n`. It first checks for primality using Miller-Rabin. If `n` is composite, it uses Pollard's Rho to find one factor `d`, and then recursively factorizes `d` and `n/d`.
"""

import math
import random
from content.math.miller_rabin import is_prime


def _pollard_rho_factor(n):
    """Finds a non-trivial factor of n using Pollard's Rho. n must be composite."""
    if n % 2 == 0:
        return 2

    f = lambda val, c: (pow(val, 2, n) + c) % n

    while True:
        x = random.randint(1, n - 2)
        y = x
        c = random.randint(1, n - 1)
        d = 1

        while d == 1:
            x = f(x, c)
            y = f(f(y, c), c)
            d = math.gcd(abs(x - y), n)

        if d != n:
            return d


def factorize(n):
    if n <= 1:
        return []

    factors = []

    def get_factors(num):
        if num <= 1:
            return
        if is_prime(num):
            factors.append(num)
            return

        factor = _pollard_rho_factor(num)
        get_factors(factor)
        get_factors(num // factor)

    get_factors(n)
    factors.sort()
    return factors
