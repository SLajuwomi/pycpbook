"""
@description
This script is a correctness test for the Python list operations examples provided in
`content/fundamentals/list_operations.py`. It ensures that all the example
code snippets are syntactically correct and produce the expected results.

This comprehensive test validates all list operations, initialization patterns,
common pitfalls, and advanced features covered in the educational content.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content.fundamentals.list_operations import list_operations_examples


def run_test():
    """
    Executes the example function and asserts the correctness of all outputs.
    """
    results = list_operations_examples()
    
    # === Test Initialization Patterns ===
    assert results["empty_list"] == []
    assert results["filled_list"] == [1, 2, 3, 4, 5]
    assert results["zeros_list"] == [0, 0, 0, 0, 0]
    assert results["matrix_2d"] == [[0, 0, 0], [0, 0, 0]]
    
    # Test the common mistake - all rows should be the same reference
    wrong_matrix = results["wrong_matrix"]
    assert wrong_matrix == [[1, 0, 0], [1, 0, 0]]
    assert wrong_matrix[0] is wrong_matrix[1]  # Same object reference
    
    # === Test Basic Modifications ===
    assert results["lst_after_operations"] == [0, 1, 3, 4, 5, 6, 7]
    assert results["last_element"] == 9
    assert results["element_at_2"] == 2
    assert results["temp_list_cleared"] == []
    
    # === Test Searching and Counting ===
    assert results["first_two_index"] == 1
    assert results["count_of_twos"] == 3
    assert results["has_three"] == True
    assert results["has_six"] == False
    
    # === Test Sorting and Reversing ===
    assert results["sorted_asc"] == [1, 1, 2, 3, 4, 5, 6, 9]
    assert results["sorted_desc"] == [9, 6, 5, 4, 3, 2, 1, 1]
    assert results["sorted_new"] == [1, 1, 3, 4, 5]
    assert results["original_unchanged"] == [3, 1, 4, 1, 5]  # Should be unchanged
    assert results["reverse_list"] == [5, 4, 3, 2, 1]
    assert results["reverse_slice"] == [5, 4, 3, 2, 1]
    
    # === Test Slicing Operations ===
    assert results["first_half"] == [0, 1, 2, 3, 4]
    assert results["second_half"] == [5, 6, 7, 8, 9]
    assert results["middle"] == [2, 3, 4, 5, 6]
    assert results["even_indices"] == [0, 2, 4, 6, 8]
    assert results["odd_indices"] == [1, 3, 5, 7, 9]
    assert results["reversed_slice"] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert results["last_element_slice"] == 9
    assert results["last_three"] == [7, 8, 9]
    
    # === Test Copying Operations ===
    # Test that shallow copies are affected by nested changes
    shallow1 = results["shallow_copy1"]
    shallow2 = results["shallow_copy2"]
    deep = results["deep_copy"]
    original = results["original_copy_modified"]
    
    # Original should have nested list modified
    assert original == [1, 2, [99, 4]]
    
    # Shallow copies should also be affected (same nested object reference)
    assert shallow1 == [1, 2, [99, 4]]
    assert shallow2 == [1, 2, [99, 4]]
    
    # Deep copy should be unaffected (separate nested object)
    assert deep == [1, 2, [3, 4]]
    
    # === Test List Comprehensions ===
    assert results["squares"] == [0, 1, 4, 9, 16]
    assert results["even_squares"] == [0, 4, 16, 36, 64]
    assert results["matrix_flatten"] == [1, 2, 3, 4]
    
    # === Test Advanced Operations ===
    assert results["enumerated"] == [(0, 'a'), (1, 'b'), (2, 'c')]
    assert results["zipped"] == [(1, 'a'), (2, 'b'), (3, 'c')]
    assert results["max_val"] == 9
    assert results["min_val"] == 1
    assert results["sum_val"] == 20
    
    print("List Operations: All examples are correct!")


if __name__ == "__main__":
    run_test()
