from typing import List


def quicksort(arr: List[int]) -> List[int]:
    """
    Sorts an array of integers using the quicksort algorithm.

    Args:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: A new list with the sorted integers.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
