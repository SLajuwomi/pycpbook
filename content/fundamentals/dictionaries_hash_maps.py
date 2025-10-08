"""
Dictionaries (hash maps) are essential in competitive programming for constant
average-time lookups, counts, grouping, and memoization. This section covers
core operations, performance notes, common patterns like frequency maps and
"dictionary of lists", and typical CP use-cases.

Basics:
- Creation: `{}`, `dict()`, from pairs: `dict([(k, v), ...])`
- Access: `d[k]`, safe get: `d.get(k, default)`, membership: `k in d`
- Update: `d[k] = v`, `d.update(other)`
- Removal: `del d[k]`, `d.pop(k, default)`, `d.popitem()`
- Iteration: `for k in d`, `for k, v in d.items()`, `for v in d.values()`
- Copy: `d.copy()`, `dict(d)`; note nested structures require explicit copies

Performance and behavior:
- Average $O(1)$ insert/lookup/delete with good hashing
- Keys must be hashable and compared by equality; do not use mutable keys
- Python preserves insertion order, but algorithms should not depend on it

Frequency maps and counters:
- Manual counting: increment with guard or using `get`
- `collections.Counter` provides counting, `most_common`, and arithmetic, but
  manual dicts are often faster to type and sufficient for contests

Dictionary of lists (grouping/bucketing):
- Guard pattern: initialize list when missing
- `setdefault`: concise way to initialize-and-append
- `defaultdict(list)`: best when many keys are created dynamically

Memoization tables:
- Use dicts for top-down DP caching when states are irregular or sparse
- Compare with `functools.lru_cache` when using pure functions

Common CP use-cases:
- Two-sum index map, sliding window frequency map
- Grouping by key (e.g., modulo buckets), adjacency lists
- Coordinate compression maps from values to ranks

Pitfalls:
- Mutating a shared list across keys by accident; create new lists per key
- Using unhashable keys (lists, dicts); prefer tuples for composite keys
- Memory growth from unbounded maps; clear or reuse when appropriate
"""

from collections import defaultdict, Counter


def freq_map(arr):
    d = {}
    for x in arr:
        d[x] = d.get(x, 0) + 1
    return d


def freq_map_counter(arr):
    return dict(Counter(arr))


def group_by_mod(arr, k):
    d = {}
    for x in arr:
        r = x % k
        if r not in d:
            d[r] = []
        d[r].append(x)
    return d


def add_to_bucket_dict(d, k, v):
    if k not in d:
        d[k] = []
    d[k].append(v)
    return d


def add_to_bucket_setdefault(d, k, v):
    d.setdefault(k, []).append(v)
    return d


def add_to_bucket_defaultdict(d, k, v):
    d[k].append(v)
    return d


def make_defaultdict_list():
    return defaultdict(list)


