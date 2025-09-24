"""
@description
This script is a simple demonstration and correctness test for the custom hash
implementation. It doesn't perform a "stress test" in the traditional sense of
validating against a naive solution for performance, but rather ensures that
the `CustomHash` wrapper works as intended with Python's built-in dictionary.

The test does the following:
1.  Creates a large number of integer keys.
2.  Wraps each key in a `CustomHash` object.
3.  Inserts these wrapped keys into a standard Python dictionary.
4.  Verifies that each inserted key can be successfully looked up.
5.  Verifies that keys that were not inserted are not found.

This test confirms that the `__hash__` and `__eq__` methods of the `CustomHash`
class are correctly implemented and that the wrapper can be used reliably to
store and retrieve values from a hash map.
"""

import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.data_structures.hash_map_custom import CustomHash


def run_test():
    """
    Performs a correctness test on the CustomHash implementation.
    """
    NUM_KEYS = 10000
    MAX_VAL = 10**9

    custom_dict = {}
    keys_present = set()

    for i in range(NUM_KEYS):
        key = random.randint(0, MAX_VAL)
        custom_key = CustomHash(key)
        value = f"value_for_{key}"

        custom_dict[custom_key] = value
        keys_present.add(key)

    # Verify that all inserted keys can be found
    for key in keys_present:
        custom_key = CustomHash(key)
        assert (
            custom_key in custom_dict
        ), f"Key {key} should be in the dict, but was not found."
        expected_value = f"value_for_{key}"
        assert (
            custom_dict[custom_key] == expected_value
        ), f"Value mismatch for key {key}."

    # Verify that some non-inserted keys are not found
    for _ in range(NUM_KEYS):
        key = random.randint(MAX_VAL + 1, 2 * MAX_VAL)
        if key not in keys_present:
            custom_key = CustomHash(key)
            assert (
                custom_key not in custom_dict
            ), f"Key {key} should not be in the dict, but was found."

    print("Custom Hash Map: All tests passed!")


if __name__ == "__main__":
    run_test()
