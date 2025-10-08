"""
Implements the Miller-Rabin primality test, a probabilistic
algorithm for determining whether a given number is prime. It is highly
efficient and is the standard method for primality testing in competitive
programming for numbers that are too large for a sieve.
The algorithm is based on properties of square roots of unity modulo a prime
number and Fermat's Little Theorem. For a number `n` to be tested, we first
write `n - 1` as `2^s * d`, where `d` is odd. The test then proceeds:
1.  Pick a base `a` (a "witness").
2.  Compute `x = a^d mod n`.
3.  If `x == 1` or `x == n - 1`, `n` might be prime, and this test passes for this base.
4.  Otherwise, for `s-1` times, compute `x = x^2 mod n`. If `x` becomes `n - 1`,
    the test passes for this base.
5.  If after these steps, `x` is not `n - 1`, then `n` is definitely composite.
If `n` passes this test for multiple well-chosen bases `a`, it is prime with
a very high probability. For 64-bit integers, a specific set of deterministic
witnesses can be used to make the test 100% accurate. This implementation uses
such a set, making it reliable for contest use.
"""

from content.math.modular_arithmetic import power


def is_prime(n):
    """
    Checks if a number is prime using the Miller-Rabin primality test.
    This implementation is deterministic for all integers up to 2^64.

    Args:
        n (int): The number to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # A set of witnesses that is deterministic for all 64-bit integers.
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in witnesses:
        if a >= n:
            break
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue

        is_composite = True
        for _ in range(s - 1):
            x = power(x, 2, n)
            if x == n - 1:
                is_composite = False
                break
        if is_composite:
            return False

    return True
