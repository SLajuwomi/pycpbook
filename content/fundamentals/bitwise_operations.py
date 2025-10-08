"""
Bitwise operations are foundational in competitive programming. They allow
constant-time manipulation of integer masks, which represent sets and states.
This section explains the core operators and provides utility functions used
frequently in problems involving subsets, DP on masks, and low-level tricks.

Operators and meaning:
- `&` bitwise AND: keeps a bit only if it is set in both operands
- `|` bitwise OR: sets a bit if it is set in either operand
- `^` bitwise XOR: sets a bit if it is set in exactly one operand
- `~` bitwise NOT: flips all bits
- `<<` left shift: shifts bits left by k positions, introducing zeros on the right
- `>>` right shift: shifts bits right by k positions

In Python, integers are arbitrary precision and use sign-magnitude with infinite
precision logically, so `~x` is `-(x+1)`. For mask manipulations we usually work
with non-negative integers and carefully limit ourselves to the lower N bits.

Common patterns:
- Test i-th bit: `(x >> i) & 1`
- Set i-th bit: `x | (1 << i)`
- Unset i-th bit: `x & ~(1 << i)`
- Toggle i-th bit: `x ^ (1 << i)`
- Lowest set bit (lowbit): `x & -x`

Complexities:
- All single-step operations are $O(1)$.
- Loops over bits are $O(B)$ where $B$ is the number of bits visited.
- Kernighan’s popcount loop runs in $O(\\text{number of set bits})$.

Tips and pitfalls:
- Use `bit_length()` to derive indices quickly. MSB index is `x.bit_length() - 1`.
- Right shifting negative numbers is generally avoided in CP code; stick to non-negative masks.
- For subset DP, iterate submasks of `mask` using the idiom below. The loop visits
  each submask once, so total work is proportional to the number of submasks.

This module provides:
- Bit manipulations: set, unset, toggle, test
- Queries: `is_power_of_two`, `count_set_bits`, `lowest_set_bit`, `msb_index`, `lsb_index`
- Iterators: `iterate_submasks(mask)`, `iterate_bits(mask)`
- Helper: `next_power_of_two(x)`

Use cases include subset enumeration, DP on bitmasks, and constructing fast
checks for properties like power-of-two and bit positions.
"""

def bit_set(x, i):
    return x | (1 << i)


def bit_unset(x, i):
    return x & ~(1 << i)


def bit_toggle(x, i):
    return x ^ (1 << i)


def bit_test(x, i):
    return ((x >> i) & 1) == 1


def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0


def count_set_bits(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


def lowest_set_bit(x):
    return x & -x


def msb_index(x):
    return x.bit_length() - 1 if x else -1


def lsb_index(x):
    return (x & -x).bit_length() - 1 if x else -1


def iterate_submasks(mask):
    s = mask
    while s:
        yield s
        s = (s - 1) & mask
    yield 0


def iterate_bits(mask):
    m = mask
    while m:
        lb = m & -m
        yield lb.bit_length() - 1
        m ^= lb


def next_power_of_two(x):
    if x <= 0:
        return 1
    return 1 << (x - 1).bit_length()


