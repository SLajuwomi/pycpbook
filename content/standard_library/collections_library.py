"""
This guide covers essential data structures from Python's `collections`
module that are extremely useful in competitive programming: `deque`, `Counter`,
and `defaultdict`.
`collections.deque`:
A double-ended queue that supports adding and removing elements from both ends in
$O(1)$ time. This makes it a highly efficient implementation for both queues
(using `append` and `popleft`) and stacks (using `append` and `pop`). It is
generally preferred over a `list` for queue operations because `list.pop(0)` is an
$O(N)$ operation.
`collections.Counter`:
A specialized dictionary subclass for counting hashable objects. It's a convenient
way to tally frequencies of elements in a list or characters in a string.
It supports common operations like initialization from an iterable, accessing
counts (which defaults to 0 for missing items), and arithmetic operations for
combining counters.
`collections.defaultdict`:
A dictionary subclass that calls a factory function to supply missing values.
When a key is accessed for the first time, it is not present in the dictionary,
so the factory function is called to create a default value for that key. This
is useful for avoiding `KeyError` checks when, for example, building an
adjacency list (`defaultdict(list)`) or counting items (`defaultdict(int)`).
element access and update for `Counter` and `defaultdict`) are amortized $O(1)$.
"""

from collections import deque, Counter, defaultdict


def collections_examples():
    """
    Demonstrates the usage of deque, Counter, and defaultdict.
    This function is primarily for inclusion in the notebook and is called
    by the stress test to ensure correctness.
    """
    # --- deque ---
    q = deque([1, 2, 3])
    q.append(4)
    q.appendleft(0)
    q_pop_left = q.popleft()
    q_pop_right = q.pop()

    # --- Counter ---
    data = ["a", "b", "c", "a", "b", "a"]
    counts = Counter(data)
    count_of_a = counts["a"]
    count_of_d = counts["d"]

    # --- defaultdict ---
    adj = defaultdict(list)
    edges = [(0, 1), (0, 2), (1, 2)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Access a missing key to trigger the default factory
    missing_key_val = adj[5]

    return {
        "final_deque": list(q),
        "q_pop_left": q_pop_left,
        "q_pop_right": q_pop_right,
        "counter_a": count_of_a,
        "counter_d": count_of_d,
        "adj_list": dict(adj),
        "adj_list_missing": missing_key_val,
    }
