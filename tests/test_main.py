@pytest.fixture
def sorted_data():
    """
    Fixture that returns a basic sorted and unsorted list of integers.
    """
    return [3, 6, 8, 10, 1, 2, 1]

@pytest.fixture
def empty_data():
    """
    Fixture that returns an empty list.
    """
    return []

@pytest.fixture
def large_data():
    """
    Fixture that returns a large list of integers for performance testing.
    """
    return list(range(10000, 0, -1))

def test_basic_functionality(sorted_data):
    """
    Test the quicksort function on a basic unsorted list.
    """
    assert quicksort(sorted_data) == sorted(sorted_data)

def test_edge_case_empty_list(empty_data):
    """
    Test the quicksort function with an empty list.
    """
    assert quicksort(empty_data) == []

def test_edge_case_large_list(large_data):
    """
    Test the quicksort function with a large list to check performance.
    """
    result = quicksort(large_data)
    assert result == sorted(large_data)

# Note: Python's recursion depth may limit the input size that can be handled by this test
# In practice, this test checks if the algorithm can handle large inputs efficiently.