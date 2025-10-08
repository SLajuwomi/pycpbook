"""
This section provides a reference for common and powerful Python
idioms that are particularly useful in competitive programming for writing
concise, efficient, and readable code.
List, Set, and Dictionary Comprehensions:
A concise way to create lists, sets, and dictionaries. The syntax is
`[expression for item in iterable if condition]`. This is often faster and
more readable than using explicit `for` loops with `.append()`.
Advanced Sorting:
Python's `sorted()` function and the `.sort()` list method are highly optimized.
They can be customized using a `key` argument, which is typically a `lambda`
function. This allows for sorting complex objects based on specific attributes
or computed values without writing a full comparison function.
String Manipulations:
- Slicing: Python's slicing `s[start:stop:step]` is a powerful tool for
  substrings and reversing. `s[::-1]` reverses a string in $O(N)$ time.
- `split()` and `join()`: These methods are the standard way to parse
  space-separated input and format list-based output. `line.split()` handles
  various whitespace, and `' '.join(map(str, my_list))` is a common output pattern.
Character and Number Conversions:
- `ord(c)`: Returns the ASCII/Unicode integer value of a single character `c`.
  For example, `ord('a')` is 97. This is useful for character arithmetic, like
  `ord(char) - ord('a')` to get a 0-indexed alphabet position.
- `chr(i)`: The inverse of `ord()`. Returns the character for an integer ASCII
  value `i`. For example, `chr(97)` is `'a'`.
- `int(s)` and `str(i)`: Standard functions to convert strings to integers and
  integers to strings, respectively.
"""


def python_idioms_examples():
    """
    Demonstrates various Python idioms useful in competitive programming.
    This function is primarily for inclusion in the notebook and is called
    by the stress test to ensure correctness.
    """
    # List Comprehensions
    squares = [x * x for x in range(5)]
    even_squares = [x * x for x in range(10) if x % 2 == 0]

    # Set and Dictionary Comprehensions
    unique_squares = {x * x for x in [-1, 1, -2, 2]}
    square_map = {x: x * x for x in range(5)}

    # Advanced Sorting
    pairs = [(1, 5), (3, 2), (2, 8)]
    sorted_by_second = sorted(pairs, key=lambda p: p[1])

    # String Manipulations
    sentence = "this is a sentence"
    words = sentence.split()
    rejoined = "-".join(words)
    reversed_sentence = sentence[::-1]

    # Character and Number Conversions
    char_a = "a"
    ord_a = ord(char_a)
    chr_97 = chr(97)
    num_str = "123"
    num_int = int(num_str)
    back_to_str = str(num_int)

    # The function can return the values to be checked by a test script.
    return {
        "squares": squares,
        "even_squares": even_squares,
        "unique_squares": unique_squares,
        "square_map": square_map,
        "sorted_by_second": sorted_by_second,
        "words": words,
        "rejoined": rejoined,
        "reversed_sentence": reversed_sentence,
        "ord_a": ord_a,
        "chr_97": chr_97,
        "num_int": num_int,
        "back_to_str": back_to_str,
    }
