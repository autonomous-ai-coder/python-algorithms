# aac-quicksort

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![Version](https://img.shields.io/badge/version-0.1.0-orange.svg)

## Description

A package that implements the quicksort algorithm for sorting integers.

## Installation

You can install the package using pip:
```bash
pip install aac-quicksort
```

## Usage

Here's how to use the quicksort function:
```python
from aac_quicksort import quicksort

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
```

## Test Results

✅ All tests passing

### Coverage
- Lines covered: 100.0%
- Branches covered: 0.0%

### Test Cases
- Sort a basic list of integers  
  - Input: `sorted_data`  
  - Expected: `[1, 1, 2, 3, 6, 8, 10]`
- Sort an empty list  
  - Input: `empty_data`  
  - Expected: `[]`
- Sort a large list of integers  
  - Input: `large_data`  
  - Expected: `sorted list of 10000 to 1`

### Edge Cases
- Empty list  
- Very large list