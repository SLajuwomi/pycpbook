import itertools
import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from content.dp.knapsack import (
    knapsack_01,
    knapsack_unbounded,
    knapsack_bounded,
    subset_sum_possible,
    knapsack_01_value_optimized,
    knapsack_bounded_mq,
)


def brute_knapsack_01(weights, values, C):
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        tw = 0
        tv = 0
        for i in range(n):
            if (mask >> i) & 1:
                tw += weights[i]
                tv += values[i]
        if tw <= C and tv > best:
            best = tv
    return best


def brute_unbounded(weights, values, C):
    dp = [0] * (C + 1)
    for c in range(C + 1):
        for w, v in zip(weights, values):
            if w <= c and dp[c - w] + v > dp[c]:
                dp[c] = dp[c - w] + v
    return dp[C]


def brute_bounded(weights, values, counts, C):
    items = []
    for w, v, m in zip(weights, values, counts):
        items.extend([(w, v)] * m)
    if not items:
        return 0
    W = [w for w, _ in items]
    V = [v for _, v in items]
    return brute_knapsack_01(W, V, C)


def verify_subset_sum(nums, S):
    n = len(nums)
    possible = set([0])
    for x in nums:
        newp = set()
        for s in possible:
            ns = s + x
            newp.add(ns)
        possible |= newp
    return (S in possible)


def run_random_tests():
    random.seed(0)
    # 0/1 and value-optimized cross-check
    for _ in range(400):
        n = random.randint(0, 10)
        W = [random.randint(1, 15) for _ in range(n)]
        V = [random.randint(0, 20) for _ in range(n)]
        C = random.randint(0, 60)

        ans01 = knapsack_01(W, V, C)
        brute01 = brute_knapsack_01(W, V, C)
        assert ans01 == brute01

        valopt = knapsack_01_value_optimized(W, V, C)
        assert valopt == brute01

    # unbounded
    for _ in range(200):
        n = random.randint(0, 8)
        W = [random.randint(1, 10) for _ in range(n)]
        V = [random.randint(0, 15) for _ in range(n)]
        C = random.randint(0, 50)

        ans_unb = knapsack_unbounded(W, V, C)
        brute_unb = brute_unbounded(W, V, C)
        assert ans_unb == brute_unb

    # bounded (binary split vs brute) and MQ cross-check
    for _ in range(200):
        n = random.randint(0, 8)
        W = [random.randint(1, 10) for _ in range(n)]
        V = [random.randint(0, 15) for _ in range(n)]
        M = [random.randint(0, 5) for _ in range(n)]
        C = random.randint(0, 50)

        ans_b = knapsack_bounded(W, V, M, C)
        brute_b = brute_bounded(W, V, M, C)
        assert ans_b == brute_b

        # MQ is optional optimization; compare when sums are not huge
        ans_mq = knapsack_bounded_mq(W, V, M, C)
        assert ans_mq == brute_b

    # subset sum bitset
    for _ in range(400):
        n = random.randint(0, 18)
        nums = [random.randint(0, 30) for _ in range(n)]
        S = random.randint(0, 200)
        bit = subset_sum_possible(nums, S)
        brute = verify_subset_sum(nums, S)
        assert bit == brute


def run_test():
    run_random_tests()
    print("Knapsack: All tests passed!")


if __name__ == "__main__":
    run_test()
