"""
@description
This script is a stress test for the Aho-Corasick algorithm. It validates the
correctness of the `AhoCorasick` class by comparing its results against a naive,
brute-force search over a large number of randomized test cases.

The test workflow is as follows:
1.  A `naive_search` function is defined. It finds all occurrences by iterating
    through each pattern and using Python's built-in `string.find()` method in a
    loop.
2.  For many iterations, a random text string and a random set of pattern
    strings are generated.
3.  The `AhoCorasick` class is instantiated with the patterns to build the
    automaton.
4.  The `search` method is called on the text.
5.  The `naive_search` is also performed on the same text and patterns.
6.  The results from both searches are collected. Since the Aho-Corasick
    algorithm reports the ending index of a match, the results are converted
    to starting indices for a fair comparison.
7.  The lists of found matches (as `(pattern_index, start_index)` tuples) are
    sorted and then asserted to be identical.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.string.aho_corasick import AhoCorasick
from stress_tests.utilities.random_gen import random_string


def naive_search(text, patterns):
    """
    A naive implementation of multi-pattern search for validation.
    """
    matches = []
    for i, pattern in enumerate(patterns):
        if not pattern:
            continue
        start_index = 0
        while True:
            index = text.find(pattern, start_index)
            if index == -1:
                break
            matches.append((i, index))
            start_index = index + 1
    return matches


def run_test():
    """
    Performs a stress test on the Aho-Corasick implementation.
    """
    ITERATIONS = 200
    MAX_TEXT_LEN = 1000
    MAX_PATTERNS = 50
    MAX_PATTERN_LEN = 20
    ALPHABET = "abc"

    for i in range(ITERATIONS):
        text_len = random.randint(100, MAX_TEXT_LEN)
        text = random_string(text_len, ALPHABET)

        num_patterns = random.randint(1, MAX_PATTERNS)
        patterns = []
        for _ in range(num_patterns):
            p_len = random.randint(1, MAX_PATTERN_LEN)
            patterns.append(random_string(p_len, ALPHABET))

        # Ensure unique patterns to simplify testing logic
        patterns = list(set(patterns))

        # Optimized search
        ac = AhoCorasick(patterns)
        res_optimized_raw = ac.search(text)

        # Convert end indices to start indices
        res_optimized = []
        for p_idx, end_idx in res_optimized_raw:
            start_idx = end_idx - len(patterns[p_idx]) + 1
            res_optimized.append((p_idx, start_idx))

        # Naive search
        res_naive = naive_search(text, patterns)

        # Sort for canonical comparison
        res_optimized.sort()
        res_naive.sort()

        assert res_optimized == res_naive, (
            f"Aho-Corasick search failed on iteration {i}!\n"
            f"Text: '{text[:100]}...'\n"
            f"Patterns: {patterns}\n"
            f"Expected: {res_naive}\n"
            f"Got: {res_optimized}"
        )

    print("Aho-Corasick: All tests passed!")


if __name__ == "__main__":
    run_test()
