"""
Author: PyCPBook Community
Source: Standard computer science curriculum (e.g., CLRS)
Description: This guide provides a template and explanation for recursion and
backtracking. Backtracking is a general algorithmic technique for solving
problems recursively by trying to build a solution incrementally, one piece at a
time, and removing those solutions ("backtracking") that fail to satisfy the
constraints of the problem at any point in time.

The core of backtracking is a recursive function that follows a "choose,
explore, unchoose" pattern:
1.  **Choose**: Make a choice at the current state. This could be including an
    element in a subset, placing a queen on a chessboard, or moving to a new
    cell in a maze.
2.  **Explore**: Recursively call the function to explore further possibilities
    that arise from the choice made.
3.  **Unchoose**: After the recursive call returns, undo the choice made in
    step 1. This is the "backtracking" step. It allows the algorithm to explore
    other paths from the current state.

The example below, "generating all subsets," demonstrates this pattern perfectly.
To generate all subsets of a set of numbers, we can iterate through the numbers.
For each number, we have two choices: include it in the current subset, or not
include it. The backtracking function explores both paths.

Time: $O(N \\cdot 2^N)$. There are $2^N$ possible subsets. For each subset, it
takes up to $O(N)$ time to create a copy to add to the results list.
Space: $O(N)$ for the recursion depth and the temporary list storing the current
subset. The output list itself requires $O(N \\cdot 2^N)$ space.
Status: To be stress-tested
"""


def generate_subsets(nums):
    """
    Generates all possible subsets (the power set) of a list of numbers.

    Args:
        nums (list[int]): A list of numbers.

    Returns:
        list[list[int]]: A list containing all subsets of nums.
    """
    result = []
    current_subset = []

    def backtrack(start_index):
        # Add the current subset configuration to the result list.
        # A copy is made because current_subset will be modified.
        result.append(list(current_subset))

        # Explore further choices.
        for i in range(start_index, len(nums)):
            # 1. Choose: Include the number nums[i] in the current subset.
            current_subset.append(nums[i])

            # 2. Explore: Recursively call with the next index.
            backtrack(i + 1)

            # 3. Unchoose: Remove nums[i] to backtrack and explore other paths.
            current_subset.pop()

    backtrack(0)
    return result
