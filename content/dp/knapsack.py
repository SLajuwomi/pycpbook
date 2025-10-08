"""
Knapsack problems appear in many variations. This section provides contest-ready
implementations and explains when to use each:

- 0/1 Knapsack: each item can be taken once. Weight-optimized 1D DP in $O(NC)$.
- Unbounded Knapsack: unlimited copies of each item. Forward 1D DP in $O(NC)$.
- Bounded Knapsack: limited copies per item. Use binary splitting to reduce to 0/1.
- Subset Sum via bitset: fast using Python integer shifts.
- 0/1 Value-Optimized: minimize weight to achieve value; useful when $C$ is large
  but total value is moderate.
- Bounded Knapsack (Monotone Queue): optimize per residue class to handle large
  capacities with counts.

Implementation notes:
- For 0/1, iterate capacity descending to avoid reusing an item.
- For unbounded, iterate ascending to allow multiple uses.
- Binary splitting transforms count into $O(\log m)$ items per original item.
- Bitset subset sum uses integer bit operations; shift left by weight and OR.
- Value-optimized uses value dimension; check minimal weight within capacity.
- Monotone queue optimization maintains a deque per residue class to enforce counts.
"""


def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            nv = dp[c - w] + v
            if nv > dp[c]:
                dp[c] = nv
    return dp[capacity]


def knapsack_unbounded(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(w, capacity + 1):
            nv = dp[c - w] + v
            if nv > dp[c]:
                dp[c] = nv
    return dp[capacity]


def knapsack_bounded(weights, values, counts, capacity):
    items_w = []
    items_v = []
    for w, v, m in zip(weights, values, counts):
        k = 1
        while m > 0:
            take = k if k <= m else m
            items_w.append(w * take)
            items_v.append(v * take)
            m -= take
            k <<= 1
    return knapsack_01(items_w, items_v, capacity)


def subset_sum_possible(nums, S):
    if S < 0:
        return False
    bits = 1
    for x in nums:
        if 0 <= x <= S:
            bits |= bits << x
    return ((bits >> S) & 1) == 1


def knapsack_01_value_optimized(weights, values, capacity):
    V = sum(values)
    INF = capacity + 1
    dp = [INF] * (V + 1)
    dp[0] = 0
    for w, v in zip(weights, values):
        for val in range(V, v - 1, -1):
            nw = dp[val - v] + w
            if nw < dp[val]:
                dp[val] = nw
    best = 0
    for val in range(V + 1):
        if dp[val] <= capacity and val > best:
            best = val
    return best


def knapsack_bounded_mq(weights, values, counts, capacity):
    dp = [0] * (capacity + 1)
    for w, v, m in zip(weights, values, counts):
        if w == 0:
            if v > 0 and m > 0:
                return v * m + dp[capacity]
            continue
        for r in range(w):
            deq = []
            idx = 0
            for c in range(r, capacity + 1, w):
                base = dp[c] - idx * v
                while deq and deq[-1][0] <= base:
                    deq.pop()
                deq.append((base, idx))
                while deq and deq[0][1] < idx - m:
                    deq.pop(0)
                dp[c] = deq[0][0] + idx * v
                idx += 1
    return dp[capacity]


