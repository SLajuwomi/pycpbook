"""
Author: PyCPBook Community
Source: CP-Algorithms
Description: Implements a solver for a system of linear congruences using the
Chinese Remainder Theorem (CRT). Given a system of congruences:
$x \\equiv a_1 \\pmod{n_1}$
$x \\equiv a_2 \\pmod{n_2}$
...
$x \\equiv a_k \\pmod{n_k}$
the algorithm finds a solution `x` that satisfies all of them. This implementation
handles the general case where the moduli `n_i` are not necessarily pairwise coprime.

The algorithm works by iteratively combining pairs of congruences. Given a solution
for the first `i-1` congruences, `x \equiv a_{res} (mod n_{res})`, it combines
this with the i-th congruence `x \equiv a_i (mod n_i)`.

This requires solving a linear congruence of the form `k * n_{res} \equiv a_i - a_{res} (mod n_i)`.
A solution exists if and only if `(a_i - a_{res})` is divisible by `g = gcd(n_{res}, n_i)`.
If a solution exists, the two congruences are merged into a new one:
`x \equiv a_{new} (mod n_{new})`, where `n_{new} = lcm(n_{res}, n_i)`.
This process is repeated for all congruences. If at any step a solution does not exist,
the entire system has no solution.

Time: $O(K \\cdot \\log(\max(n_i)))$, where $K$ is the number of congruences.
Each merge step involves `extended_gcd`, which is logarithmic.
Space: $O(1)$
Status: Stress-tested
"""

from content.math.modular_arithmetic import extended_gcd


def chinese_remainder_theorem(remainders, moduli):
    """
    Solves a system of linear congruences.
    `x \equiv remainders[i] (mod moduli[i])` for all i.

    Args:
        remainders (list[int]): A list of remainders (a_i).
        moduli (list[int]): A list of moduli (n_i).

    Returns:
        tuple[int, int] | None: A tuple `(result, lcm)` representing the solution
        `x \equiv result (mod lcm)`, or None if no solution exists.
    """
    if not remainders or not moduli or len(remainders) != len(moduli):
        return 0, 1

    a1 = remainders[0]
    n1 = moduli[0]

    for i in range(1, len(remainders)):
        a2 = remainders[i]
        n2 = moduli[i]

        g, x, _ = extended_gcd(n1, n2)

        if (a1 - a2) % g != 0:
            return None

        # Solve k * n1 \equiv a2 - a1 (mod n2)
        # k * (n1/g) \equiv (a2 - a1)/g (mod n2/g)
        # k \equiv ((a2 - a1)/g) * inv(n1/g) (mod n2/g)
        # inv(n1/g) mod (n2/g) is x from extended_gcd(n1, n2)
        k0 = (x * ((a2 - a1) // g)) % (n2 // g)

        # New solution: x = a1 + k*n1. With k = k0 + t*(n2/g)
        # x = a1 + (k0 + t*(n2/g)) * n1 = (a1 + k0*n1) + t*lcm(n1, n2)
        a1 = a1 + k0 * n1
        n1 = n1 * (n2 // g)  # lcm(n1, n2)
        a1 %= n1

    return a1, n1
