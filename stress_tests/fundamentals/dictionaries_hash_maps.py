import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from content.fundamentals.dictionaries_hash_maps import (
    freq_map,
    freq_map_counter,
    group_by_mod,
    add_to_bucket_dict,
    add_to_bucket_setdefault,
    add_to_bucket_defaultdict,
    make_defaultdict_list,
)


def run_random_tests():
    random.seed(0)
    for _ in range(3000):
        n = random.randint(0, 60)
        arr = [random.randint(-20, 20) for _ in range(n)]
        fm = freq_map(arr)
        fmc = freq_map_counter(arr)
        assert fm == fmc

        k = random.randint(1, 10)
        g = group_by_mod(arr, k)
        # naive grouping
        g2 = {}
        for x in arr:
            r = x % k
            g2.setdefault(r, []).append(x)
        assert g == g2

        # bucket add equivalence across patterns
        d1 = {}
        d2 = {}
        d3 = make_defaultdict_list()
        m = random.randint(0, 40)
        ops = [(random.randint(-5, 5), random.randint(-50, 50)) for _ in range(m)]
        for k_, v_ in ops:
            add_to_bucket_dict(d1, k_, v_)
            add_to_bucket_setdefault(d2, k_, v_)
            add_to_bucket_defaultdict(d3, k_, v_)
        assert d1 == d2 == dict(d3)


def run_test():
    run_random_tests()
    print("Dictionaries / Hash Maps: All tests passed!")


if __name__ == "__main__":
    run_test()


