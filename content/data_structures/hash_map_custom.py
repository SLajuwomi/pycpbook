"""
Author: PyCPBook Community
Source: KACTL, neal wu's blog
Description: Provides an explanation and an example of a custom hash for Python's
dictionaries and sets to prevent slowdowns from anti-hash tests. In competitive
programming, some problems use test cases specifically designed to cause many
collisions in standard hash table implementations (like Python's dict),
degrading their performance from average $O(1)$ to worst-case $O(N)$.

This can be mitigated by using a hash function with a randomized component, so
that the hash values are unpredictable to an adversary. A common technique is to
XOR the object's standard hash with a fixed, randomly generated constant.

The `splitmix64` function shown below is a high-quality hash function that can be
used for this purpose. It's simple, fast, and provides good distribution.

To use a custom hash, you can wrap integer or tuple keys in a custom class that
overrides the `__hash__` and `__eq__` methods.

Example usage with a dictionary:
`my_map = {}`
`my_map[CustomHash(123)] = "value"`

This forces Python's `dict` to use your `CustomHash` object's `__hash__` method,
thus using the randomized hash function. This is particularly useful in problems
involving hashing of tuples, such as coordinates or polynomial hash values.
Time: The hash computation is $O(1)$. Dictionary operations remain amortized $O(1)$.
Space: Adds a small constant overhead per key for the wrapper object.
Status: Not applicable (Utility/Informational)
"""

import time

# A fixed random seed ensures the same hash function for each run,
# but it's generated based on time to be unpredictable.
SPLITMIX64_SEED = int(time.time()) ^ 0x9E3779B97F4A7C15


def splitmix64(x):
    """A fast, high-quality hash function for 64-bit integers."""
    x += 0x9E3779B97F4A7C15
    x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9
    x = (x ^ (x >> 27)) * 0x94D049BB133111EB
    return x ^ (x >> 31)


class CustomHash:
    """
    A wrapper class for hashable objects to use a custom hash function.
    This helps prevent collisions from anti-hash test cases.
    """

    def __init__(self, obj):
        self.obj = obj

    def __hash__(self):
        # Combine the object's hash with a fixed random seed using a robust function.
        return splitmix64(hash(self.obj) + SPLITMIX64_SEED)

    def __eq__(self, other):
        # The wrapped objects must still be comparable.
        return self.obj == other.obj

    def __repr__(self):
        return f"CustomHash({self.obj})"


# Example of how to use it
def custom_hash_example():
    # Standard dictionary, potentially vulnerable
    standard_dict = {}
    # Dictionary with custom hash, much more robust
    custom_dict = {}

    key = (12345, 67890)  # A tuple key, common in geometry or hashing problems

    # Using the standard hash
    standard_dict[key] = "some value"

    # Using the custom hash
    custom_key = CustomHash(key)
    custom_dict[custom_key] = "some value"

    print(f"Standard hash for {key}: {hash(key)}")
    print(f"Custom hash for {key}: {hash(custom_key)}")

    # Verifying that it works
    assert custom_key in custom_dict
    assert CustomHash(key) in custom_dict
    assert CustomHash((0, 0)) not in custom_dict
