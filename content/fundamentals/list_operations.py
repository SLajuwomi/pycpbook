"""
This comprehensive guide covers Python lists, one of the most fundamental
data structures in competitive programming. Lists are dynamic arrays that can store
elements of different types and are highly optimized for various operations.
Basic List Operations:
Lists support numerous operations for manipulation and querying. Understanding the
time complexity of each operation is crucial for competitive programming efficiency.
- `append(x)`: Adds element x to the end of the list. This is an amortized $O(1)$
  operation, making it the preferred way to build lists incrementally.
- `pop()` / `pop(i)`: Removes and returns the last element (default) or element at
  index i. `pop()` is $O(1)$, but `pop(i)` is $O(N)$ as it requires shifting
  elements. Avoid `pop(0)` for large lists - use `collections.deque` instead.
- `insert(i, x)`: Inserts element x at index i, shifting subsequent elements.
  This is $O(N)$ due to element shifting, so use sparingly.
- `remove(x)`: Removes the first occurrence of x. This is $O(N)$ as it must
  search through the list. For frequent removals, consider using sets.
- `extend(iterable)`: Appends all elements from an iterable. More efficient
  than multiple `append()` calls for adding multiple elements.
- `clear()`: Removes all elements, equivalent to `del lst[:]`.
Searching and Counting Operations:
- `index(x)`: Returns the index of the first occurrence of x. Raises ValueError
  if not found. Use `try/except` or check `x in lst` first.
- `count(x)`: Returns the number of occurrences of x in the list.
- `x in lst`: Membership test returning True/False. Both `index()` and `count()`
  must scan the list, so they're $O(N)$.
Sorting and Reversing:
- `sort()`: Sorts the list in-place in $O(N \\log N)$ time. Use `sort(reverse=True)`
  for descending order. For custom sorting, use the `key` parameter.
- `sorted(lst)`: Returns a new sorted list without modifying the original.
- `reverse()`: Reverses the list in-place in $O(N)$ time.
- `lst[::-1]`: Creates a new reversed list using slicing.
List Initialization Patterns:
- `[]`: Empty list initialization.
- `[0] * n`: Creates a list of n zeros. Use with immutable types only.
- `[[0] * m for _ in range(n)]`: Creates a proper 2D list (n×m matrix).
- `[[0] * m] * n`: WRONG! Creates n references to the same list object.
Common Pitfalls:
1. Shallow vs Deep Copy: `lst[:]` and `lst.copy()` create shallow copies.
   For nested structures, use `copy.deepcopy()`.
2. Default Mutable Arguments: Never use `def func(lst=[])` as the same list
   object is reused across function calls. Use `def func(lst=None)` instead.
3. List Multiplication with Mutable Objects: `[[0] * 3] * 2` creates a list
   where all rows reference the same object.
Performance Tips for Competitive Programming:
- Pre-allocate lists when size is known: `lst = [0] * n`
- Use list comprehensions instead of loops for better performance
- For frequent insertions/deletions at the beginning, use `collections.deque`
- When building large lists, `append()` is faster than `insert(0, x)`
- Use `enumerate()` for index-value pairs instead of manual indexing
Memory Considerations:
- Lists grow dynamically, so memory usage can be higher than expected
- Use `del lst[i]` or `lst.pop(i)` to free memory when elements are no longer needed
- For very large datasets, consider using generators or processing in chunks
"""

import copy


def list_operations_examples():
    """
    Demonstrates comprehensive Python list operations and common patterns
    used in competitive programming. This function is primarily for inclusion
    in the notebook and is called by the stress test to ensure correctness.
    """
    
    # === Basic List Creation and Initialization ===
    empty_list = []
    filled_list = [1, 2, 3, 4, 5]
    zeros_list = [0] * 5
    matrix_2d = [[0] * 3 for _ in range(2)]
    
    # Common mistake - all rows reference the same object
    wrong_matrix = [[0] * 3] * 2
    wrong_matrix[0][0] = 1
    
    # === Basic Modifications ===
    # append() - O(1) amortized
    lst = [1, 2, 3]
    lst.append(4)
    lst.append(5)
    
    # extend() - O(k) where k is length of iterable
    lst.extend([6, 7, 8])
    
    # insert() - O(N)
    lst.insert(0, 0)
    lst.insert(3, 99)
    
    # remove() - O(N)
    lst.remove(99)
    
    # pop() operations
    last_element = lst.pop()  # O(1)
    element_at_2 = lst.pop(2)  # O(N)
    
    # clear()
    temp_list = [1, 2, 3]
    temp_list.clear()
    
    # === Searching and Counting ===
    search_list = [1, 2, 3, 2, 4, 2, 5]
    
    # index() - O(N)
    first_two_index = search_list.index(2)
    
    # count() - O(N)
    count_of_twos = search_list.count(2)
    
    # membership test - O(N)
    has_three = 3 in search_list
    has_six = 6 in search_list
    
    # === Sorting and Reversing ===
    sort_list = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # sort() - in-place, O(N log N)
    sort_list.sort()
    sorted_asc = sort_list.copy()
    
    # sort(reverse=True)
    sort_list.sort(reverse=True)
    sorted_desc = sort_list.copy()
    
    # sorted() - returns new list
    original = [3, 1, 4, 1, 5]
    sorted_new = sorted(original)
    
    # reverse() - in-place, O(N)
    reverse_list = [1, 2, 3, 4, 5]
    reverse_list.reverse()
    
    # slicing for reversal - creates new list
    reverse_slice = [1, 2, 3, 4, 5][::-1]
    
    # === Slicing Operations ===
    slice_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Basic slicing
    first_half = slice_list[:5]
    second_half = slice_list[5:]
    middle = slice_list[2:7]
    
    # Step slicing
    even_indices = slice_list[::2]
    odd_indices = slice_list[1::2]
    reversed_slice = slice_list[::-1]
    
    # Negative indexing
    last_element = slice_list[-1]
    last_three = slice_list[-3:]
    
    # === Copying Operations ===
    original_copy = [1, 2, [3, 4]]
    
    # Shallow copy methods
    shallow_copy1 = original_copy[:]
    shallow_copy2 = original_copy.copy()
    
    # Deep copy
    deep_copy = copy.deepcopy(original_copy)
    
    # Demonstrate shallow vs deep copy
    original_copy[2][0] = 99
    
    # === List Comprehensions ===
    squares = [x * x for x in range(5)]
    even_squares = [x * x for x in range(10) if x % 2 == 0]
    matrix_flatten = [x for row in [[1, 2], [3, 4]] for x in row]
    
    # === Advanced Operations ===
    # enumerate() for index-value pairs
    enumerated = list(enumerate(['a', 'b', 'c']))
    
    # zip() for pairing lists
    zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))
    
    # max, min, sum
    numbers = [1, 5, 3, 9, 2]
    max_val = max(numbers)
    min_val = min(numbers)
    sum_val = sum(numbers)
    
    return {
        # Initialization results
        "empty_list": empty_list,
        "filled_list": filled_list,
        "zeros_list": zeros_list,
        "matrix_2d": matrix_2d,
        "wrong_matrix": wrong_matrix,
        
        # Basic modifications
        "lst_after_operations": lst,
        "last_element": last_element,
        "element_at_2": element_at_2,
        "temp_list_cleared": temp_list,
        
        # Searching results
        "first_two_index": first_two_index,
        "count_of_twos": count_of_twos,
        "has_three": has_three,
        "has_six": has_six,
        
        # Sorting results
        "sorted_asc": sorted_asc,
        "sorted_desc": sorted_desc,
        "sorted_new": sorted_new,
        "original_unchanged": original,
        "reverse_list": reverse_list,
        "reverse_slice": reverse_slice,
        
        # Slicing results
        "first_half": first_half,
        "second_half": second_half,
        "middle": middle,
        "even_indices": even_indices,
        "odd_indices": odd_indices,
        "reversed_slice": reversed_slice,
        "last_element_slice": last_element,
        "last_three": last_three,
        
        # Copying results
        "shallow_copy1": shallow_copy1,
        "shallow_copy2": shallow_copy2,
        "deep_copy": deep_copy,
        "original_copy_modified": original_copy,
        
        # List comprehensions
        "squares": squares,
        "even_squares": even_squares,
        "matrix_flatten": matrix_flatten,
        
        # Advanced operations
        "enumerated": enumerated,
        "zipped": zipped,
        "max_val": max_val,
        "min_val": min_val,
        "sum_val": sum_val,
    }
