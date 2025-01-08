
# quicksort_package

A package that implements the quicksort algorithm.

## Installation

```bash
pip install quicksort_package
```

## Usage

```python
from typing import List


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

## Explanation

The quicksort function works by choosing a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. In this implementation, the pivot is chosen to be the middle element of the array. Elements equal to the pivot are put in the 'middle' list and are not further sorted.

## Tests

import pytest
from typing import List


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


@pytest.fixture
def unsorted_list():
    return [3, 6, 8, 10, 1, 2, 1]


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def single_element_list():
    return [42]


@pytest.fixture
def sorted_list():
    return [1, 2, 3, 4, 5]


def test_quick_sort_basic_functionality(unsorted_list):
    """
    Test basic functionality of quicksort with a typical unsorted list.
    """
    assert quicksort(unsorted_list) == [1, 1, 2, 3, 6, 8, 10]


def test_quick_sort_empty_list(empty_list):
    """
    Test quicksort with an empty list.
    """
    assert quicksort(empty_list) == []


def test_quick_sort_single_element(single_element_list):
    """
    Test quicksort with a single element list.
    """
    assert quicksort(single_element_list) == [42]


def test_quick_sort_already_sorted(sorted_list):
    """
    Test quicksort with an already sorted list.
    """
    assert quicksort(sorted_list) == [1, 2, 3, 4, 5]


def test_quick_sort_reverse_sorted():
    """
    Test quicksort with a reverse sorted list.
    """
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_quick_sort_duplicates():
    """
    Test quicksort with a list containing duplicates.
    """
    assert quicksort([3, 3, 2, 1, 4, 4]) == [1, 2, 3, 3, 4, 4]


def test_quick_sort_large_input():
    """
    Test quicksort performance with a large input list.
    """
    input_list = list(range(1000, 0, -1))  # Reverse sorted list
    assert quicksort(input_list) == list(range(1, 1001))


def test_quick_sort_error_conditions():
    """
    Test quicksort error conditions with invalid input types.
    """
    with pytest.raises(TypeError):
        quicksort(None)
    with pytest.raises(TypeError):
        quicksort(42)
    with pytest.raises(TypeError):
        quicksort([1, 'two', 3])  # Mixed types


# Performance testing can be done using pytest-benchmark or similar tools.
# Here we demonstrate a simple performance test by checking execution time for large datasets.
import time

def test_quick_sort_performance():
    """
    Test execution time for sorting a large list.
    """
    input_list = list(range(100000, 0, -1))  # Reverse sorted list
    start_time = time.time()
    quicksort(input_list)
    duration = time.time() - start_time
    assert duration < 2  # Ensure it runs in under 2 seconds for large input

## Requirements


