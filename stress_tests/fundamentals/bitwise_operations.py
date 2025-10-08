import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from content.fundamentals import bitwise_operations as B


def naive_count_set_bits(x):
    return bin(x & ((1 << 64) - 1)).count('1') if x >= 0 else bin(x & ((1 << 64) - 1)).count('1')


def naive_lowest_set_bit(x):
    if x == 0:
        return 0
    i = 0
    while ((x >> i) & 1) == 0:
        i += 1
    return 1 << i


def naive_msb_index(x):
    if x == 0:
        return -1
    i = 0
    while (1 << (i + 1)) <= x:
        i += 1
    return i


def naive_lsb_index(x):
    if x == 0:
        return -1
    i = 0
    while ((x >> i) & 1) == 0:
        i += 1
    return i


def submasks_naive(mask):
    res = []
    pc = naive_count_set_bits(mask)
    bits = [i for i in range(32) if (mask >> i) & 1]
    for s in range(1 << pc):
        m = 0
        for j, b in enumerate(bits):
            if (s >> j) & 1:
                m |= 1 << b
        res.append(m)
    return sorted(res)


def run_test():
    random.seed(0)
    # Validate bit helpers and queries
    for _ in range(3000):
        x = random.getrandbits(24)
        i = random.randrange(0, 24)

        # set/unset/toggle/test roundtrip
        y = B.bit_set(x, i)
        assert ((y >> i) & 1) == 1
        z = B.bit_unset(y, i)
        assert ((z >> i) & 1) == 0
        t = B.bit_toggle(z, i)
        assert ((t >> i) & 1) == 1
        assert B.bit_test(t, i) is True
        t2 = B.bit_toggle(t, i)
        assert B.bit_test(t2, i) is False

        # power of two
        p2 = 1 << random.randrange(0, 24)
        assert B.is_power_of_two(p2) is True
        if p2 > 1:
            assert B.is_power_of_two(p2 + 1) is False

        # popcount
        assert B.count_set_bits(x) == bin(x).count('1')

        # lowbit
        assert B.lowest_set_bit(x) == naive_lowest_set_bit(x)

        # indices
        assert B.msb_index(x) == naive_msb_index(x)
        assert B.lsb_index(x) == naive_lsb_index(x)

        # iterate_bits covers exactly set bit indices
        idxs = list(B.iterate_bits(x))
        idxs_sorted = sorted(idxs)
        idxs_truth = [j for j in range(24) if ((x >> j) & 1) == 1]
        assert idxs_sorted == idxs_truth

        # next_power_of_two
        n = random.randrange(-2, 1 << 20)
        nxt = B.next_power_of_two(n)
        if n <= 1:
            assert nxt == 1
        else:
            assert nxt >= n and (nxt & (nxt - 1)) == 0 and (nxt >> 1) < n

    # Validate submask iteration
    for _ in range(500):
        mask = random.getrandbits(18)
        subs = sorted(B.iterate_submasks(mask))
        subs_naive = submasks_naive(mask)
        assert subs == subs_naive

    print("Passed!")


if __name__ == "__main__":
    run_test()


