from typing import List
import sys

sys.setrecursionlimit(10**6)

def quicksort(arr: List[int]) -> List[int]:
    """
    Sorts an array of integers using the quicksort algorithm.

    :param arr: List of integers to sort.
    :return: A new sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)