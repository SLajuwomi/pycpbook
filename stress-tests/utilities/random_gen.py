"""
@description
This module provides general-purpose utility functions for generating random data
for use in stress tests. These helpers simplify the creation of diverse and
randomized test cases for algorithms.

Key functions:
- random_int: Generates a random integer within a specified range.
- random_list: Generates a list of random integers.
- random_string: Generates a random string of a given length.
"""

import random
import string


def random_int(min_val, max_val):
    """
    Generates a single random integer within a specified inclusive range.

    Args:
        min_val (int): The minimum possible value for the random integer.
        max_val (int): The maximum possible value for the random integer.

    Returns:
        int: A random integer between min_val and max_val, inclusive.
    """
    return random.randint(min_val, max_val)


def random_list(size, min_val, max_val):
    """
    Generates a list of random integers.

    Args:
        size (int): The number of elements in the list.
        min_val (int): The minimum value for elements in the list.
        max_val (int): The maximum value for elements in the list.

    Returns:
        list[int]: A list of 'size' random integers.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def random_string(length, charset=string.ascii_lowercase):
    """
    Generates a random string of a given length from a character set.

    Args:
        length (int): The length of the string to generate.
        charset (str, optional): The set of characters to choose from.
                                 Defaults to lowercase English letters.

    Returns:
        str: A random string of the specified length.
    """
    return "".join(random.choice(charset) for _ in range(length))
