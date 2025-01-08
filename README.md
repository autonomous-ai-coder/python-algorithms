# aac-quicksort

![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg) ![Version](https://img.shields.io/badge/version-0.1.0-brightgreen.svg)

## Description
A Python package that implements the quicksort algorithm for sorting lists of integers.

## Installation
To install the package, use pip:
```bash
pip install aac-quicksort
```

## Usage
To use the quicksort function, you can import it as follows:
```python
from aac_quicksort import quicksort

sorted_list = quicksort([7, 5, 6, 4, 8])
print(sorted_list)  # Output: [4, 5, 6, 7, 8]
```

## Test Results
✅ All tests passing

### Coverage
- Lines covered: 100.0%
- Branches covered: 0.0%

### Test Cases
- **Basic test with sorted data**  
  **Input:** `sorted_data`  
  **Expected:** `[4, 5, 6, 7, 8]`  
- **Basic test with unsorted data**  
  **Input:** `unsorted_data`  
  **Expected:** `[4, 5, 6, 7, 8]`

### Edge Cases
- Empty list
- Single element list
- List with identical elements

## License
This project is licensed under the MIT License.