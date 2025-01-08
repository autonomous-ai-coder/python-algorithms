# aac-quicksort

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg) ![Version](https://img.shields.io/badge/version-0.1.0-brightgreen.svg)

## Description
A package that provides a quicksort algorithm to sort a list of integers.

## Installation
To install the package, use pip:
```bash
pip install aac-quicksort
```

## Usage
Here is an example of how to use the quicksort function:
```python
from aac_quicksort import quicksort

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

## Test Results
### Test Coverage
- Lines covered: 100.0%
- Branches covered: 0.0%

### Test Cases
- Basic functionality test with a list of integers
  - Input: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`
  - Expected: `[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]`

### Edge Cases
- Empty input list should return an empty list
- Large input list should be sorted correctly
- Single element list should return the same list
- List with duplicate elements should be sorted correctly
- Already sorted list should remain unchanged
