"""
Author: PyCPBook Community
Source: Introduction to Algorithms (CLRS)
Description: Implements the classic binary search algorithm to find the index of
a specific target value within a sorted array. Binary search is a highly
efficient search algorithm that works by repeatedly dividing the search interval
in half.

This implementation searches for an exact match of a `target` value within a
sorted array `arr`.

The algorithm maintains a search space as an inclusive range `[low, high]`.
In each step, it examines the middle element `arr[mid]`:
- If `arr[mid]` is equal to the `target`, the index `mid` is returned.
- If `arr[mid]` is less than the `target`, the search continues in the right
  half of the array, by setting `low = mid + 1`.
- If `arr[mid]` is greater than the `target`, the search continues in the left
  half of the array, by setting `high = mid - 1`.

The loop continues as long as `low <= high`. If the loop terminates without
finding the target, it means the target is not present in the array, and the
function returns -1.

This version is suitable for problems where you need to check for the presence
of a specific value and get its index. For problems requiring finding the first
element satisfying a condition (lower/upper bound), a different variant of
binary search is needed.
Time: $O(\log N)$, where $N$ is the number of elements in the array.
Space: $O(1)$
Status: Stress-tested
"""


def binary_search(arr, target):
    """
    Searches for a target value in a sorted array.

    Args:
        arr (list): A sorted list of elements.
        target: The value to search for.

    Returns:
        int: The index of the target in the array if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
