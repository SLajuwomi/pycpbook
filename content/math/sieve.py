"""
Implements the Sieve of Eratosthenes, a highly efficient algorithm
for finding all prime numbers up to a specified integer `n`.
The algorithm works by iteratively marking as composite (i.e., not prime) the
multiples of each prime, starting with the first prime number, 2.
1. Create a boolean list `is_prime` of size `n+1`, initializing all entries
   to `True`. `is_prime[0]` and `is_prime[1]` are set to `False`.
2. Iterate from `p = 2` up to `sqrt(n)`.
3. If `is_prime[p]` is still `True`, then `p` is a prime number.
4. For this prime `p`, iterate through its multiples starting from `p*p`
   (i.e., `p*p`, `p*p + p`, `p*p + 2p`, ...) and mark them as not prime by
   setting `is_prime[multiple]` to `False`. We can start from `p*p` because
   any smaller multiple `k*p` where `k < p` would have already been marked by
   a smaller prime factor `k`.
5. After the loop, the `is_prime` array contains `True` at indices that are
   prime numbers and `False` otherwise.
This implementation returns the boolean array itself, which is often more
versatile in contests than a list of primes (e.g., for quick primality checks).
A list of primes can be easily generated from this array if needed.
"""


def sieve(n):
    """
    Generates a sieve of primes up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for the sieve (inclusive).

    Returns:
        list[bool]: A boolean list of size n+1 where is_prime[i] is True if i
                    is a prime number, and False otherwise.
    """
    if n < 2:
        return [False] * (n + 1)

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    return is_prime
