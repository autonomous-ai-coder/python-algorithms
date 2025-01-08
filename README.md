# aac-quicksort

![Python package](https://img.shields.io/badge/python-3.6%2B-blue.svg) ![Version](https://img.shields.io/badge/version-0.1.0-brightgreen.svg)

## Description
A package that implements the quicksort algorithm to sort a list of integers.

## Installation
To install the package, use pip:
```bash
pip install aac-quicksort
```

## Usage
Here's how to use the quicksort function:
```python
from aac_quicksort import quicksort

unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = quicksort(unsorted_list)
print(sorted_list)  # Output: [5, 7, 23, 32, 34, 62]
```

## Test Results
### Test Coverage
✅ All tests passing

- **Lines covered:** 100.0%
- **Branches covered:** 0.0%

### Test Cases
- Test quicksort with a basic unsorted list.
  - Input: `small_unsorted_list`
  - Expected: `sorted(small_unsorted_list)`
- Test quicksort with an empty list.
  - Input: `empty_list`
  - Expected: `[]`
- Test quicksort with a large unsorted list for performance.
  - Input: `large_unsorted_list`
  - Expected: `sorted(large_unsorted_list)`
- Test quicksort with a single element list.
  - Input: `[42]`
  - Expected: `[42]`
- Test quicksort with all elements identical.
  - Input: `[5, 5, 5, 5, 5]`
  - Expected: `[5, 5, 5, 5, 5]`

### Edge Cases
- Empty list
- Single element list
- All elements identical

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.